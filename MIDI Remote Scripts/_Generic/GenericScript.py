# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Generic\GenericScript.py
# Compiled at: 2018-11-30 15:48:11
from __future__ import absolute_import, print_function, unicode_literals
from functools import partial
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.Layer import Layer
from _Framework.TransportComponent import TransportComponent
from .SpecialMixerComponent import SpecialMixerComponent

def is_valid_midi_channel(integer):
    return 0 <= integer < 16


def is_valid_midi_identifier(integer):
    return 0 <= integer < 128


def has_specification_for(control, specifications):
    return is_valid_midi_identifier(specifications.get(control, -1))


class GenericScript(ControlSurface):
    """ A generic script class with predefined behaviour.
        It can be customised to use/not use certain controls on instantiation.
    """

    def __init__(self, c_instance, macro_map_mode, volume_map_mode, device_controls, transport_controls, volume_controls, trackarm_controls, bank_controls, descriptions=None, mixer_options=None):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            global_channel = 0
            if descriptions:
                if list(descriptions.keys()).count(b'INPUTPORT') > 0:
                    self._suggested_input_port = descriptions[b'INPUTPORT']
                if list(descriptions.keys()).count(b'OUTPUTPORT') > 0:
                    self._suggested_output_port = descriptions[b'OUTPUTPORT']
                if list(descriptions.keys()).count(b'CHANNEL') > 0:
                    global_channel = descriptions[b'CHANNEL']
                    if not is_valid_midi_channel(global_channel):
                        global_channel = 0
                if list(descriptions.keys()).count(b'PAD_TRANSLATION') > 0:
                    self.set_pad_translations(descriptions[b'PAD_TRANSLATION'])
            self._init_mixer_component(volume_controls, trackarm_controls, mixer_options, global_channel, volume_map_mode)
            self._init_device_component(device_controls, bank_controls, global_channel, macro_map_mode)
            self._init_transport_component(transport_controls, global_channel)

    def handle_sysex(self, midi_bytes):
        pass

    def _init_mixer_component(self, volume_controls, trackarm_controls, mixer_options, global_channel, volume_map_mode):
        momentary_buttons = mixer_options is not None and b'NOTOGGLE' in mixer_options.keys()
        MixerButton = partial(ButtonElement, momentary_buttons, MIDI_CC_TYPE, global_channel)

        def make_mixer_encoder(cc, channel, name):
            if is_valid_midi_identifier(cc) and is_valid_midi_channel(channel):
                return EncoderElement(MIDI_CC_TYPE, channel, cc, volume_map_mode, name=name)
            else:
                return

        def make_mixer_button(control, name):
            return MixerButton(mixer_options[control], name=name)

        if volume_controls != None and trackarm_controls != None:
            num_strips = max(len(volume_controls), len(trackarm_controls))
            send_info = []
            mixer = SpecialMixerComponent(num_strips, name=b'Mixer')
            mixer.master_strip().name = b'Master_Channel_Strip'
            mixer.selected_strip().name = b'Selected_Channel_Strip'
            if mixer_options != None:
                if has_specification_for(b'MASTERVOLUME', mixer_options) and is_valid_midi_identifier(mixer_options[b'MASTERVOLUME']):
                    mixer.master_strip().layer = Layer(volume_control=make_mixer_encoder(mixer_options[b'MASTERVOLUME'], global_channel, b'Master_Volume_Control'))
                for send in xrange(mixer_options.get(b'NUMSENDS', 0)):
                    send_info.append(mixer_options[(b'SEND%d' % (send + 1))])

                layer_specs = {}
                if has_specification_for(b'NEXTBANK', mixer_options):
                    layer_specs[b'bank_up_button'] = make_mixer_button(b'NEXTBANK', b'Mixer_Next_Bank_Button')
                if has_specification_for(b'PREVBANK', mixer_options):
                    layer_specs[b'bank_down_button'] = make_mixer_button(b'PREVBANK', b'Mixer_Previous_Bank_Button')
                mixer.layer = Layer(**layer_specs)
            for track in xrange(num_strips):
                strip = mixer.channel_strip(track)
                strip.name = b'Channel_Strip_' + str(track)
                layer_specs = {}
                if 0 <= track < len(volume_controls):
                    channel = global_channel
                    cc = volume_controls[track]
                    if isinstance(volume_controls[track], (tuple, list)):
                        cc = volume_controls[track][0]
                        if is_valid_midi_channel(volume_controls[track][1]):
                            channel = volume_controls[track][1]
                    if is_valid_midi_identifier(cc) and is_valid_midi_channel(channel):
                        layer_specs[b'volume_control'] = make_mixer_encoder(cc, channel, str(track) + b'_Volume_Control')
                if 0 <= track < len(trackarm_controls) and is_valid_midi_identifier(trackarm_controls[track]):
                    layer_specs[b'arm_button'] = MixerButton(trackarm_controls[track], name=str(track) + b'_Arm_Button')
                send_controls_raw = []
                for index, send in enumerate(send_info):
                    if 0 <= track < len(send):
                        channel = global_channel
                        cc = send[track]
                        if isinstance(send[track], (tuple, list)):
                            cc = send[track][0]
                            if is_valid_midi_channel(send[track][1]):
                                channel = send[track][1]
                        if is_valid_midi_identifier(cc) and is_valid_midi_channel(channel):
                            send_controls_raw.append(make_mixer_encoder(cc, channel, name=b'%d_Send_%d_Control' % (track, index)))

                if len(send_controls_raw) > 0:
                    layer_specs[b'send_controls'] = ButtonMatrixElement(rows=[
                     send_controls_raw])
                strip.layer = Layer(**layer_specs)

        return

    def _init_device_component(self, device_controls, bank_controls, global_channel, macro_map_mode):
        is_momentary = True
        DeviceButton = partial(ButtonElement, is_momentary, MIDI_CC_TYPE)

        def make_bank_button(control, name, is_momentary=True):
            return DeviceButton(global_channel, bank_controls[control], name=name)

        if device_controls:
            device = DeviceComponent(device_selection_follows_track_selection=True, name=b'Device_Component')
            layer_specs = {}
            if bank_controls:
                if has_specification_for(b'NEXTBANK', bank_controls):
                    layer_specs[b'bank_next_button'] = make_bank_button(b'NEXTBANK', b'Device_Next_Bank_Button')
                if has_specification_for(b'PREVBANK', bank_controls):
                    layer_specs[b'bank_prev_button'] = make_bank_button(b'PREVBANK', b'Device_Previous_Bank_Button')
                if has_specification_for(b'TOGGLELOCK', bank_controls):
                    layer_specs[b'lock_button'] = make_bank_button(b'TOGGLELOCK', b'Device_Lock_Button')
                bank_buttons_raw = []
                for index in xrange(8):
                    key = b'BANK' + str(index + 1)
                    if key in bank_controls.keys():
                        control_info = bank_controls[key]
                        channel = global_channel
                        cc = control_info
                        if isinstance(control_info, (tuple, list)):
                            cc = control_info[0]
                            if is_valid_midi_channel(control_info[1]):
                                channel = control_info[1]
                        if is_valid_midi_identifier(cc) and is_valid_midi_channel(channel):
                            name = b'Device_Bank_' + str(index) + b'_Button'
                            bank_buttons_raw.append(DeviceButton(channel, cc, name=name))

                if len(bank_buttons_raw) > 0:
                    layer_specs[b'bank_buttons'] = ButtonMatrixElement(rows=[
                     bank_buttons_raw])
            parameter_encoders_raw = []
            for index, control_info in enumerate(device_controls):
                channel = global_channel
                cc = control_info
                if isinstance(control_info, (tuple, list)):
                    cc = control_info[0]
                    if is_valid_midi_channel(control_info[1]):
                        channel = control_info[1]
                if is_valid_midi_identifier(cc) and is_valid_midi_channel(channel):
                    name = b'Device_Parameter_%d_Control' % index
                    parameter_encoders_raw.append(EncoderElement(MIDI_CC_TYPE, channel, cc, macro_map_mode, name=name))

            if len(parameter_encoders_raw) > 0:
                layer_specs[b'parameter_controls'] = ButtonMatrixElement(rows=[
                 parameter_encoders_raw])
            device.layer = Layer(**layer_specs)
            self.set_device_component(device)

    def _init_transport_component(self, transport_controls, global_channel):

        def make_transport_button(control, name, is_momentary=True):
            return ButtonElement(is_momentary, MIDI_CC_TYPE, global_channel, transport_controls[control], name=name)

        if transport_controls:
            momentary_seek = b'NORELEASE' not in transport_controls.keys()
            layer_specs = {}
            if has_specification_for(b'STOP', transport_controls):
                layer_specs[b'stop_button'] = make_transport_button(b'STOP', b'Stop_Button')
            if has_specification_for(b'PLAY', transport_controls):
                layer_specs[b'play_button'] = make_transport_button(b'PLAY', b'Play_Button')
            if has_specification_for(b'REC', transport_controls):
                layer_specs[b'record_button'] = make_transport_button(b'REC', b'Record_Button')
            if has_specification_for(b'LOOP', transport_controls):
                layer_specs[b'loop_button'] = make_transport_button(b'LOOP', b'Loop_Button')
            if has_specification_for(b'FFWD', transport_controls):
                layer_specs[b'seek_forward_button'] = make_transport_button(b'FFWD', b'FFwd_Button', is_momentary=momentary_seek)
            if has_specification_for(b'RWD', transport_controls):
                layer_specs[b'seek_backward_button'] = make_transport_button(b'RWD', b'Rwd_Button', is_momentary=momentary_seek)
            transport = TransportComponent(name=b'Transport')
            transport.layer = Layer(**layer_specs)