# uncompyle6 version 3.3.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 15:29:51) [MSC v.1915 64 bit (AMD64)]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\ableton\v2\control_surface\default_bank_definitions.py
# Compiled at: 2019-05-10 18:21:20
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base.collection import IndexedDict
from ableton.v2.control_surface import BANK_MAIN_KEY, BANK_PARAMETERS_KEY, use
RACK_BANKS = IndexedDict((
 (
  b'Macros',
  {BANK_PARAMETERS_KEY: (
                         b'Macro 1', b'Macro 2', b'Macro 3', b'Macro 4',
                         b'Macro 5', b'Macro 6', b'Macro 7', b'Macro 8')}),))
BANK_DEFINITIONS = {b'AudioEffectGroupDevice': RACK_BANKS, 
   b'MidiEffectGroupDevice': RACK_BANKS, 
   b'InstrumentGroupDevice': RACK_BANKS, 
   b'DrumGroupDevice': RACK_BANKS, 
   b'UltraAnalog': IndexedDict((
                  (
                   BANK_MAIN_KEY,
                   {BANK_PARAMETERS_KEY: (
                                          use(b'OSC1 Shape').if_parameter(b'OSC1 On/Off').has_value(b'On').else_use(b'OSC2 Shape').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'OSC1 Octave').if_parameter(b'OSC1 On/Off').has_value(b'On').else_use(b'OSC2 Octave').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'OSC2 Shape').if_parameter(b'OSC1 On/Off').has_value(b'On').and_parameter(b'OSC2 On/Off').has_value(b'On').else_use(b'OSC1 Semi').if_parameter(b'OSC1 On/Off').has_value(b'On').else_use(b'OSC2 Semi').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'OSC2 Octave').if_parameter(b'OSC1 On/Off').has_value(b'On').and_parameter(b'OSC2 On/Off').has_value(b'On').else_use(b'OSC1 Detune').if_parameter(b'OSC1 On/Off').has_value(b'On').else_use(b'OSC2 Detune').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'F1 Type').if_parameter(b'F1 On/Off').has_value(b'On').else_use(b'F2 Type').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'F1 Freq').if_parameter(b'F1 On/Off').has_value(b'On').else_use(b'F2 Freq').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'F1 Resonance').if_parameter(b'F1 On/Off').has_value(b'On').else_use(b'F2 Resonance').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          b'Volume')}),
                  (
                   b'Osc. 1 Shape',
                   {BANK_PARAMETERS_KEY: (
                                          b'OSC1 On/Off',
                                          use(b'OSC1 Shape').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'OSC1 On/Off').has_value(b'Off').else_use(b'OSC1 PW').if_parameter(b'OSC1 Shape').has_value(b'Rect'),
                                          use(b'').if_parameter(b'OSC1 On/Off').has_value(b'Off').else_use(b'O1 PW < LFO').if_parameter(b'OSC1 Shape').has_value(b'Rect').else_use(b'').if_parameter(b'LFO1 On/Off').has_value(b'Off'),
                                          use(b'').if_parameter(b'OSC1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'OSC1 Shape').has_value(b'Noise').else_use(b'').if_parameter(b'OSC1 Shape').has_value(b'Sine').else_use(b'OSC1 Mode'),
                                          use(b'').if_parameter(b'OSC1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'OSC1 Shape').has_value(b'Noise').else_use(b'O1 Sub/Sync'),
                                          use(b'OSC1 Balance').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'OSC1 Level').if_parameter(b'OSC1 On/Off').has_value(b'On'))}),
                  (
                   b'Osc. 1 Pitch',
                   {BANK_PARAMETERS_KEY: (
                                          b'OSC1 On/Off',
                                          use(b'OSC1 Octave').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'OSC1 Semi').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'OSC1 Detune').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'PEG1 Amount').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'PEG1 Time').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'O1 Keytrack').if_parameter(b'OSC1 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'OSC1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'LFO1 On/Off').has_value(b'Off').else_use(b'OSC1 < LFO'))}),
                  (
                   b'Osc. 2 Shape',
                   {BANK_PARAMETERS_KEY: (
                                          b'OSC2 On/Off',
                                          use(b'OSC2 Shape').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'OSC2 On/Off').has_value(b'Off').else_use(b'OSC2 PW').if_parameter(b'OSC2 Shape').has_value(b'Rect'),
                                          use(b'').if_parameter(b'OSC2 On/Off').has_value(b'Off').else_use(b'O2 PW < LFO').if_parameter(b'OSC2 Shape').has_value(b'Rect').else_use(b'').if_parameter(b'LFO2 On/Off').has_value(b'Off'),
                                          use(b'').if_parameter(b'OSC2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'OSC2 Shape').has_value(b'Noise').else_use(b'').if_parameter(b'OSC2 Shape').has_value(b'Sine').else_use(b'OSC2 Mode'),
                                          use(b'').if_parameter(b'OSC2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'OSC2 Shape').has_value(b'Noise').else_use(b'O2 Sub/Sync'),
                                          use(b'OSC2 Balance').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'OSC2 Level').if_parameter(b'OSC2 On/Off').has_value(b'On'))}),
                  (
                   b'Osc. 2 Pitch',
                   {BANK_PARAMETERS_KEY: (
                                          b'OSC2 On/Off',
                                          use(b'OSC2 Octave').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'OSC2 Semi').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'OSC2 Detune').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'PEG2 Amount').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'PEG2 Time').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'O2 Keytrack').if_parameter(b'OSC2 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'OSC2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'LFO2 On/Off').has_value(b'Off').else_use(b'OSC2 < LFO'))}),
                  (
                   b'Filters',
                   {BANK_PARAMETERS_KEY: (
                                          b'F1 On/Off',
                                          use(b'F1 Type').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'F1 Freq').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'F1 Resonance').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          b'F2 On/Off',
                                          use(b'F2 Type').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'F2 Freq').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'F2 Resonance').if_parameter(b'F2 On/Off').has_value(b'On'))}),
                  (
                   b'Filt. 1 Env.',
                   {BANK_PARAMETERS_KEY: (
                                          b'F1 On/Off',
                                          use(b'FEG1 < Vel').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'FEG1 A < Vel').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'FEG1 Attack').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'FEG1 Decay').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'FEG1 Sustain').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'FEG1 S Time').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'FEG1 Rel').if_parameter(b'F1 On/Off').has_value(b'On'))}),
                  (
                   b'Filt. 2 Env.',
                   {BANK_PARAMETERS_KEY: (
                                          b'F2 On/Off',
                                          use(b'FEG2 < Vel').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'FEG2 A < Vel').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'FEG2 Attack').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'FEG2 Decay').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'FEG2 Sustain').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'FEG2 S Time').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'FEG2 Rel').if_parameter(b'F2 On/Off').has_value(b'On'))}),
                  (
                   b'Filt. Modulation',
                   {BANK_PARAMETERS_KEY: (
                                          b'F1 On/Off',
                                          use(b'F1 Freq < LFO').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'F1 Freq < Env').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          use(b'F1 Res < LFO').if_parameter(b'F1 On/Off').has_value(b'On'),
                                          b'F2 On/Off',
                                          use(b'F2 Freq < LFO').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'F2 Freq < Env').if_parameter(b'F2 On/Off').has_value(b'On'),
                                          use(b'F2 Res < LFO').if_parameter(b'F2 On/Off').has_value(b'On'))}),
                  (
                   b'Amp',
                   {BANK_PARAMETERS_KEY: (
                                          use(b'AMP1 Level').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AMP1 Pan').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AMP1 < LFO').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'LFO1 On/Off').has_value(b'Off').else_use(b'LFO1 Speed').if_parameter(b'LFO1 Sync').has_value(b'Hertz').else_use(b'LFO1 SncRate'),
                                          use(b'AMP2 Level').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AMP2 Pan').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AMP2 < LFO').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'LFO2 On/Off').has_value(b'Off').else_use(b'LFO2 Speed').if_parameter(b'LFO2 Sync').has_value(b'Hertz').else_use(b'LFO2 SncRate'))}),
                  (
                   b'Amp 1 Envelope',
                   {BANK_PARAMETERS_KEY: (
                                          b'AMP1 On/Off',
                                          use(b'AEG1 < Vel').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AEG1 A < Vel').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AEG1 Attack').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AEG1 Decay').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AEG1 Sustain').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AEG1 S Time').if_parameter(b'AMP1 On/Off').has_value(b'On'),
                                          use(b'AEG1 Rel').if_parameter(b'AMP1 On/Off').has_value(b'On'))}),
                  (
                   b'Amp 2 Envelope',
                   {BANK_PARAMETERS_KEY: (
                                          b'AMP2 On/Off',
                                          use(b'AEG2 < Vel').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AEG2 A < Vel').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AEG2 Attack').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AEG2 Decay').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AEG2 Sustain').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AEG2 S Time').if_parameter(b'AMP2 On/Off').has_value(b'On'),
                                          use(b'AEG2 Rel').if_parameter(b'AMP2 On/Off').has_value(b'On'))}),
                  (
                   b'Noise & Unison',
                   {BANK_PARAMETERS_KEY: (
                                          b'Noise On/Off',
                                          use(b'Noise Level').if_parameter(b'Noise On/Off').has_value(b'On'),
                                          use(b'Noise Color').if_parameter(b'Noise On/Off').has_value(b'On'),
                                          use(b'Noise Balance').if_parameter(b'Noise On/Off').has_value(b'On'),
                                          b'Unison On/Off',
                                          use(b'Unison Detune').if_parameter(b'Unison On/Off').has_value(b'On'),
                                          use(b'Unison Delay').if_parameter(b'Unison On/Off').has_value(b'On'),
                                          b'')}),
                  (
                   b'Performance',
                   {BANK_PARAMETERS_KEY: (
                                          b'Glide On/Off',
                                          use(b'Glide Time').if_parameter(b'Glide On/Off').has_value(b'On'),
                                          use(b'Glide Mode').if_parameter(b'Glide On/Off').has_value(b'On'),
                                          use(b'Glide Legato').if_parameter(b'Glide On/Off').has_value(b'On'),
                                          b'PB Range', b'Key Stretch', b'Key Error', b'Voices')}),
                  (
                   b'LFO 1',
                   {BANK_PARAMETERS_KEY: (
                                          b'LFO1 On/Off',
                                          use(b'LFO1 Sync').if_parameter(b'LFO1 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'LFO1 On/Off').has_value(b'Off').else_use(b'LFO1 Speed').if_parameter(b'LFO1 Sync').has_value(b'Hertz').else_use(b'LFO1 SncRate'),
                                          use(b'LFO1 Shape').if_parameter(b'LFO1 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'LFO1 On/Off').has_value(b'Off').else_use(b'LFO1 PW').if_parameter(b'LFO1 Shape').has_value(b'Rect').else_use(b'LFO1 PW').if_parameter(b'LFO1 Shape').has_value(b'Tri'),
                                          use(b'LFO1 Phase').if_parameter(b'LFO1 On/Off').has_value(b'On'),
                                          use(b'LFO1 Delay').if_parameter(b'LFO1 On/Off').has_value(b'On'),
                                          use(b'LFO1 Fade In').if_parameter(b'LFO1 On/Off').has_value(b'On'))}),
                  (
                   b'LFO 2',
                   {BANK_PARAMETERS_KEY: (
                                          b'LFO2 On/Off',
                                          use(b'LFO2 Sync').if_parameter(b'LFO2 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'LFO2 On/Off').has_value(b'Off').else_use(b'LFO2 Speed').if_parameter(b'LFO2 Sync').has_value(b'Hertz').else_use(b'LFO2 SncRate'),
                                          use(b'LFO2 Shape').if_parameter(b'LFO2 On/Off').has_value(b'On'),
                                          use(b'').if_parameter(b'LFO2 On/Off').has_value(b'Off').else_use(b'LFO2 PW').if_parameter(b'LFO2 Shape').has_value(b'Rect').else_use(b'LFO2 PW').if_parameter(b'LFO2 Shape').has_value(b'Tri'),
                                          use(b'LFO2 Phase').if_parameter(b'LFO2 On/Off').has_value(b'On'),
                                          use(b'LFO2 Delay').if_parameter(b'LFO2 On/Off').has_value(b'On'),
                                          use(b'LFO2 Fade In').if_parameter(b'LFO2 On/Off').has_value(b'On'))}),
                  (
                   b'Vibrato',
                   {BANK_PARAMETERS_KEY: (
                                          b'Vib On/Off',
                                          use(b'Vib Amount').if_parameter(b'Vib On/Off').has_value(b'On'),
                                          use(b'Vib Speed').if_parameter(b'Vib On/Off').has_value(b'On'),
                                          use(b'Vib Delay').if_parameter(b'Vib On/Off').has_value(b'On'),
                                          use(b'Vib Fade-In').if_parameter(b'Vib On/Off').has_value(b'On'),
                                          use(b'Vib Error').if_parameter(b'Vib On/Off').has_value(b'On'),
                                          use(b'Vib < ModWh').if_parameter(b'Vib On/Off').has_value(b'On'),
                                          b'')}))), 
   b'ChannelEq': IndexedDict((
                (
                 BANK_MAIN_KEY,
                 {BANK_PARAMETERS_KEY: (
                                        b'Highpass On', use(b'Low Gain').with_name(b'Low'),
                                        use(b'Mid Gain').with_name(b'Mid'), b'Mid Freq',
                                        use(b'High Gain').with_name(b'High'),
                                        use(b'Gain').with_name(b'Output'), b'', b'')}),)), 
   b'Collision': IndexedDict((
                (
                 BANK_MAIN_KEY,
                 {BANK_PARAMETERS_KEY: (
                                        use(b'Res 1 Type').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Brightness'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'Res 1 Opening').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Inharmonics'),
                                        use(b'Res 1 Decay').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'Res 1 Radius').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'Res 1 Radius').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Material'),
                                        use(b'Mallet Stiffness').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Noise Amount').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        b'Volume')}),
                (
                 b'Mix',
                 {BANK_PARAMETERS_KEY: (
                                        use(b'Res 1 Volume').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'Panorama').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'Res 1 Bleed').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'Res 2 Volume').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'Res 2 Panorama').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'Res 2 Bleed').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        b'Structure', b'Volume')}),
                (
                 b'Mallet',
                 {BANK_PARAMETERS_KEY: (
                                        b'Mallet On/Off',
                                        use(b'Mallet Volume').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Noise Amount').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Stiffness').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Noise Color').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Modulation').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Volume < Vel').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Noise Amount < Vel').if_parameter(b'Mallet On/Off').has_value(b'On'))}),
                (
                 b'Noise Envelope',
                 {BANK_PARAMETERS_KEY: (
                                        b'Noise On/Off',
                                        use(b'Noise Volume').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Volume < Key').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Volume < Vel').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Attack').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Sustain').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Decay').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Release').if_parameter(b'Noise On/Off').has_value(b'On'))}),
                (
                 b'Noise Filter',
                 {BANK_PARAMETERS_KEY: (
                                        b'Noise On/Off',
                                        use(b'Noise Volume').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Filter Type').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Filter Freq').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Filter Q').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Freq < Key').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Freq < Vel').if_parameter(b'Noise On/Off').has_value(b'On'),
                                        use(b'Noise Freq < Env').if_parameter(b'Noise On/Off').has_value(b'On'))}),
                (
                 b'Res. 1 Body',
                 {BANK_PARAMETERS_KEY: (
                                        b'Res 1 On/Off',
                                        use(b'Res 1 Type').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'Res 1 Ratio').if_parameter(b'Res 1 Type').has_value(b'Plate').else_use(b'Res 1 Ratio').if_parameter(b'Res 1 Type').has_value(b'Membrane'),
                                        use(b'Res 1 Decay').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'Res 1 Radius').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'Res 1 Radius').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Material'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Listening L'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Listening R'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Hit'))}),
                (
                 b'Res. 1 Tune',
                 {BANK_PARAMETERS_KEY: (
                                        b'Res 1 On/Off',
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Brightness'),
                                        use(b'Res 1 Quality').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 1 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 1 Type').has_value(b'Tube').else_use(b'Res 1 Opening').if_parameter(b'Res 1 Type').has_value(b'Pipe').else_use(b'Res 1 Inharmonics'),
                                        use(b'Res 1 Tune').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'Res 1 Fine Tune').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'Res 1 Pitch Env.').if_parameter(b'Res 1 On/Off').has_value(b'On'),
                                        use(b'Res 1 Pitch Env. Time').if_parameter(b'Res 1 On/Off').has_value(b'On'))}),
                (
                 b'Res. 2 Body',
                 {BANK_PARAMETERS_KEY: (
                                        b'Res 2 On/Off',
                                        use(b'Res 2 Type').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'Res 2 Ratio').if_parameter(b'Res 2 Type').has_value(b'Plate').else_use(b'Res 2 Ratio').if_parameter(b'Res 2 Type').has_value(b'Membrane'),
                                        use(b'Res 2 Decay').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'Res 2 Radius').if_parameter(b'Res 2 Type').has_value(b'Tube').else_use(b'Res 2 Radius').if_parameter(b'Res 2 Type').has_value(b'Pipe').else_use(b'Res 2 Material'),
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Pipe').else_use(b'Res 2 Listening L'),
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Pipe').else_use(b'Res 2 Listening R'),
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Pipe').else_use(b'Res 2 Hit'))}),
                (
                 b'Res. 2 Tune',
                 {BANK_PARAMETERS_KEY: (
                                        b'Res 2 On/Off',
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Tube').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Pipe').else_use(b'Res 2 Brightness'),
                                        use(b'Res 2 Quality').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'Res 2 On/Off').has_value(b'Off').else_use(b'').if_parameter(b'Res 2 Type').has_value(b'Tube').else_use(b'Res 2 Opening').if_parameter(b'Res 2 Type').has_value(b'Pipe').else_use(b'Res 2 Inharmonics'),
                                        use(b'Res 2 Tune').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'Res 2 Fine Tune').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'Res 2 Pitch Env.').if_parameter(b'Res 2 On/Off').has_value(b'On'),
                                        use(b'Res 2 Pitch Env. Time').if_parameter(b'Res 2 On/Off').has_value(b'On'))}),
                (
                 b'LFO 1',
                 {BANK_PARAMETERS_KEY: (
                                        b'LFO 1 On/Off',
                                        use(b'LFO 1 Depth').if_parameter(b'LFO 1 On/Off').has_value(b'On'),
                                        use(b'LFO 1 Shape').if_parameter(b'LFO 1 On/Off').has_value(b'On'),
                                        use(b'LFO 1 Sync').if_parameter(b'LFO 1 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'LFO 1 On/Off').has_value(b'Off').else_use(b'LFO 1 Sync Rate').if_parameter(b'LFO 1 Sync').has_value(b'Sync').else_use(b'LFO 1 Rate'),
                                        use(b'LFO 1 Offset').if_parameter(b'LFO 1 On/Off').has_value(b'On'),
                                        use(b'LFO 1 Destination A').if_parameter(b'LFO 1 On/Off').has_value(b'On'),
                                        use(b'LFO 1 Destination A Amount').if_parameter(b'LFO 1 On/Off').has_value(b'On'))}),
                (
                 b'LFO 2',
                 {BANK_PARAMETERS_KEY: (
                                        b'LFO 2 On/Off',
                                        use(b'LFO 2 Depth').if_parameter(b'LFO 2 On/Off').has_value(b'On'),
                                        use(b'LFO 2 Shape').if_parameter(b'LFO 2 On/Off').has_value(b'On'),
                                        use(b'LFO 2 Sync').if_parameter(b'LFO 2 On/Off').has_value(b'On'),
                                        use(b'').if_parameter(b'LFO 2 On/Off').has_value(b'Off').else_use(b'LFO 2 Sync Rate').if_parameter(b'LFO 2 Sync').has_value(b'Sync').else_use(b'LFO 2 Rate'),
                                        use(b'LFO 2 Offset').if_parameter(b'LFO 2 On/Off').has_value(b'On'),
                                        use(b'LFO 2 Destination A').if_parameter(b'LFO 2 On/Off').has_value(b'On'),
                                        use(b'LFO 2 Destination A Amount').if_parameter(b'LFO 2 On/Off').has_value(b'On'))}),
                (
                 b'Mallet Mod.',
                 {BANK_PARAMETERS_KEY: (
                                        b'Mallet On/Off',
                                        use(b'Mallet Volume < Key').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Volume < Vel').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Noise Amount < Key').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Noise Amount < Vel').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Stiffness < Key').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        use(b'Mallet Stiffness < Vel').if_parameter(b'Mallet On/Off').has_value(b'On'),
                                        b'')}))), 
   b'LoungeLizard': IndexedDict((
                   (
                    BANK_MAIN_KEY,
                    {BANK_PARAMETERS_KEY: (
                                           b'M Stiffness', b'M Force', b'Noise Amount', b'F Tine Vol',
                                           b'F Tone Vol', b'F Release', b'P Symmetry', b'Volume')}),
                   (
                    b'Mallet',
                    {BANK_PARAMETERS_KEY: (
                                           b'M Stiffness', b'M Force', b'Noise Pitch', b'Noise Decay',
                                           b'Noise Amount', b'M Stiff < Vel', b'M Force < Vel', b'Volume')}),
                   (
                    b'Fork',
                    {BANK_PARAMETERS_KEY: (
                                           b'F Tine Color', b'F Tine Decay', b'F Tine Vol', b'F Tone Vol',
                                           b'F Tone Decay', b'F Release', b'F Tine < Key', b'Volume')}),
                   (
                    b'Damper',
                    {BANK_PARAMETERS_KEY: (
                                           b'Damp Tone', b'Damp Balance', b'Damp Amount', b'', b'', b'', b'', b'Volume')}),
                   (
                    b'Pickup',
                    {BANK_PARAMETERS_KEY: (
                                           b'P Symmetry', b'P Distance', b'P Amp In', b'P Amp Out',
                                           b'Pickup Model', b'P Amp < Key', b'', b'Volume')}),
                   (
                    b'Modulation',
                    {BANK_PARAMETERS_KEY: (
                                           b'M Stiff < Vel', b'M Stiff < Key', b'M Force < Vel', b'M Force < Key',
                                           b'Noise < Key', b'F Tine < Key', b'P Amp < Key', b'Volume')}),
                   (
                    b'Global',
                    {BANK_PARAMETERS_KEY: (
                                           b'KB Stretch', b'PB Range', b'', b'', b'Voices', b'Semitone', b'Detune', b'Volume')}))), 
   b'InstrumentImpulse': IndexedDict((
                        (
                         BANK_MAIN_KEY,
                         {BANK_PARAMETERS_KEY: (
                                                b'1 Transpose', b'1 Volume', b'3 Transpose', b'3 Volume',
                                                b'7 Transpose', b'7 Volume', b'8 Transpose', b'8 Volume')}),
                        (
                         b'Pad 1',
                         {BANK_PARAMETERS_KEY: (
                                                b'1 Start', b'1 Envelope Decay', b'1 Stretch Factor', b'1 Saturator Drive',
                                                b'1 Envelope Type', b'1 Transpose', b'1 Volume <- Vel', b'1 Volume')}),
                        (
                         b'1 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'1 Filter Freq', b'1 Filter Res', b'1 Filter Type', b'1 Filter <- Vel',
                                                b'1 Filter <- Random', b'1 Pan', b'1 Pan <- Vel', b'1 Pan <- Random')}),
                        (
                         b'Pad 2',
                         {BANK_PARAMETERS_KEY: (
                                                b'2 Start', b'2 Envelope Decay', b'2 Stretch Factor', b'2 Saturator Drive',
                                                b'2 Envelope Type', b'2 Transpose', b'2 Volume <- Vel', b'2 Volume')}),
                        (
                         b'2 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'2 Filter Freq', b'2 Filter Res', b'2 Filter Type', b'2 Filter <- Vel',
                                                b'2 Filter <- Random', b'2 Pan', b'2 Pan <- Vel', b'2 Pan <- Random')}),
                        (
                         b'Pad 3',
                         {BANK_PARAMETERS_KEY: (
                                                b'3 Start', b'3 Envelope Decay', b'3 Stretch Factor', b'3 Saturator Drive',
                                                b'3 Envelope Type', b'3 Transpose', b'3 Volume <- Vel', b'3 Volume')}),
                        (
                         b'3 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'3 Filter Freq', b'3 Filter Res', b'3 Filter Type', b'3 Filter <- Vel',
                                                b'3 Filter <- Random', b'3 Pan', b'3 Pan <- Vel', b'3 Pan <- Random')}),
                        (
                         b'Pad 4',
                         {BANK_PARAMETERS_KEY: (
                                                b'4 Start', b'4 Envelope Decay', b'4 Stretch Factor', b'4 Saturator Drive',
                                                b'4 Envelope Type', b'4 Transpose', b'4 Volume <- Vel', b'4 Volume')}),
                        (
                         b'4 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'4 Filter Freq', b'4 Filter Res', b'4 Filter Type', b'4 Filter <- Vel',
                                                b'4 Filter <- Random', b'4 Pan', b'4 Pan <- Vel', b'4 Pan <- Random')}),
                        (
                         b'Pad 5',
                         {BANK_PARAMETERS_KEY: (
                                                b'5 Start', b'5 Envelope Decay', b'5 Stretch Factor', b'5 Saturator Drive',
                                                b'5 Envelope Type', b'5 Transpose', b'5 Volume <- Vel', b'5 Volume')}),
                        (
                         b'5 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'5 Filter Freq', b'5 Filter Res', b'5 Filter Type', b'5 Filter <- Vel',
                                                b'5 Filter <- Random', b'5 Pan', b'5 Pan <- Vel', b'5 Pan <- Random')}),
                        (
                         b'Pad 6',
                         {BANK_PARAMETERS_KEY: (
                                                b'6 Start', b'6 Envelope Decay', b'6 Stretch Factor', b'6 Saturator Drive',
                                                b'6 Envelope Type', b'6 Transpose', b'6 Volume <- Vel', b'6 Volume')}),
                        (
                         b'6 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'6 Filter Freq', b'6 Filter Res', b'6 Filter Type', b'6 Filter <- Vel',
                                                b'6 Filter <- Random', b'6 Pan', b'6 Pan <- Vel', b'6 Pan <- Random')}),
                        (
                         b'Pad 7',
                         {BANK_PARAMETERS_KEY: (
                                                b'7 Start', b'7 Envelope Decay', b'7 Stretch Factor', b'7 Saturator Drive',
                                                b'7 Envelope Type', b'7 Transpose', b'7 Volume <- Vel', b'7 Volume')}),
                        (
                         b'7 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'7 Filter Freq', b'7 Filter Res', b'7 Filter Type', b'7 Filter <- Vel',
                                                b'7 Filter <- Random', b'7 Pan', b'7 Pan <- Vel', b'7 Pan <- Random')}),
                        (
                         b'Pad 8',
                         {BANK_PARAMETERS_KEY: (
                                                b'8 Start', b'8 Envelope Decay', b'8 Stretch Factor', b'8 Saturator Drive',
                                                b'8 Envelope Type', b'8 Transpose', b'8 Volume <- Vel', b'8 Volume')}),
                        (
                         b'8 Filt/Mod/Pan',
                         {BANK_PARAMETERS_KEY: (
                                                b'8 Filter Freq', b'8 Filter Res', b'8 Filter Type', b'8 Filter <- Vel',
                                                b'8 Filter <- Random', b'8 Pan', b'8 Pan <- Vel', b'8 Pan <- Random')}),
                        (
                         b'Global',
                         {BANK_PARAMETERS_KEY: (
                                                b'Global Time', b'Global Transpose', b'Global Volume', b'', b'', b'', b'', b'')}))), 
   b'Operator': IndexedDict((
               (
                BANK_MAIN_KEY,
                {BANK_PARAMETERS_KEY: (
                                       use(b'Algorithm').if_parameter(b'Filter On').has_value(b'Off').else_use(b'Filter Freq'),
                                       use(b'Filter Res (Legacy)').if_parameter(b'Filter Res').is_available(False).and_parameter(b'Filter On').has_value(b'On').else_use(b'Filter Res').if_parameter(b'Filter On').has_value(b'On').else_use(b'Tone'),
                                       use(b'').if_parameter(b'Osc-A On').has_value(b'Off').else_use(b'A Coarse').if_parameter(b'A Fix On ').has_value(b'Off').else_use(b'A Fix Freq'),
                                       use(b'').if_parameter(b'Osc-A On').has_value(b'Off').else_use(b'A Fine').if_parameter(b'A Fix On ').has_value(b'Off').else_use(b'A Fix Freq Mul'),
                                       use(b'').if_parameter(b'Osc-B On').has_value(b'Off').else_use(b'B Coarse').if_parameter(b'B Fix On ').has_value(b'Off').else_use(b'B Fix Freq'),
                                       use(b'').if_parameter(b'Osc-B On').has_value(b'Off').else_use(b'B Fine').if_parameter(b'B Fix On ').has_value(b'Off').else_use(b'B Fix Freq Mul'),
                                       use(b'Osc-B Level').if_parameter(b'Osc-B On').has_value(b'On'),
                                       b'Volume')}),
               (
                b'Global',
                {BANK_PARAMETERS_KEY: (
                                       b'Time', b'Time < Key', b'Tone', b'Algorithm',
                                       b'Panorama', b'Pan < Key', b'Pan < Rnd', b'Volume')}),
               (
                b'Osc. A',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-A On',
                                       use(b'Osc-A Level').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'A Fix On ').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-A On').has_value(b'Off').else_use(b'A Coarse').if_parameter(b'A Fix On ').has_value(b'Off').else_use(b'A Fix Freq'),
                                       use(b'').if_parameter(b'Osc-A On').has_value(b'Off').else_use(b'A Fine').if_parameter(b'A Fix On ').has_value(b'Off').else_use(b'A Fix Freq Mul'),
                                       use(b'Osc-A Wave').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Osc-A Retrig').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-A On').has_value(b'Off').else_use(b'Osc-A Phase').if_parameter(b'Osc-A Retrig').has_value(b'On'))}),
               (
                b'Osc. A Env.',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-A On',
                                       use(b'Ae Init').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Ae Attack').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Ae Peak').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Ae Decay').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Ae Sustain').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Ae Release').if_parameter(b'Osc-A On').has_value(b'On'),
                                       use(b'Osc-A Lev < Vel').if_parameter(b'Osc-A On').has_value(b'On'))}),
               (
                b'Osc. B',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-B On',
                                       use(b'Osc-B Level').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'B Fix On ').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-B On').has_value(b'Off').else_use(b'B Coarse').if_parameter(b'B Fix On ').has_value(b'Off').else_use(b'B Fix Freq'),
                                       use(b'').if_parameter(b'Osc-B On').has_value(b'Off').else_use(b'B Fine').if_parameter(b'B Fix On ').has_value(b'Off').else_use(b'B Fix Freq Mul'),
                                       use(b'Osc-B Wave').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Osc-B Retrig').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-B On').has_value(b'Off').else_use(b'Osc-B Phase').if_parameter(b'Osc-B Retrig').has_value(b'On'))}),
               (
                b'Osc. B Env.',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-B On',
                                       use(b'Be Init').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Be Attack').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Be Peak').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Be Decay').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Be Sustain').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Be Release').if_parameter(b'Osc-B On').has_value(b'On'),
                                       use(b'Osc-B Lev < Vel').if_parameter(b'Osc-B On').has_value(b'On'))}),
               (
                b'Osc. C',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-C On',
                                       use(b'Osc-C Level').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'C Fix On ').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-C On').has_value(b'Off').else_use(b'C Coarse').if_parameter(b'C Fix On ').has_value(b'Off').else_use(b'C Fix Freq'),
                                       use(b'').if_parameter(b'Osc-C On').has_value(b'Off').else_use(b'C Fine').if_parameter(b'C Fix On ').has_value(b'Off').else_use(b'C Fix Freq Mul'),
                                       use(b'Osc-C Wave').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Osc-C Retrig').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-C On').has_value(b'Off').else_use(b'Osc-C Phase').if_parameter(b'Osc-C Retrig').has_value(b'On'))}),
               (
                b'Osc. C Env.',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-C On',
                                       use(b'Ce Init').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Ce Attack').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Ce Peak').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Ce Decay').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Ce Sustain').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Ce Release').if_parameter(b'Osc-C On').has_value(b'On'),
                                       use(b'Osc-C Lev < Vel').if_parameter(b'Osc-C On').has_value(b'On'))}),
               (
                b'Osc. D',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-D On',
                                       use(b'Osc-D Level').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'D Fix On ').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-D On').has_value(b'Off').else_use(b'D Coarse').if_parameter(b'D Fix On ').has_value(b'Off').else_use(b'D Fix Freq'),
                                       use(b'').if_parameter(b'Osc-D On').has_value(b'Off').else_use(b'D Fine').if_parameter(b'D Fix On ').has_value(b'Off').else_use(b'D Fix Freq Mul'),
                                       use(b'Osc-D Wave').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'Osc-D Retrig').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'').if_parameter(b'Osc-D On').has_value(b'Off').else_use(b'Osc-D Phase').if_parameter(b'Osc-D Retrig').has_value(b'On'))}),
               (
                b'Osc. D Env.',
                {BANK_PARAMETERS_KEY: (
                                       b'Osc-D On',
                                       use(b'De Init').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'De Attack').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'De Peak').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'De Decay').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'De Sustain').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'De Release').if_parameter(b'Osc-D On').has_value(b'On'),
                                       use(b'Osc-D Lev < Vel').if_parameter(b'Osc-D On').has_value(b'On'))}),
               (
                b'Filter',
                {BANK_PARAMETERS_KEY: (
                                       b'Filter On',
                                       use(b'').if_parameter(b'Filter On').has_value(b'Off').else_use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).else_use(b'Filter Type (Legacy)'),
                                       use(b'Filter Freq').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'').if_parameter(b'Filter On').has_value(b'Off').else_use(b'Filter Res').if_parameter(b'Filter Res').is_available(True).else_use(b'Filter Res (Legacy)'),
                                       use(b'').if_parameter(b'Filter On').has_value(b'Off').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Lowpass').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Highpass').else_use(b'Filter Circuit - BP/NO/Morph'),
                                       use(b'').if_parameter(b'Filter On').has_value(b'Off').else_use(b'Filter Morph').if_parameter(b'Filter Type').has_value(b'Morph').else_use(b'').if_parameter(b'Filter Type').has_value(b'Lowpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Highpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Bandpass').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Notch').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'Filter Drive'),
                                       use(b'Filter Slope').if_parameter(b'Filter On').has_value(b'On').and_parameter(b'Filter Slope').is_available(True),
                                       use(b'Filt < Vel').if_parameter(b'Filter On').has_value(b'On'))}),
               (
                b'Filt. Env.',
                {BANK_PARAMETERS_KEY: (
                                       use(b'Fe Amount').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe Init').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe Attack').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe Peak').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe Decay').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe Sustain').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe Release').if_parameter(b'Filter On').has_value(b'On'),
                                       use(b'Fe End').if_parameter(b'Filter On').has_value(b'On'))}),
               (
                b'LFO',
                {BANK_PARAMETERS_KEY: (
                                       b'LFO On',
                                       use(b'LFO Type').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'LFO Range').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'').if_parameter(b'LFO On').has_value(b'Off').else_use(b'LFO Sync').if_parameter(b'LFO Range').has_value(b'Sync').else_use(b'LFO Rate'),
                                       use(b'LFO Retrigger').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'LFO Amt').if_parameter(b'LFO On').has_value(b'On'),
                                       b'', b'')}),
               (
                b'LFO Env.',
                {BANK_PARAMETERS_KEY: (
                                       b'LFO On',
                                       use(b'Le Init').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'Le Attack').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'Le Peak').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'Le Decay').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'Le Sustain').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'Le Release').if_parameter(b'LFO On').has_value(b'On'),
                                       use(b'Le End').if_parameter(b'LFO On').has_value(b'On'))}),
               (
                b'Pitch',
                {BANK_PARAMETERS_KEY: (
                                       b'Transpose', b'Spread', b'Glide On',
                                       use(b'Glide Time').if_parameter(b'Glide On').has_value(b'On'),
                                       b'Pe On',
                                       use(b'Pe Amount').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'LFO < Pe').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe Dst B').if_parameter(b'Pe On').has_value(b'On'))}),
               (
                b'Pitch Env.',
                {BANK_PARAMETERS_KEY: (
                                       b'Pe On',
                                       use(b'Pe Attack').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe Peak').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe Decay').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe Sustain').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe Release').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe End').if_parameter(b'Pe On').has_value(b'On'),
                                       use(b'Pe R < Vel').if_parameter(b'Pe On').has_value(b'On'))}))), 
   b'MultiSampler': IndexedDict((
                   (
                    BANK_MAIN_KEY,
                    {BANK_PARAMETERS_KEY: (
                                           b'Ve Attack', b'Ve Decay', b'Ve Sustain', b'Ve Release',
                                           use(b'Pan').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).else_use(b'Filter Type (Legacy)'),
                                           use(b'Transpose').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Freq'),
                                           use(b'Detune').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Res').if_parameter(b'Filter Res').is_available(True).else_use(b'Filter Res (Legacy)'),
                                           b'Volume')}),
                   (
                    b'Volume Env.',
                    {BANK_PARAMETERS_KEY: (
                                           b'Ve Init', b'Ve Attack', b'Ve Peak', b'Ve Decay',
                                           b'Ve Sustain', b'Ve Release', b'Vol < Vel', b'Volume')}),
                   (
                    b'Env. Loop & Pan',
                    {BANK_PARAMETERS_KEY: (
                                           b'Ve Mode',
                                           use(b'Ve Loop').if_parameter(b'Ve Mode').has_value(b'Loop').else_use(b'Ve Retrig').if_parameter(b'Ve Mode').has_value(b'Beat').else_use(b'Ve Retrig').if_parameter(b'Ve Mode').has_value(b'Sync').else_use(b''),
                                           b'Ve R < Vel', b'', b'Pan', b'Pan < Rnd', b'Time', b'Time < Key')}),
                   (
                    b'Filter',
                    {BANK_PARAMETERS_KEY: (
                                           b'F On',
                                           use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).else_use(b'Filter Type (Legacy)'),
                                           use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Freq'),
                                           use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Res').if_parameter(b'Filter Res').is_available(True).else_use(b'Filter Res (Legacy)'),
                                           use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Lowpass').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Highpass').else_use(b'Filter Circuit - BP/NO/Morph'),
                                           use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Morph').if_parameter(b'Filter Type').has_value(b'Morph').else_use(b'').if_parameter(b'Filter Type').has_value(b'Lowpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Highpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Bandpass').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Notch').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'Filter Drive'),
                                           use(b'Filter Slope').if_parameter(b'F On').has_value(b'On').and_parameter(b'Filter Slope').is_available(True),
                                           use(b'Filt < Vel').if_parameter(b'F On').has_value(b'On'))}),
                   (
                    b'Filt. Env',
                    {BANK_PARAMETERS_KEY: (
                                           b'Fe On',
                                           use(b'Fe < Env').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Init').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Attack').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Decay').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Peak').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Sustain').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Release').if_parameter(b'Fe On').has_value(b'On'))}),
                   (
                    b'Shaper',
                    {BANK_PARAMETERS_KEY: (
                                           b'Fe On',
                                           use(b'Fe End').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'Fe Mode').if_parameter(b'Fe On').has_value(b'On'),
                                           use(b'').if_parameter(b'Fe On').has_value(b'Off').else_use(b'Fe Loop').if_parameter(b'Fe Mode').has_value(b'Loop').else_use(b'Fe Retrig').if_parameter(b'Fe Mode').has_value(b'Beat').else_use(b'Fe Retrig').if_parameter(b'Fe Mode').has_value(b'Sync').else_use(b''),
                                           use(b'Fe R < Vel').if_parameter(b'Fe On').has_value(b'On'),
                                           b'Shaper On',
                                           use(b'Shaper Type').if_parameter(b'Shaper On').has_value(b'On'),
                                           use(b'Shaper Amt').if_parameter(b'Shaper On').has_value(b'On'))}),
                   (
                    b'Osc. pg. 1',
                    {BANK_PARAMETERS_KEY: (
                                           b'Osc On',
                                           use(b'O Mode').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Init').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Attack').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Peak').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Decay').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Sustain').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Release').if_parameter(b'Osc On').has_value(b'On'))}),
                   (
                    b'Osc. pg. 2',
                    {BANK_PARAMETERS_KEY: (
                                           use(b'Oe End').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'Oe Mode').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'').if_parameter(b'Osc On').has_value(b'Off').else_use(b'Oe Loop').if_parameter(b'Oe Mode').has_value(b'Loop').else_use(b'Oe Retrig').if_parameter(b'Oe Mode').has_value(b'Beat').else_use(b'Oe Retrig').if_parameter(b'Oe Mode').has_value(b'Sync').else_use(b''),
                                           use(b'O Type').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'O Volume').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'O Fix On').if_parameter(b'Osc On').has_value(b'On'),
                                           use(b'').if_parameter(b'Osc On').has_value(b'Off').else_use(b'O Coarse').if_parameter(b'O Fix On').has_value(b'Off').else_use(b'O Fix Freq'),
                                           use(b'').if_parameter(b'Osc On').has_value(b'Off').else_use(b'O Fine').if_parameter(b'O Fix On').has_value(b'Off').else_use(b'O Fix Freq Mul'))}),
                   (
                    b'Pitch Env.',
                    {BANK_PARAMETERS_KEY: (
                                           b'Pe On',
                                           use(b'Pe < Env').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Init').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Attack').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Peak').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Decay').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Sustain').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Release').if_parameter(b'Pe On').has_value(b'On'))}),
                   (
                    b'Pitch Env. 2',
                    {BANK_PARAMETERS_KEY: (
                                           b'Pe On',
                                           use(b'Pe End').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe R < Vel').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'Pe Mode').if_parameter(b'Pe On').has_value(b'On'),
                                           use(b'').if_parameter(b'Pe On').has_value(b'Off').else_use(b'Pe Loop').if_parameter(b'Pe Mode').has_value(b'Loop').else_use(b'Pe Retrig').if_parameter(b'Pe Mode').has_value(b'Beat').else_use(b'Pe Retrig').if_parameter(b'Pe Mode').has_value(b'Sync').else_use(b''),
                                           b'', b'', b'')}),
                   (
                    b'Pitch/Glide',
                    {BANK_PARAMETERS_KEY: (
                                           b'Pe On', b'Spread', b'Transpose', b'Detune', b'Key Zone Shift', b'Glide Mode',
                                           use(b'Glide Time').if_parameter(b'Glide Mode').has_value(b'On'),
                                           b'')}),
                   (
                    b'LFO1 pg. 1',
                    {BANK_PARAMETERS_KEY: (
                                           b'L 1 On',
                                           use(b'L 1 Wave').if_parameter(b'L 1 On').has_value(b'On'),
                                           use(b'L 1 Sync').if_parameter(b'L 1 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 1 On').has_value(b'Off').else_use(b'L 1 Sync Rate').if_parameter(b'L 1 Sync').has_value(b'Sync').else_use(b'L 1 Rate'),
                                           use(b'Vol < LFO').if_parameter(b'L 1 On').has_value(b'On'),
                                           use(b'Filt < LFO').if_parameter(b'L 1 On').has_value(b'On'),
                                           use(b'Pan < LFO').if_parameter(b'L 1 On').has_value(b'On'),
                                           use(b'Pitch < LFO').if_parameter(b'L 1 On').has_value(b'On'))}),
                   (
                    b'LFO1 pg. 2',
                    {BANK_PARAMETERS_KEY: (
                                           b'L 1 On',
                                           use(b'L 1 Retrig').if_parameter(b'L 1 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 1 On').has_value(b'Off').else_use(b'L 1 Offset').if_parameter(b'L 1 Retrig').has_value(b'On').else_use(b''),
                                           use(b'L 1 Attack').if_parameter(b'L 1 On').has_value(b'On'),
                                           b'', b'', b'', b'')}),
                   (
                    b'LFO2 pg. 1',
                    {BANK_PARAMETERS_KEY: (
                                           b'L 2 On',
                                           use(b'L 2 Wave').if_parameter(b'L 2 On').has_value(b'On'),
                                           use(b'L 2 Sync').if_parameter(b'L 2 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 2 On').has_value(b'Off').else_use(b'L 2 Sync Rate').if_parameter(b'L 2 Sync').has_value(b'Sync').else_use(b'L 2 Rate'),
                                           use(b'L 2 Retrig').if_parameter(b'L 2 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 2 On').has_value(b'Off').else_use(b'L 2 Offset').if_parameter(b'L 2 Retrig').has_value(b'On').else_use(b''),
                                           use(b'L 2 Attack').if_parameter(b'L 2 On').has_value(b'On'),
                                           b'')}),
                   (
                    b'LFO2 pg. 2',
                    {BANK_PARAMETERS_KEY: (
                                           b'L 2 On',
                                           use(b'L 2 St Mode').if_parameter(b'L 2 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 2 On').has_value(b'Off').else_use(b'L 2 Spin').if_parameter(b'L 2 St Mode').has_value(b'Spin').else_use(b'L 2 Phase'),
                                           b'', b'', b'', b'', b'')}),
                   (
                    b'LFO3 pg. 1',
                    {BANK_PARAMETERS_KEY: (
                                           b'L 3 On',
                                           use(b'L 3 Wave').if_parameter(b'L 3 On').has_value(b'On'),
                                           use(b'L 3 Sync').if_parameter(b'L 3 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 3 On').has_value(b'Off').else_use(b'L 3 Sync Rate').if_parameter(b'L 3 Sync').has_value(b'Sync').else_use(b'L 3 Rate'),
                                           use(b'L 3 Retrig').if_parameter(b'L 3 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 3 On').has_value(b'Off').else_use(b'L 3 Offset').if_parameter(b'L 3 Retrig').has_value(b'On').else_use(b''),
                                           use(b'L 3 Attack').if_parameter(b'L 3 On').has_value(b'On'),
                                           b'')}),
                   (
                    b'LFO3 pg. 2',
                    {BANK_PARAMETERS_KEY: (
                                           b'L 3 On',
                                           use(b'L 3 St Mode').if_parameter(b'L 3 On').has_value(b'On'),
                                           use(b'').if_parameter(b'L 3 On').has_value(b'Off').else_use(b'L 3 Spin').if_parameter(b'L 3 St Mode').has_value(b'Spin').else_use(b'L 3 Phase'),
                                           b'', b'', b'', b'', b'')}),
                   (
                    b'Aux Env.',
                    {BANK_PARAMETERS_KEY: (
                                           b'Ae On',
                                           use(b'Ae < Env').if_parameter(b'Ae On').has_value(b'On'),
                                           use(b'Ae Init').if_parameter(b'Ae On').has_value(b'On'),
                                           use(b'Ae Attack').if_parameter(b'Ae On').has_value(b'On'),
                                           use(b'Ae Peak').if_parameter(b'Ae On').has_value(b'On'),
                                           use(b'Ae Decay').if_parameter(b'Ae On').has_value(b'On'),
                                           use(b'Ae Sustain').if_parameter(b'Ae On').has_value(b'On'),
                                           use(b'Ae Release').if_parameter(b'Ae On').has_value(b'On'))}),
                   (
                    b'Aux Env. 2',
                    {BANK_PARAMETERS_KEY: (
                                           b'Ae On',
                                           use(b'Ae End').if_parameter(b'Ae On').has_value(b'Off'),
                                           use(b'Ae R < Vel').if_parameter(b'Ae On').has_value(b'Off'),
                                           use(b'Ae Mode').if_parameter(b'Ae On').has_value(b'Off'),
                                           use(b'').if_parameter(b'Ae On').has_value(b'Off').else_use(b'Ae Loop').if_parameter(b'Ae Mode').has_value(b'Loop').else_use(b'Ae Retrig').if_parameter(b'Ae Mode').has_value(b'Beat').else_use(b'Ae Retrig').if_parameter(b'Ae Mode').has_value(b'Sync').else_use(b''),
                                           b'', b'', b'')}))), 
   b'OriginalSimpler': IndexedDict((
                      (
                       BANK_MAIN_KEY,
                       {BANK_PARAMETERS_KEY: (
                                              use(b'Ve Attack').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Start'),
                                              use(b'Ve Decay').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'End'),
                                              use(b'Ve Sustain').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Fade In').if_parameter(b'Mode').has_value(b'One-Shot').else_use(b'Nudge').if_parameter(b'Mode').has_value(b'Slicing').else_use(b'S Start').if_parameter(b'Mode').has_value(b'Classic'),
                                              use(b'Ve Release').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Fade Out').if_parameter(b'Mode').has_value(b'One-Shot').else_use(b'Playback').if_parameter(b'Mode').has_value(b'Slicing').else_use(b'S Length').if_parameter(b'Mode').has_value(b'Classic'),
                                              use(b'Pan').if_parameter(b'Multi Sample').has_value(b'On').and_parameter(b'F On').has_value(b'Off').else_use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).and_parameter(b'Multi Sample').has_value(b'On').else_use(b'Filter Type (Legacy)').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Transpose').if_parameter(b'Mode').has_value(b'One-Shot').else_use(b'S Loop On').if_parameter(b'Mode').has_value(b'Classic'),
                                              use(b'Filter Freq').if_parameter(b'Multi Sample').has_value(b'On').and_parameter(b'F On').has_value(b'On').else_use(b'Transpose').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Gain').if_parameter(b'Mode').has_value(b'One-Shot').else_use(b'Slice by').if_parameter(b'Mode').has_value(b'Slicing').else_use(b'S Loop Length').if_parameter(b'Mode').has_value(b'Classic').and_parameter(b'S Loop On').has_value(b'On').else_use(b'Transpose'),
                                              use(b'Detune').if_parameter(b'Multi Sample').has_value(b'On').and_parameter(b'F On').has_value(b'Off').else_use(b'Filter Res').if_parameter(b'Filter Res').is_available(True).and_parameter(b'Multi Sample').has_value(b'On').else_use(b'Filter Res (Legacy)').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Trigger Mode').if_parameter(b'Mode').has_value(b'One-Shot').else_use(b'Sensitivity').if_parameter(b'Slice by').has_value(b'Transient').and_parameter(b'Mode').has_value(b'Slicing').else_use(b'Division').if_parameter(b'Slice by').has_value(b'Beat').and_parameter(b'Mode').has_value(b'Slicing').else_use(b'Regions').if_parameter(b'Slice by').has_value(b'Region').and_parameter(b'Mode').has_value(b'Slicing').else_use(b'Pad Slicing').if_parameter(b'Slice Style').has_value(b'Manual').and_parameter(b'Mode').has_value(b'Slicing').else_use(b'Trigger Mode').if_parameter(b'Mode').has_value(b'Slicing').else_use(b'S Loop Fade').if_parameter(b'Mode').has_value(b'Classic').and_parameter(b'Warp').has_value(b'Off').else_use(b'Detune'),
                                              use(b'Volume').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Mode'))}),
                      (
                       b'Global',
                       {BANK_PARAMETERS_KEY: (
                                              b'Glide Mode',
                                              use(b'').if_parameter(b'Glide Mode').has_value(b'Off').else_use(b'Glide Time'),
                                              b'Voices', b'Transpose', b'Detune', b'Vol < Vel',
                                              b'Gain', b'Volume')}),
                      (
                       b'Volume Envelope',
                       {BANK_PARAMETERS_KEY: (
                                              use(b'Ve Attack').if_parameter(b'Mode').has_value(b'Classic').else_use(b'Fade In'),
                                              use(b'Ve Decay').if_parameter(b'Mode').has_value(b'Classic').else_use(b'Fade Out'),
                                              use(b'Ve Sustain').if_parameter(b'Mode').has_value(b'Classic'),
                                              use(b'Ve Release').if_parameter(b'Mode').has_value(b'Classic'),
                                              b'Filt < Vel', b'Vol < Vel', b'Vol < LFO', b'Volume')}),
                      (
                       b'Warp',
                       {BANK_PARAMETERS_KEY: (
                                              use(b'').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'Warp'),
                                              use(b'').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'').if_parameter(b'Warp').has_value(b'Off').else_use(b'Warp Mode'),
                                              use(b'').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'').if_parameter(b'Warp').has_value(b'Off').else_use(b'Preserve').if_parameter(b'Warp Mode').has_value(b'Beats').else_use(b'Grain Size Tones').if_parameter(b'Warp Mode').has_value(b'Tones').else_use(b'Grain Size Texture').if_parameter(b'Warp Mode').has_value(b'Texture').else_use(b'Formants').if_parameter(b'Warp Mode').has_value(b'Pro'),
                                              use(b'').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'').if_parameter(b'Warp').has_value(b'Off').else_use(b'Loop Mode').if_parameter(b'Warp Mode').has_value(b'Beats').else_use(b'Flux').if_parameter(b'Warp Mode').has_value(b'Texture').else_use(b'Envelope Complex Pro').if_parameter(b'Warp Mode').has_value(b'Pro'),
                                              use(b'').if_parameter(b'Multi Sample').has_value(b'On').else_use(b'').if_parameter(b'Warp').has_value(b'Off').else_use(b'Envelope').if_parameter(b'Warp Mode').has_value(b'Beats'),
                                              b'', b'', b'')}),
                      (
                       b'Filter',
                       {BANK_PARAMETERS_KEY: (
                                              b'F On',
                                              use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).else_use(b'Filter Type (Legacy)'),
                                              use(b'Filter Freq').if_parameter(b'F On').has_value(b'On'),
                                              use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Res').if_parameter(b'Filter Res').is_available(True).else_use(b'Filter Res (Legacy)'),
                                              use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Lowpass').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Highpass').else_use(b'Filter Circuit - BP/NO/Morph'),
                                              use(b'').if_parameter(b'F On').has_value(b'Off').else_use(b'Filter Morph').if_parameter(b'Filter Type').has_value(b'Morph').else_use(b'').if_parameter(b'Filter Type').has_value(b'Lowpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Highpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Bandpass').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Notch').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'Filter Drive'),
                                              use(b'Filter Slope').if_parameter(b'F On').has_value(b'On').and_parameter(b'Filter Slope').is_available(True),
                                              use(b'Filt < LFO').if_parameter(b'F On').has_value(b'On'))}),
                      (
                       b'Filter Envelope',
                       {BANK_PARAMETERS_KEY: (
                                              b'Fe On',
                                              use(b'Fe Attack').if_parameter(b'Fe On').has_value(b'On'),
                                              use(b'Fe Decay').if_parameter(b'Fe On').has_value(b'On'),
                                              use(b'Fe Sustain').if_parameter(b'Fe On').has_value(b'On'),
                                              use(b'Fe Release').if_parameter(b'Fe On').has_value(b'On'),
                                              use(b'Filter Freq').if_parameter(b'Fe On').has_value(b'On').and_parameter(b'F On').has_value(b'On'),
                                              use(b'Filter Res').if_parameter(b'Fe On').has_value(b'On').and_parameter(b'F On').has_value(b'On'),
                                              use(b'Fe < Env').if_parameter(b'Fe On').has_value(b'On'))}),
                      (
                       b'Pitch Envelope',
                       {BANK_PARAMETERS_KEY: (
                                              b'Pe On',
                                              use(b'Pe Attack').if_parameter(b'Pe On').has_value(b'On'),
                                              use(b'Pe Decay').if_parameter(b'Pe On').has_value(b'On'),
                                              use(b'Pe Sustain').if_parameter(b'Pe On').has_value(b'On'),
                                              use(b'Pe Release').if_parameter(b'Pe On').has_value(b'On'),
                                              use(b'Pe < Env').if_parameter(b'Pe On').has_value(b'On'),
                                              b'', b'')}),
                      (
                       b'LFO',
                       {BANK_PARAMETERS_KEY: (
                                              b'L On',
                                              use(b'L Wave').if_parameter(b'L On').has_value(b'On'),
                                              use(b'L Sync').if_parameter(b'L On').has_value(b'On'),
                                              use(b'').if_parameter(b'L On').has_value(b'Off').else_use(b'L Rate').if_parameter(b'L Sync').has_value(b'Free').else_use(b'L Sync Rate'),
                                              use(b'L Attack').if_parameter(b'L On').has_value(b'On'),
                                              use(b'L R < Key').if_parameter(b'L On').has_value(b'On'),
                                              use(b'L Retrig').if_parameter(b'L On').has_value(b'On'),
                                              use(b'L Offset').if_parameter(b'L On').has_value(b'On'))}),
                      (
                       b'Pan',
                       {BANK_PARAMETERS_KEY: (
                                              b'Pan', b'Spread', b'Pan < Rnd', b'Pan < LFO', b'', b'', b'', b'')}))), 
   b'StringStudio': IndexedDict((
                   (
                    BANK_MAIN_KEY,
                    {BANK_PARAMETERS_KEY: (
                                           use(b'Excitator Type').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc ForceMassProt').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc FricStiff').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Velocity').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'E Pos').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           b'String Decay', b'Str Damping', b'Volume')}),
                   (
                    b'Excitator',
                    {BANK_PARAMETERS_KEY: (
                                           b'Exc On/Off',
                                           use(b'Excitator Type').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc ForceMassProt').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc FricStiff').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Velocity').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'E Pos').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'E Pos Abs').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           b'Volume')}),
                   (
                    b'String & Pickup',
                    {BANK_PARAMETERS_KEY: (
                                           b'String Decay', b'S Decay < Key', b'S Decay Ratio', b'Str Inharmon',
                                           b'Str Damping', b'S Damp < Key', b'Pickup On/Off',
                                           use(b'Pickup Pos').if_parameter(b'Pickup On/Off').has_value(b'On'))}),
                   (
                    b'Damper',
                    {BANK_PARAMETERS_KEY: (
                                           b'Damper On',
                                           use(b'Damper Mass').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'D Stiffness').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'Damp Pos').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'D Damping').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'Damper Gated').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'').if_parameter(b'Damper On').has_value(b'Off').else_use(b'D Velocity').if_parameter(b'Damper Gated').has_value(b'On').else_use(b''),
                                           use(b'D Pos Abs').if_parameter(b'Damper On').has_value(b'On'))}),
                   (
                    b'Termination',
                    {BANK_PARAMETERS_KEY: (
                                           b'Term On/Off',
                                           use(b'Term Mass').if_parameter(b'Term On/Off').has_value(b'On'),
                                           use(b'Term Fng Stiff').if_parameter(b'Term On/Off').has_value(b'On'),
                                           use(b'Term Fret Stiff').if_parameter(b'Term On/Off').has_value(b'On'),
                                           use(b'T Mass < Vel').if_parameter(b'Term On/Off').has_value(b'On'),
                                           use(b'T Mass < Key').if_parameter(b'Term On/Off').has_value(b'On'),
                                           b'', b'Volume')}),
                   (
                    b'Body',
                    {BANK_PARAMETERS_KEY: (
                                           b'Body On/Off',
                                           use(b'Body Type').if_parameter(b'Body On/Off').has_value(b'On'),
                                           use(b'Body Size').if_parameter(b'Body On/Off').has_value(b'On'),
                                           use(b'Body Decay').if_parameter(b'Body On/Off').has_value(b'On'),
                                           use(b'Body Low-Cut').if_parameter(b'Body On/Off').has_value(b'On'),
                                           use(b'Body High-Cut').if_parameter(b'Body On/Off').has_value(b'On'),
                                           use(b'Body Mix').if_parameter(b'Body On/Off').has_value(b'On'),
                                           b'Volume')}),
                   (
                    b'Filter',
                    {BANK_PARAMETERS_KEY: (
                                           b'Filter On/Off',
                                           use(b'Filter Freq').if_parameter(b'Filter On/Off').has_value(b'On'),
                                           use(b'Filter Reso').if_parameter(b'Filter On/Off').has_value(b'On'),
                                           use(b'Filter Type').if_parameter(b'Filter On/Off').has_value(b'On'),
                                           use(b'Freq < Env').if_parameter(b'Filter On/Off').has_value(b'On'),
                                           use(b'Freq < LFO').if_parameter(b'Filter On/Off').has_value(b'On'),
                                           use(b'Reso < Env').if_parameter(b'Filter On/Off').has_value(b'On'),
                                           use(b'Reso < LFO').if_parameter(b'Filter On/Off').has_value(b'On'))}),
                   (
                    b'LFO',
                    {BANK_PARAMETERS_KEY: (
                                           b'LFO On/Off',
                                           use(b'LFO Shape').if_parameter(b'LFO On/Off').has_value(b'On'),
                                           use(b'LFO Sync On').if_parameter(b'LFO On/Off').has_value(b'On'),
                                           use(b'').if_parameter(b'LFO On/Off').has_value(b'Off').else_use(b'LFO SyncRate').if_parameter(b'LFO Sync On').has_value(b'Beat').else_use(b'LFO Speed'),
                                           use(b'LFO Delay').if_parameter(b'LFO On/Off').has_value(b'On'),
                                           use(b'LFO Fade In').if_parameter(b'LFO On/Off').has_value(b'On'),
                                           b'', b'')}),
                   (
                    b'Vibrato',
                    {BANK_PARAMETERS_KEY: (
                                           b'Vibrato On/Off',
                                           use(b'Vib Delay').if_parameter(b'Vibrato On/Off').has_value(b'On'),
                                           use(b'Vib Fade-In').if_parameter(b'Vibrato On/Off').has_value(b'On'),
                                           use(b'Vib Speed').if_parameter(b'Vibrato On/Off').has_value(b'On'),
                                           use(b'Vib Amount').if_parameter(b'Vibrato On/Off').has_value(b'On'),
                                           use(b'Vib < ModWh').if_parameter(b'Vibrato On/Off').has_value(b'On'),
                                           use(b'Vib Error').if_parameter(b'Vibrato On/Off').has_value(b'On'),
                                           b'')}),
                   (
                    b'Unison & Portamento',
                    {BANK_PARAMETERS_KEY: (
                                           b'Unison On/Off',
                                           use(b'Unison Voices').if_parameter(b'Unison On/Off').has_value(b'On'),
                                           use(b'Uni Delay').if_parameter(b'Unison On/Off').has_value(b'On'),
                                           use(b'Uni Detune').if_parameter(b'Unison On/Off').has_value(b'On'),
                                           b'Porta On/Off',
                                           use(b'Porta Time').if_parameter(b'Porta On/Off').has_value(b'On'),
                                           use(b'Porta Legato').if_parameter(b'Porta On/Off').has_value(b'On'),
                                           use(b'Porta Prop').if_parameter(b'Porta On/Off').has_value(b'On'))}),
                   (
                    b'Global',
                    {BANK_PARAMETERS_KEY: (
                                           b'Octave', b'Semitone', b'Fine Tune', b'Voices',
                                           b'PB Depth', b'Stretch', b'Error', b'Key Priority')}),
                   (
                    b'Filt. Env.',
                    {BANK_PARAMETERS_KEY: (
                                           b'FEG On/Off',
                                           use(b'FEG Attack').if_parameter(b'FEG On/Off').has_value(b'On'),
                                           use(b'FEG Decay').if_parameter(b'FEG On/Off').has_value(b'On'),
                                           use(b'FEG Sustain').if_parameter(b'FEG On/Off').has_value(b'On'),
                                           use(b'FEG Release').if_parameter(b'FEG On/Off').has_value(b'On'),
                                           use(b'FEG Att < Vel').if_parameter(b'FEG On/Off').has_value(b'On'),
                                           use(b'FEG < Vel').if_parameter(b'FEG On/Off').has_value(b'On'),
                                           b'')}),
                   (
                    b'Excitator Mod.',
                    {BANK_PARAMETERS_KEY: (
                                           use(b'Exc Prot < Vel').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Prot < Key').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Stiff < Vel').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Stiff < Key').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Vel < Vel').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'Exc Vel < Key').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'E Pos < Vel').if_parameter(b'Exc On/Off').has_value(b'On'),
                                           use(b'E Pos < Key').if_parameter(b'Exc On/Off').has_value(b'On'))}),
                   (
                    b'Mass Mod.',
                    {BANK_PARAMETERS_KEY: (
                                           use(b'D Mass < Key').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'D Stiff < Key').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'D Pos < Key').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'D Pos < Vel').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'Damper Gated').if_parameter(b'Damper On').has_value(b'On'),
                                           use(b'').if_parameter(b'Damper On').has_value(b'Off').else_use(b'D Velo < Key').if_parameter(b'Damper Gated').has_value(b'On').else_use(b''),
                                           b'', b'')}))), 
   b'InstrumentVector': IndexedDict((
                       (
                        BANK_MAIN_KEY,
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Osc 1 Pos').with_name(b'Pos 1').if_parameter(b'Osc 1 On').has_value(b'On').else_use(b'Osc 2 Pos').with_name(b'Pos 2').if_parameter(b'Osc 2 On').has_value(b'On').else_use(b'Sub Tone').if_parameter(b'Sub On').has_value(b'On').else_use(b''),
                                               use(b'Filter 1 Freq').with_name(b'Freq 1').if_parameter(b'Filter 1 On').has_value(b'On').else_use(b'Filter 2 Freq').with_name(b'Freq 2').if_parameter(b'Filter 2 On').has_value(b'On').else_use(b'Osc 1 Effect 1').with_name(b'FX 1').if_parameter(b'Osc 1 On').has_value(b'On').else_use(b'Osc 2 Effect 1').with_name(b'FX 1').if_parameter(b'Osc 2 On').has_value(b'On').else_use(b'Osc 1 Effect 1').with_name(b'Osc1 FX1').if_parameter(b'Osc 1 On').has_value(b'Osc2 FX1').else_use(b'Osc 2 Effect 1').with_name(b'FX 1').if_parameter(b'Osc 2 On').has_value(b'On').else_use(b'Sub Transpose').if_parameter(b'Sub On').has_value(b'On').else_use(b''),
                                               use(b'Filter 1 Res').with_name(b'Res 1').if_parameter(b'Filter 1 On').has_value(b'On').else_use(b'Filter 2 Res').with_name(b'Res 2').if_parameter(b'Filter 2 On').has_value(b'On').else_use(b'Osc 1 Effect 2').with_name(b'FX 2').if_parameter(b'Osc 1 On').has_value(b'On').else_use(b'Osc 2 Effect 2').with_name(b'FX 2').if_parameter(b'Osc 2 On').has_value(b'On').else_use(b'Amp Decay').with_name(b'Decay'),
                                               use(b'Amp Release').with_name(b'Release'),
                                               b'Unison Amount',
                                               b'Time',
                                               b'Global Mod Amount',
                                               b'Volume')}),
                       (
                        b'Osc 1',
                        {BANK_PARAMETERS_KEY: (
                                               b'Osc 1 On',
                                               use(b'Osc 1 Pitch').with_name(b'Pitch'),
                                               use(b'Osc 1 Category').with_name(b'Category'),
                                               use(b'Osc 1 Table').with_name(b'Table'),
                                               use(b'Osc 1 Pos').with_name(b'Position'),
                                               use(b'Osc 1 Effect Type').with_name(b'Effect Type'),
                                               use(b'Osc 1 Effect 1').with_name(b'FX 1'),
                                               use(b'Osc 1 Effect 2').with_name(b'FX 2'))}),
                       (
                        b'Osc 2',
                        {BANK_PARAMETERS_KEY: (
                                               b'Osc 2 On',
                                               use(b'Osc 2 Pitch').with_name(b'Pitch'),
                                               use(b'Osc 2 Category').with_name(b'Category'),
                                               use(b'Osc 2 Table').with_name(b'Table'),
                                               use(b'Osc 2 Pos').with_name(b'Position'),
                                               use(b'Osc 2 Effect Type').with_name(b'Effect Type'),
                                               use(b'Osc 2 Effect 1').with_name(b'FX 1'),
                                               use(b'Osc 2 Effect 2').with_name(b'FX 2'))}),
                       (
                        b'Sub',
                        {BANK_PARAMETERS_KEY: (
                                               b'Sub On',
                                               use(b'Sub Transpose').with_name(b'Transp'),
                                               use(b'Sub Tone').with_name(b'Tone'),
                                               b'',
                                               b'',
                                               b'',
                                               b'',
                                               use(b'Sub Gain').with_name(b'Gain'))}),
                       (
                        b'Mix',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Osc 1 Pitch').with_name(b'Pitch 1'),
                                               use(b'Osc 2 Pitch').with_name(b'Pitch 2'),
                                               use(b'Sub Transpose').with_name(b'Octave Sub'),
                                               use(b'Osc 1 Pan').with_name(b'Pan 1'),
                                               use(b'Osc 2 Pan').with_name(b'Pan 2'),
                                               use(b'Osc 1 Gain').with_name(b'Gain 1'),
                                               use(b'Osc 2 Gain').with_name(b'Gain 2'),
                                               use(b'Sub Gain').with_name(b'Gain Sub'))}),
                       (
                        b'Filter 1',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Filter 1 On').with_name(b'F1 On'),
                                               use(b'Filter 1 Type').with_name(b'Type'),
                                               use(b'Filter 1 LP/HP').with_name(b'Circuit').if_parameter(b'Filter 1 Type').has_value(b'Lowpass').or_parameter(b'Filter 1 Type').has_value(b'Highpass').else_use(b'Filter 1 BP/NO/Morph').with_name(b'Circuit').if_parameter(b'Filter 1 Type').has_value(b'Bandpass').or_parameter(b'Filter 1 Type').has_value(b'Notch').or_parameter(b'Filter 1 Type').has_value(b'Morph').else_use(b''),
                                               use(b'Filter 1 Slope').with_name(b'Slope'),
                                               use(b'Filter 1 Freq').with_name(b'Freq'),
                                               use(b'Filter 1 Res').with_name(b'Res'),
                                               use(b'Filter 1 Drive').with_name(b'Drive').if_parameter(b'Filter 1 Type').has_value(b'Lowpass').or_parameter(b'Filter 1 Type').has_value(b'Highpass').or_parameter(b'Filter 1 Type').has_value(b'Notch').or_parameter(b'Filter 1 Type').has_value(b'Bandpass').and_parameter(b'Filter 1 LP/HP').does_not_have_value(b'Clean').else_use(b'Filter 1 Morph').with_name(b'Morph').if_parameter(b'Filter 1 Type').has_value(b'Morph').else_use(b''),
                                               b'')}),
                       (
                        b'Filter 2',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Filter 2 On').with_name(b'F2 On'),
                                               use(b'Filter 2 Type').with_name(b'Type'),
                                               use(b'Filter 2 LP/HP').with_name(b'Circuit').if_parameter(b'Filter 2 Type').has_value(b'Lowpass').or_parameter(b'Filter 2 Type').has_value(b'Highpass').else_use(b'Filter 2 BP/NO/Morph').with_name(b'Circuit').if_parameter(b'Filter 2 Type').has_value(b'Bandpass').or_parameter(b'Filter 2 Type').has_value(b'Notch').or_parameter(b'Filter 2 Type').has_value(b'Morph').else_use(b''),
                                               use(b'Filter 2 Slope').with_name(b'Slope'),
                                               use(b'Filter 2 Freq').with_name(b'Freq'),
                                               use(b'Filter 2 Res').with_name(b'Res'),
                                               use(b'Filter 2 Drive').with_name(b'Drive').if_parameter(b'Filter 2 Type').has_value(b'Lowpass').or_parameter(b'Filter 2 Type').has_value(b'Highpass').or_parameter(b'Filter 2 Type').has_value(b'Notch').or_parameter(b'Filter 2 Type').has_value(b'Bandpass').and_parameter(b'Filter 2 LP/HP').does_not_have_value(b'Clean').else_use(b'Filter 2 Morph').with_name(b'Morph').if_parameter(b'Filter 2 Type').has_value(b'Morph').else_use(b''),
                                               b'')}),
                       (
                        b'Amp Env',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Amp Attack').with_name(b'Attack'),
                                               use(b'Amp Decay').with_name(b'Decay'),
                                               use(b'Amp Sustain').with_name(b'Sustain'),
                                               use(b'Amp Release').with_name(b'Release'),
                                               use(b'Amp A Slope').with_name(b'A Slope'),
                                               use(b'Amp D Slope').with_name(b'D Slope'),
                                               use(b'Amp R Slope').with_name(b'R Slope'),
                                               use(b'Amp Loop Mode').with_name(b'Mode'))}),
                       (
                        b'Env 2',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Env 2 Attack').with_name(b'Attack'),
                                               use(b'Env 2 Decay').with_name(b'Decay'),
                                               use(b'Env 2 Sustain').with_name(b'Sustain'),
                                               use(b'Env 2 Release').with_name(b'Release'),
                                               use(b'Env 2 A Slope').with_name(b'A Slope'),
                                               use(b'Env 2 D Slope').with_name(b'D Slope'),
                                               use(b'Env 2 R Slope').with_name(b'R Slope'),
                                               use(b'Env 2 Loop Mode').with_name(b'Mode'))}),
                       (
                        b'Env 3',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'Env 3 Attack').with_name(b'Attack'),
                                               use(b'Env 3 Decay').with_name(b'Decay'),
                                               use(b'Env 3 Sustain').with_name(b'Sustain'),
                                               use(b'Env 3 Release').with_name(b'Release'),
                                               use(b'Env 3 A Slope').with_name(b'A Slope'),
                                               use(b'Env 3 D Slope').with_name(b'D Slope'),
                                               use(b'Env 3 R Slope').with_name(b'R Slope'),
                                               use(b'Env 3 Loop Mode').with_name(b'Mode'))}),
                       (
                        b'LFO 1',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'LFO 1 Shape').with_name(b'Shape'),
                                               use(b'LFO 1 Sync').with_name(b'Sync'),
                                               use(b'LFO 1 S. Rate').with_name(b'SyncRate').if_parameter(b'LFO 1 Sync').has_value(b'Tempo').else_use(b'LFO 1 Rate').with_name(b'Rate'),
                                               use(b'LFO 1 Shaping').with_name(b'Shaping'),
                                               use(b'LFO 1 Attack Time').with_name(b'Attack'),
                                               use(b'LFO 1 Amount').with_name(b'Amount'),
                                               use(b'LFO 1 Phase Offset').with_name(b'Phase'),
                                               use(b'LFO 1 Retrigger').with_name(b'Retrigger'))}),
                       (
                        b'LFO 2',
                        {BANK_PARAMETERS_KEY: (
                                               use(b'LFO 2 Shape').with_name(b'Shape'),
                                               use(b'LFO 2 Sync').with_name(b'Sync'),
                                               use(b'LFO 2 S. Rate').with_name(b'SyncRate').if_parameter(b'LFO 2 Sync').has_value(b'Tempo').else_use(b'LFO 2 Rate').with_name(b'Rate'),
                                               use(b'LFO 2 Shaping').with_name(b'Shaping'),
                                               use(b'LFO 2 Attack Time').with_name(b'Attack'),
                                               use(b'LFO 2 Amount').with_name(b'Amount'),
                                               use(b'LFO 2 Phase Offset').with_name(b'Phase'),
                                               use(b'LFO 2 Retrigger').with_name(b'Retrigger'))}),
                       (
                        b'Global',
                        {BANK_PARAMETERS_KEY: (
                                               b'Time',
                                               b'Global Mod Amount',
                                               b'Unison Mode',
                                               b'Unison Amount',
                                               b'Mono On',
                                               b'Glide',
                                               b'Transpose',
                                               b'Volume')}))), 
   b'MidiArpeggiator': IndexedDict((
                      (
                       BANK_MAIN_KEY,
                       {BANK_PARAMETERS_KEY: (
                                              b'Style',
                                              use(b'Synced Rate').if_parameter(b'Sync On').has_value(b'On').else_use(b'Free Rate'),
                                              b'Gate', b'Offset',
                                              b'Hold On', b'Tranpose Key', b'Transp. Steps', b'Transp. Dist.')}),
                      (
                       b'Rhythm',
                       {BANK_PARAMETERS_KEY: (
                                              b'Sync On',
                                              use(b'Synced Rate').if_parameter(b'Sync On').has_value(b'On').else_use(b'Free Rate'),
                                              use(b'Groove').if_parameter(b'Sync On').has_value(b'On'),
                                              b'Offset', b'Repeats',
                                              b'Gate', b'Retrigger Mode',
                                              use(b'Ret. Interval').if_parameter(b'Retrigger Mode').has_value(b'Beat'))}),
                      (
                       b'Pitch/Vel.',
                       {BANK_PARAMETERS_KEY: (
                                              b'Tranpose Mode',
                                              use(b'').if_parameter(b'Tranpose Mode').has_value(b'Shift').else_use(b'Tranpose Key'),
                                              use(b'').if_parameter(b'Tranpose Mode').has_value(b'Shift').else_use(b'Transp. Steps'),
                                              use(b'').if_parameter(b'Tranpose Mode').has_value(b'Shift').else_use(b'Transp. Dist.'),
                                              b'Velocity On',
                                              use(b'Vel. Retrigger').if_parameter(b'Velocity On').has_value(b'On'),
                                              use(b'Velocity Decay').if_parameter(b'Velocity On').has_value(b'On'),
                                              use(b'Velocity Target').if_parameter(b'Velocity On').has_value(b'On'))}))), 
   b'MidiChord': IndexedDict((
                (
                 b'Shift',
                 {BANK_PARAMETERS_KEY: (
                                        b'Shift1', b'Shift2', b'Shift3', b'Shift4',
                                        b'Shift5', b'Shift6', b'', b'')}),
                (
                 b'Velocity',
                 {BANK_PARAMETERS_KEY: (
                                        b'Velocity1', b'Velocity2', b'Velocity3', b'Velocity4',
                                        b'Velocity5', b'Velocity6', b'', b'')}))), 
   b'MidiNoteLength': IndexedDict((
                     (
                      BANK_MAIN_KEY,
                      {BANK_PARAMETERS_KEY: (
                                             b'Trigger Mode', b'Sync On',
                                             use(b'Synced Length').if_parameter(b'Sync On').has_value(b'On').else_use(b'Time Length'),
                                             b'Gate',
                                             use(b'On/Off-Balance').if_parameter(b'Trigger Mode').has_value(b'On'),
                                             use(b'Decay Time').if_parameter(b'Trigger Mode').has_value(b'On'),
                                             use(b'Decay Key Scale').if_parameter(b'Trigger Mode').has_value(b'On'),
                                             b'')}),)), 
   b'MidiPitcher': IndexedDict((
                  (
                   BANK_MAIN_KEY,
                   {BANK_PARAMETERS_KEY: (
                                          b'Pitch', b'Range', b'Lowest', b'', b'', b'', b'', b'')}),)), 
   b'MidiRandom': IndexedDict((
                 (
                  BANK_MAIN_KEY,
                  {BANK_PARAMETERS_KEY: (
                                         b'Chance', b'Choices', b'Mode', b'Scale', b'Sign', b'', b'', b'')}),)), 
   b'MidiScale': IndexedDict((
                (
                 BANK_MAIN_KEY,
                 {BANK_PARAMETERS_KEY: (
                                        b'Base', b'Transpose', b'Range', b'Lowest', b'Fold', b'', b'', b'')}),)), 
   b'MidiVelocity': IndexedDict((
                   (
                    BANK_MAIN_KEY,
                    {BANK_PARAMETERS_KEY: (
                                           b'Mode',
                                           use(b'').if_parameter(b'Mode').has_value(b'Fixed').else_use(b'Drive'),
                                           use(b'').if_parameter(b'Mode').has_value(b'Fixed').else_use(b'Compand'),
                                           b'Out Hi',
                                           use(b'').if_parameter(b'Mode').has_value(b'Fixed').else_use(b'Out Low'),
                                           use(b'').if_parameter(b'Mode').has_value(b'Fixed').else_use(b'Range'),
                                           use(b'').if_parameter(b'Mode').has_value(b'Fixed').else_use(b'Lowest'),
                                           b'Random')}),)), 
   b'Amp': IndexedDict((
          (
           b'Global',
           {BANK_PARAMETERS_KEY: (
                                  b'Amp Type', b'Bass', b'Middle', b'Treble',
                                  b'Presence', b'Gain', b'Volume', b'Dry/Wet')}),
          (
           b'Dual/Mono',
           {BANK_PARAMETERS_KEY: (
                                  b'Dual Mono', b'', b'', b'', b'', b'', b'', b'')}))), 
   b'AutoFilter': IndexedDict((
                 (
                  BANK_MAIN_KEY,
                  {BANK_PARAMETERS_KEY: (
                                         use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).else_use(b'Filter Type (Legacy)'),
                                         use(b'Frequency'),
                                         use(b'Resonance').if_parameter(b'Resonance').is_available(True).else_use(b'Resonance (Legacy)'),
                                         use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Lowpass').else_use(b'Filter Circuit - LP/HP').if_parameter(b'Filter Type').has_value(b'Highpass').else_use(b'Filter Circuit - BP/NO/Morph'),
                                         use(b'Morph').if_parameter(b'Filter Type').has_value(b'Morph').else_use(b'').if_parameter(b'Filter Type').has_value(b'Lowpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Highpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Bandpass').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Notch').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'Drive').if_parameter(b'Drive').is_available(True),
                                         b'LFO Amount', b'LFO Sync',
                                         use(b'LFO Frequency').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'LFO Sync Rate'))}),
                 (
                  b'Envelope',
                  {BANK_PARAMETERS_KEY: (
                                         use(b'Filter Type').if_parameter(b'Filter Type').is_available(True).else_use(b'Filter Type (Legacy)'),
                                         use(b'Frequency'),
                                         use(b'Resonance').if_parameter(b'Resonance').is_available(True).else_use(b'Resonance (Legacy)'),
                                         use(b'Slope').if_parameter(b'Slope').is_available(True),
                                         use(b'Morph').if_parameter(b'Filter Type').has_value(b'Morph').else_use(b'').if_parameter(b'Filter Type').has_value(b'Lowpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Highpass').and_parameter(b'Filter Circuit - LP/HP').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Bandpass').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'').if_parameter(b'Filter Type').has_value(b'Notch').and_parameter(b'Filter Circuit - BP/NO/Morph').has_value(b'Clean').else_use(b'Drive').if_parameter(b'Drive').is_available(True),
                                         b'Env. Attack', b'Env. Release', b'Env. Modulation')}),
                 (
                  b'LFO',
                  {BANK_PARAMETERS_KEY: (
                                         b'LFO Amount', b'LFO Waveform', b'LFO Sync',
                                         use(b'LFO Frequency').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'LFO Sync Rate'),
                                         use(b'').if_parameter(b'LFO Waveform').has_value(b'S&H Mono').else_use(b'LFO Offset').if_parameter(b'LFO Sync').has_value(b'Sync').else_use(b'LFO Stereo Mode'),
                                         use(b'').if_parameter(b'LFO Waveform').has_value(b'S&H Mono').else_use(b'LFO Phase').if_parameter(b'LFO Sync').has_value(b'Sync').else_use(b'LFO Phase').if_parameter(b'LFO Stereo Mode').has_value(b'Phase').else_use(b'LFO Spin'),
                                         b'LFO Quantize On',
                                         use(b'LFO Quantize Rate').if_parameter(b'LFO Quantize On').has_value(b'On'))}),
                 (
                  b'Sidechain',
                  {BANK_PARAMETERS_KEY: (
                                         b'S/C On',
                                         use(b'S/C Mix').if_parameter(b'S/C On').has_value(b'On'),
                                         use(b'S/C Gain').if_parameter(b'S/C On').has_value(b'On'),
                                         b'', b'', b'', b'', b'')}))), 
   b'AutoPan': IndexedDict((
              (
               BANK_MAIN_KEY,
               {BANK_PARAMETERS_KEY: (
                                      b'Amount', b'Shape', b'Invert', b'Waveform', b'LFO Type',
                                      use(b'Sync Rate').if_parameter(b'LFO Type').has_value(b'Beats').else_use(b'Frequency'),
                                      use(b'').if_parameter(b'Waveform').has_value(b'S&H Width').else_use(b'Stereo Mode').if_parameter(b'LFO Type').has_value(b'Frequency').else_use(b'Offset'),
                                      use(b'Width (Random)').if_parameter(b'Waveform').has_value(b'S&H Width').else_use(b'Phase').if_parameter(b'LFO Type').has_value(b'Beats').else_use(b'Spin').if_parameter(b'Stereo Mode').has_value(b'Spin').else_use(b'Phase'))}),)), 
   b'BeatRepeat': IndexedDict((
                 (
                  BANK_MAIN_KEY,
                  {BANK_PARAMETERS_KEY: (
                                         b'Grid', b'Interval', b'Offset', b'Gate',
                                         b'Pitch', b'Pitch Decay', b'Variation', b'Chance')}),
                 (
                  b'Filt/Mix',
                  {BANK_PARAMETERS_KEY: (
                                         b'Filter On',
                                         use(b'Filter Freq').if_parameter(b'Filter On').has_value(b'On'),
                                         use(b'Filter Width').if_parameter(b'Filter On').has_value(b'On'),
                                         b'', b'Mix Type', b'Volume', b'Decay', b'Chance')}),
                 (
                  b'Repeat Rate',
                  {BANK_PARAMETERS_KEY: (
                                         b'Repeat', b'Interval', b'Offset', b'Gate',
                                         b'Grid', b'Block Triplets', b'Variation', b'Variation Type')}))), 
   b'Cabinet': IndexedDict((
              (
               BANK_MAIN_KEY,
               {BANK_PARAMETERS_KEY: (
                                      b'Cabinet Type', b'Microphone Type', b'Microphone Position', b'Dual Mono',
                                      b'', b'', b'', b'Dry/Wet')}),)), 
   b'Chorus': IndexedDict((
             (
              b'Chorus',
              {BANK_PARAMETERS_KEY: (
                                     b'LFO Amount', b'LFO Rate', b'Delay 1 Time', b'Delay 1 HiPass',
                                     b'Delay 2 Mode',
                                     use(b'').if_parameter(b'Delay 2 Mode').has_value(b'Off').else_use(b'Delay 2 Time'),
                                     b'Feedback', b'Dry/Wet')}),
             (
              b'Other',
              {BANK_PARAMETERS_KEY: (
                                     b'LFO Extend On', b'Polarity', b'Link On', b'',
                                     b'', b'', b'', b'')}))), 
   b'Compressor2': IndexedDict((
                  (
                   BANK_MAIN_KEY,
                   {BANK_PARAMETERS_KEY: (
                                          b'Threshold',
                                          use(b'Expansion Ratio').if_parameter(b'Model').has_value(b'Expand').else_use(b'Ratio'),
                                          b'Model', b'Knee', b'Attack',
                                          use(b'Release').if_parameter(b'Auto Release On/Off').has_value(b'Off').else_use(b'Makeup').if_parameter(b'S/C On').has_value(b'Off'),
                                          b'Dry/Wet', b'Output Gain')}),
                  (
                   b'Sidechain',
                   {BANK_PARAMETERS_KEY: (
                                          b'S/C On',
                                          use(b'S/C Gain').if_parameter(b'S/C On').has_value(b'On'),
                                          use(b'S/C Mix').if_parameter(b'S/C On').has_value(b'On'),
                                          b'S/C Listen', b'S/C EQ On',
                                          use(b'S/C EQ Type').if_parameter(b'S/C EQ On').has_value(b'On'),
                                          use(b'S/C EQ Freq').if_parameter(b'S/C EQ On').has_value(b'On'),
                                          use(b'').if_parameter(b'S/C EQ On').has_value(b'Off').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'Low Shelf').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'High Shelf').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'Bell').else_use(b'S/C EQ Q'))}),
                  (
                   b'Global',
                   {BANK_PARAMETERS_KEY: (
                                          b'Auto Release On/Off', b'Env Mode',
                                          use(b'Makeup').if_parameter(b'S/C On').has_value(b'Off'),
                                          b'LookAhead', b'', b'',
                                          b'Dry/Wet', b'Output Gain')}))), 
   b'Corpus': IndexedDict((
             (
              BANK_MAIN_KEY,
              {BANK_PARAMETERS_KEY: (
                                     b'Resonance Type',
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Brightness'),
                                     b'Decay',
                                     use(b'Radius').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'Radius').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Material'),
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'Opening').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Inharmonics'),
                                     use(b'Ratio').if_parameter(b'Resonance Type').has_value(b'Plate').else_use(b'Ratio').if_parameter(b'Resonance Type').has_value(b'Membrane').else_use(b''),
                                     use(b'Transpose').if_parameter(b'MIDI Frequency').has_value(b'On').else_use(b'Tune'),
                                     b'Dry Wet')}),
             (
              b'Body',
              {BANK_PARAMETERS_KEY: (
                                     b'Resonance Type',
                                     use(b'Ratio').if_parameter(b'Resonance Type').has_value(b'Plate').else_use(b'Ratio').if_parameter(b'Resonance Type').has_value(b'Membrane'),
                                     b'Decay',
                                     use(b'Radius').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'Radius').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Material'),
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'Opening').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Inharmonics'),
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Listening L'),
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Listening R'),
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Hit'))}),
             (
              b'LFO',
              {BANK_PARAMETERS_KEY: (
                                     b'LFO On/Off',
                                     use(b'LFO Shape').if_parameter(b'LFO On/Off').has_value(b'On'),
                                     use(b'LFO Amount').if_parameter(b'LFO On/Off').has_value(b'On'),
                                     use(b'LFO Sync').if_parameter(b'LFO On/Off').has_value(b'On'),
                                     use(b'').if_parameter(b'LFO On/Off').has_value(b'Off').else_use(b'LFO Rate').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'LFO Sync Rate'),
                                     use(b'').if_parameter(b'LFO On/Off').has_value(b'Off').else_use(b'LFO Stereo Mode').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'Offset'),
                                     use(b'').if_parameter(b'LFO On/Off').has_value(b'Off').else_use(b'Phase').if_parameter(b'LFO Sync').has_value(b'Sync').else_use(b'Spin').if_parameter(b'LFO Stereo Mode').has_value(b'Spin'),
                                     b'')}),
             (
              b'Tune & Sidechain',
              {BANK_PARAMETERS_KEY: (
                                     b'MIDI Frequency', b'MIDI Mode',
                                     use(b'Transpose').if_parameter(b'MIDI Frequency').has_value(b'On').else_use(b'Tune'),
                                     use(b'Fine').if_parameter(b'MIDI Frequency').has_value(b'On'),
                                     b'Spread',
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Brightness'),
                                     b'Note Off',
                                     use(b'Off Decay').if_parameter(b'Note Off').has_value(b'On'))}),
             (
              b'Filter & Mix',
              {BANK_PARAMETERS_KEY: (
                                     b'Filter On/Off',
                                     use(b'Mid Freq').if_parameter(b'Filter On/Off').has_value(b'On'),
                                     use(b'Width').if_parameter(b'Filter On/Off').has_value(b'On'),
                                     use(b'').if_parameter(b'Resonance Type').has_value(b'Tube').else_use(b'').if_parameter(b'Resonance Type').has_value(b'Pipe').else_use(b'Resonator Quality'),
                                     b'Bleed', b'Gain', b'Dry Wet', b'')}))), 
   b'Delay': IndexedDict((
            (
             BANK_MAIN_KEY,
             {BANK_PARAMETERS_KEY: (
                                    use(b'L Sync Enum').with_name(b'DlayMd L'),
                                    use(b'L 16th').with_name(b'Beat Delay').if_parameter(b'L Sync').has_value(b'On').else_use(b'L Time').with_name(b'Beat Delay'),
                                    b'L Offset',
                                    use(b'R Sync Enum').with_name(b'DlayMd R'),
                                    use(b'R 16th').with_name(b'Beat Delay').if_parameter(b'R Sync').has_value(b'On').else_use(b'R Time').with_name(b'Beat Delay'),
                                    b'R Offset', b'Feedback', b'Dry/Wet')}),
            (
             b'Time',
             {BANK_PARAMETERS_KEY: (
                                    use(b'Delay Mode').with_name(b'DlayMd'), b'Link', b'Ping Pong', b'L Offset',
                                    b'R Offset', b'Freeze', b'Feedback', b'Dry/Wet')}),
            (
             b'Filter/Mod',
             {BANK_PARAMETERS_KEY: (
                                    b'Filter On', b'Filter Freq', b'Filter Width',
                                    use(b'Mod Freq').with_name(b'Filter Mod Rate'),
                                    b'Filter < Mod', b'Dly < Mod', b'Feedback', b'Dry/Wet')}))), 
   b'Tube': IndexedDict((
           (
            b'Character',
            {BANK_PARAMETERS_KEY: (
                                   b'Drive', b'Tube Type', b'Bias', b'Tone',
                                   b'Attack', b'Release', b'Envelope', b'Dry/Wet')}),
           (
            b'Output',
            {BANK_PARAMETERS_KEY: (
                                   b'', b'', b'', b'', b'', b'', b'Output', b'Dry/Wet')}))), 
   b'Echo': IndexedDict((
           (
            BANK_MAIN_KEY,
            {BANK_PARAMETERS_KEY: (
                                   use(b'L Time').with_name(b'M Time').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync').has_value(b'Off').else_use(b'L Time').if_parameter(b'L Sync').has_value(b'Off').else_use(b'L 16th').with_name(b'M 16th').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync Mode').has_value(b'16th').else_use(b'L 16th').if_parameter(b'L Sync Mode').has_value(b'16th').else_use(b'L Division').with_name(b'M Division').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Division'),
                                   use(b'L Sync').with_name(b'M Sync').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Sync'),
                                   use(b'L Sync Mode').with_name(b'M Sync Mode').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync').has_value(b'On').else_use(b'L Sync Mode').if_parameter(b'L Sync').has_value(b'On'),
                                   b'HP Freq', b'LP Freq', b'Feedback', b'Input Gain', b'Dry Wet')}),
           (
            b'L/Mid',
            {BANK_PARAMETERS_KEY: (
                                   use(b'L Time').with_name(b'M Time').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync').has_value(b'Off').else_use(b'L Time').if_parameter(b'L Sync').has_value(b'Off').else_use(b'L 16th').with_name(b'M 16th').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync Mode').has_value(b'16th').else_use(b'L 16th').if_parameter(b'L Sync Mode').has_value(b'16th').else_use(b'L Division').with_name(b'M Division').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Division'),
                                   use(b'L Sync').with_name(b'M Sync').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Sync'),
                                   use(b'L Sync Mode').with_name(b'M Sync Mode').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync').has_value(b'On').else_use(b'L Sync Mode').if_parameter(b'L Sync').has_value(b'On'),
                                   use(b'L Offset').with_name(b'M Offset').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Offset'),
                                   b'Link', b'Feedback', b'Feedback Inv', b'Dry Wet')}),
           (
            b'R/Side',
            {BANK_PARAMETERS_KEY: (
                                   use(b'R Time').with_name(b'S Time').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'R Sync').has_value(b'Off').and_parameter(b'Link').has_value(b'Off').else_use(b'R Time').if_parameter(b'R Sync').has_value(b'Off').and_parameter(b'Link').has_value(b'Off').else_use(b'R 16th').with_name(b'S 16th').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'R Sync Mode').has_value(b'16th').and_parameter(b'Link').has_value(b'Off').else_use(b'R 16th').if_parameter(b'R Sync Mode').has_value(b'16th').and_parameter(b'Link').has_value(b'Off').else_use(b'R Division').with_name(b'S Division').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'Link').has_value(b'Off').else_use(b'R Division').if_parameter(b'Link').has_value(b'Off').else_use(b'L Time').with_name(b'M Time').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync').has_value(b'Off').else_use(b'L Time').if_parameter(b'L Sync').has_value(b'Off').else_use(b'L 16th').with_name(b'M 16th').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync Mode').has_value(b'16th').else_use(b'L 16th').if_parameter(b'L Sync Mode').has_value(b'16th').else_use(b'L Division').with_name(b'M Division').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Division'),
                                   use(b'R Sync').with_name(b'S Sync').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'Link').has_value(b'Off').else_use(b'R Sync').if_parameter(b'Link').has_value(b'Off').else_use(b'L Sync').with_name(b'M Sync').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'L Sync'),
                                   use(b'R Sync Mode').with_name(b'S Sync Mode').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'R Sync').has_value(b'On').and_parameter(b'Link').has_value(b'Off').else_use(b'R Sync Mode').if_parameter(b'R Sync').has_value(b'On').and_parameter(b'Link').has_value(b'Off').else_use(b'L Sync Mode').with_name(b'M Sync Mode').if_parameter(b'Channel Mode').has_value(b'Mid/Side').and_parameter(b'L Sync').has_value(b'On').else_use(b'L Sync Mode').if_parameter(b'L Sync').has_value(b'On'),
                                   use(b'R Offset').with_name(b'S Offset').if_parameter(b'Channel Mode').has_value(b'Mid/Side').else_use(b'R Offset'),
                                   b'Link', b'Feedback', b'Feedback Inv', b'Dry Wet')}),
           (
            b'Global',
            {BANK_PARAMETERS_KEY: (
                                   b'Repitch', b'Channel Mode', b'Stereo Width', b'',
                                   b'Clip Dry', b'Input Gain', b'Output Gain', b'Dry Wet')}),
           (
            b'Filter',
            {BANK_PARAMETERS_KEY: (
                                   b'Filter On', b'HP Freq', b'HP Res', b'LP Freq',
                                   b'LP Res', b'Input Gain', b'Output Gain', b'Dry Wet')}),
           (
            b'Modulation',
            {BANK_PARAMETERS_KEY: (
                                   b'Mod Wave', b'Mod Sync',
                                   use(b'Mod Rate').if_parameter(b'Mod Sync').has_value(b'On').else_use(b'Mod Freq'),
                                   b'Mod Phase', b'Env Mix', b'Dly < Mod', b'Flt < Mod', b'Mod 4x')}),
           (
            b'Reverb',
            {BANK_PARAMETERS_KEY: (
                                   b'Reverb Level', b'Reverb Loc', b'Reverb Decay', b'',
                                   b'', b'', b'', b'')}),
           (
            b'Gate/Ducking',
            {BANK_PARAMETERS_KEY: (
                                   b'Gate On', b'Gate Thr', b'Gate Release', b'',
                                   b'Duck On', b'Duck Thr', b'Duck Release', b'')}),
           (
            b'Noise/Wobble',
            {BANK_PARAMETERS_KEY: (
                                   b'Noise On', b'Noise Amt', b'Noise Mrph', b'',
                                   b'Wobble On', b'Wobble Amt', b'Wobble Mrph', b'')}))), 
   b'Eq8': IndexedDict((
          (
           BANK_MAIN_KEY,
           {BANK_PARAMETERS_KEY: (
                                  use(b'1 Frequency A').if_parameter(b'1 Filter On A').has_value(b'On'),
                                  use(b'').if_parameter(b'1 Filter On A').has_value(b'Off').else_use(b'1 Gain A').if_parameter(b'1 Filter Type A').has_value(b'Low Shelf').else_use(b'1 Gain A').if_parameter(b'1 Filter Type A').has_value(b'Bell').else_use(b'1 Gain A').if_parameter(b'1 Filter Type A').has_value(b'High Shelf').else_use(b'1 Resonance A'),
                                  use(b'2 Frequency A').if_parameter(b'2 Filter On A').has_value(b'On'),
                                  use(b'').if_parameter(b'2 Filter On A').has_value(b'Off').else_use(b'2 Gain A').if_parameter(b'2 Filter Type A').has_value(b'Low Shelf').else_use(b'2 Gain A').if_parameter(b'2 Filter Type A').has_value(b'Bell').else_use(b'2 Gain A').if_parameter(b'2 Filter Type A').has_value(b'High Shelf').else_use(b'2 Resonance A'),
                                  use(b'3 Frequency A').if_parameter(b'3 Filter On A').has_value(b'On'),
                                  use(b'').if_parameter(b'3 Filter On A').has_value(b'Off').else_use(b'3 Gain A').if_parameter(b'3 Filter Type A').has_value(b'Low Shelf').else_use(b'3 Gain A').if_parameter(b'3 Filter Type A').has_value(b'Bell').else_use(b'3 Gain A').if_parameter(b'3 Filter Type A').has_value(b'High Shelf').else_use(b'3 Resonance A'),
                                  use(b'4 Frequency A').if_parameter(b'4 Filter On A').has_value(b'On'),
                                  use(b'').if_parameter(b'4 Filter On A').has_value(b'Off').else_use(b'4 Gain A').if_parameter(b'4 Filter Type A').has_value(b'Low Shelf').else_use(b'4 Gain A').if_parameter(b'4 Filter Type A').has_value(b'Bell').else_use(b'4 Gain A').if_parameter(b'4 Filter Type A').has_value(b'High Shelf').else_use(b'4 Resonance A'))}),
          (
           b'EQ Band 1',
           {BANK_PARAMETERS_KEY: (
                                  b'1 Filter On A',
                                  use(b'1 Filter Type A').if_parameter(b'1 Filter On A').has_value(b'On'),
                                  use(b'1 Frequency A').if_parameter(b'1 Filter On A').has_value(b'On'),
                                  use(b'1 Gain A').if_parameter(b'1 Filter On A').has_value(b'On'),
                                  use(b'1 Resonance A').if_parameter(b'1 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 2',
           {BANK_PARAMETERS_KEY: (
                                  b'2 Filter On A',
                                  use(b'2 Filter Type A').if_parameter(b'2 Filter On A').has_value(b'On'),
                                  use(b'2 Frequency A').if_parameter(b'2 Filter On A').has_value(b'On'),
                                  use(b'2 Gain A').if_parameter(b'2 Filter On A').has_value(b'On'),
                                  use(b'2 Resonance A').if_parameter(b'2 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 3',
           {BANK_PARAMETERS_KEY: (
                                  b'3 Filter On A',
                                  use(b'3 Filter Type A').if_parameter(b'3 Filter On A').has_value(b'On'),
                                  use(b'3 Frequency A').if_parameter(b'3 Filter On A').has_value(b'On'),
                                  use(b'3 Gain A').if_parameter(b'3 Filter On A').has_value(b'On'),
                                  use(b'3 Resonance A').if_parameter(b'3 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 4',
           {BANK_PARAMETERS_KEY: (
                                  b'4 Filter On A',
                                  use(b'4 Filter Type A').if_parameter(b'4 Filter On A').has_value(b'On'),
                                  use(b'4 Frequency A').if_parameter(b'4 Filter On A').has_value(b'On'),
                                  use(b'4 Gain A').if_parameter(b'4 Filter On A').has_value(b'On'),
                                  use(b'4 Resonance A').if_parameter(b'4 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 5',
           {BANK_PARAMETERS_KEY: (
                                  b'5 Filter On A',
                                  use(b'5 Filter Type A').if_parameter(b'5 Filter On A').has_value(b'On'),
                                  use(b'5 Frequency A').if_parameter(b'5 Filter On A').has_value(b'On'),
                                  use(b'5 Gain A').if_parameter(b'5 Filter On A').has_value(b'On'),
                                  use(b'5 Resonance A').if_parameter(b'5 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 6',
           {BANK_PARAMETERS_KEY: (
                                  b'6 Filter On A',
                                  use(b'6 Filter Type A').if_parameter(b'6 Filter On A').has_value(b'On'),
                                  use(b'6 Frequency A').if_parameter(b'6 Filter On A').has_value(b'On'),
                                  use(b'6 Gain A').if_parameter(b'6 Filter On A').has_value(b'On'),
                                  use(b'6 Resonance A').if_parameter(b'6 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 7',
           {BANK_PARAMETERS_KEY: (
                                  b'7 Filter On A',
                                  use(b'7 Filter Type A').if_parameter(b'7 Filter On A').has_value(b'On'),
                                  use(b'7 Frequency A').if_parameter(b'7 Filter On A').has_value(b'On'),
                                  use(b'7 Gain A').if_parameter(b'7 Filter On A').has_value(b'On'),
                                  use(b'7 Resonance A').if_parameter(b'7 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'EQ Band 8',
           {BANK_PARAMETERS_KEY: (
                                  b'8 Filter On A',
                                  use(b'8 Filter Type A').if_parameter(b'8 Filter On A').has_value(b'On'),
                                  use(b'8 Frequency A').if_parameter(b'8 Filter On A').has_value(b'On'),
                                  use(b'8 Gain A').if_parameter(b'8 Filter On A').has_value(b'On'),
                                  use(b'8 Resonance A').if_parameter(b'8 Filter On A').has_value(b'On'),
                                  b'Adaptive Q', b'Scale', b'Output Gain')}),
          (
           b'8 x Frequency',
           {BANK_PARAMETERS_KEY: (
                                  use(b'1 Frequency A').if_parameter(b'1 Filter On A').has_value(b'On'),
                                  use(b'2 Frequency A').if_parameter(b'2 Filter On A').has_value(b'On'),
                                  use(b'3 Frequency A').if_parameter(b'3 Filter On A').has_value(b'On'),
                                  use(b'4 Frequency A').if_parameter(b'4 Filter On A').has_value(b'On'),
                                  use(b'5 Frequency A').if_parameter(b'5 Filter On A').has_value(b'On'),
                                  use(b'6 Frequency A').if_parameter(b'6 Filter On A').has_value(b'On'),
                                  use(b'7 Frequency A').if_parameter(b'7 Filter On A').has_value(b'On'),
                                  use(b'8 Frequency A').if_parameter(b'8 Filter On A').has_value(b'On'))}),
          (
           b'8 x Gain',
           {BANK_PARAMETERS_KEY: (
                                  use(b'').if_parameter(b'1 Filter On A').has_value(b'Off').else_use(b'1 Gain A').if_parameter(b'1 Filter Type A').has_value(b'Low Shelf').else_use(b'1 Gain A').if_parameter(b'1 Filter Type A').has_value(b'Bell').else_use(b'1 Gain A').if_parameter(b'1 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'2 Filter On A').has_value(b'Off').else_use(b'2 Gain A').if_parameter(b'2 Filter Type A').has_value(b'Low Shelf').else_use(b'2 Gain A').if_parameter(b'2 Filter Type A').has_value(b'Bell').else_use(b'2 Gain A').if_parameter(b'2 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'3 Filter On A').has_value(b'Off').else_use(b'3 Gain A').if_parameter(b'3 Filter Type A').has_value(b'Low Shelf').else_use(b'3 Gain A').if_parameter(b'3 Filter Type A').has_value(b'Bell').else_use(b'3 Gain A').if_parameter(b'3 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'4 Filter On A').has_value(b'Off').else_use(b'4 Gain A').if_parameter(b'4 Filter Type A').has_value(b'Low Shelf').else_use(b'4 Gain A').if_parameter(b'4 Filter Type A').has_value(b'Bell').else_use(b'4 Gain A').if_parameter(b'4 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'5 Filter On A').has_value(b'Off').else_use(b'5 Gain A').if_parameter(b'5 Filter Type A').has_value(b'Low Shelf').else_use(b'5 Gain A').if_parameter(b'5 Filter Type A').has_value(b'Bell').else_use(b'5 Gain A').if_parameter(b'5 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'6 Filter On A').has_value(b'Off').else_use(b'6 Gain A').if_parameter(b'6 Filter Type A').has_value(b'Low Shelf').else_use(b'6 Gain A').if_parameter(b'6 Filter Type A').has_value(b'Bell').else_use(b'6 Gain A').if_parameter(b'6 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'7 Filter On A').has_value(b'Off').else_use(b'7 Gain A').if_parameter(b'7 Filter Type A').has_value(b'Low Shelf').else_use(b'7 Gain A').if_parameter(b'7 Filter Type A').has_value(b'Bell').else_use(b'7 Gain A').if_parameter(b'7 Filter Type A').has_value(b'High Shelf').else_use(b''),
                                  use(b'').if_parameter(b'8 Filter On A').has_value(b'Off').else_use(b'8 Gain A').if_parameter(b'8 Filter Type A').has_value(b'Low Shelf').else_use(b'8 Gain A').if_parameter(b'8 Filter Type A').has_value(b'Bell').else_use(b'8 Gain A').if_parameter(b'8 Filter Type A').has_value(b'High Shelf').else_use(b''))}),
          (
           b'8 x Resonance',
           {BANK_PARAMETERS_KEY: (
                                  b'1 Resonance A', b'2 Resonance A', b'3 Resonance A', b'4 Resonance A',
                                  b'5 Resonance A', b'6 Resonance A', b'7 Resonance A', b'8 Resonance A')}))), 
   b'FilterEQ3': IndexedDict((
                (
                 b'EQ',
                 {BANK_PARAMETERS_KEY: (
                                        b'LowOn', b'MidOn', b'HighOn',
                                        use(b'GainLo').if_parameter(b'LowOn').has_value(b'On'),
                                        use(b'GainMid').if_parameter(b'MidOn').has_value(b'On'),
                                        use(b'GainHi').if_parameter(b'HighOn').has_value(b'On'),
                                        b'FreqLo', b'FreqHi')}),
                (
                 b'Slope',
                 {BANK_PARAMETERS_KEY: (
                                        b'Slope', b'', b'', b'', b'', b'', b'', b'')}))), 
   b'Erosion': IndexedDict((
              (
               BANK_MAIN_KEY,
               {BANK_PARAMETERS_KEY: (
                                      b'Mode', b'Frequency',
                                      use(b'').if_parameter(b'Mode').has_value(b'Sine').else_use(b'Width'),
                                      b'Amount', b'', b'', b'', b'')}),)), 
   b'ProxyAudioEffectDevice': IndexedDict((
                             (
                              BANK_MAIN_KEY,
                              {BANK_PARAMETERS_KEY: (
                                                     b'Input Gain', b'Output Gain', b'Dry/Wet', b'', b'', b'', b'', b'')}),)), 
   b'FilterDelay': IndexedDict((
                  (
                   BANK_MAIN_KEY,
                   {BANK_PARAMETERS_KEY: (
                                          use(b'2 Filter Freq').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'2 Filter Width').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'2 Delay Mode').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'').if_parameter(b'2 Input On').has_value(b'Off').else_use(b'2 Time Delay').if_parameter(b'2 Delay Mode').has_value(b'Off').else_use(b'2 Beat Delay'),
                                          use(b'2 Feedback').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'1 Volume').if_parameter(b'1 Input On').has_value(b'On').else_use(b'2 Pan'),
                                          use(b'2 Volume').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'3 Volume').if_parameter(b'3 Input On').has_value(b'On').else_use(b'Dry'))}),
                  (
                   b'L Filter',
                   {BANK_PARAMETERS_KEY: (
                                          b'1 Input On',
                                          use(b'1 Filter Freq').if_parameter(b'1 Input On').has_value(b'On'),
                                          use(b'1 Filter Width').if_parameter(b'1 Input On').has_value(b'On'),
                                          use(b'1 Feedback').if_parameter(b'1 Input On').has_value(b'On'),
                                          use(b'1 Delay Mode').if_parameter(b'1 Input On').has_value(b'On'),
                                          use(b'').if_parameter(b'1 Input On').has_value(b'Off').else_use(b'1 Time Delay').if_parameter(b'1 Delay Mode').has_value(b'Off').else_use(b'1 Beat Delay'),
                                          use(b'').if_parameter(b'1 Input On').has_value(b'Off').else_use(b'1 Beat Swing').if_parameter(b'1 Delay Mode').has_value(b'On').else_use(b''),
                                          use(b'1 Volume').if_parameter(b'1 Input On').has_value(b'Off'))}),
                  (
                   b'L+R Filter',
                   {BANK_PARAMETERS_KEY: (
                                          b'2 Input On',
                                          use(b'2 Filter Freq').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'2 Filter Width').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'2 Feedback').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'2 Delay Mode').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'').if_parameter(b'2 Input On').has_value(b'Off').else_use(b'2 Time Delay').if_parameter(b'2 Delay Mode').has_value(b'Off').else_use(b'2 Beat Delay'),
                                          use(b'').if_parameter(b'2 Input On').has_value(b'Off').else_use(b'2 Beat Swing').if_parameter(b'2 Delay Mode').has_value(b'On').else_use(b''),
                                          use(b'2 Volume').if_parameter(b'2 Input On').has_value(b'On'))}),
                  (
                   b'R Filter',
                   {BANK_PARAMETERS_KEY: (
                                          b'3 Input On',
                                          use(b'3 Filter Freq').if_parameter(b'3 Input On').has_value(b'On'),
                                          use(b'3 Filter Width').if_parameter(b'3 Input On').has_value(b'On'),
                                          use(b'3 Feedback').if_parameter(b'3 Input On').has_value(b'On'),
                                          use(b'3 Delay Mode').if_parameter(b'3 Input On').has_value(b'On'),
                                          use(b'').if_parameter(b'3 Input On').has_value(b'Off').else_use(b'3 Time Delay').if_parameter(b'3 Delay Mode').has_value(b'Off').else_use(b'3 Beat Delay'),
                                          use(b'').if_parameter(b'3 Input On').has_value(b'Off').else_use(b'3 Beat Swing').if_parameter(b'3 Delay Mode').has_value(b'On').else_use(b''),
                                          use(b'3 Volume').if_parameter(b'3 Input On').has_value(b'On'))}),
                  (
                   b'Mix',
                   {BANK_PARAMETERS_KEY: (
                                          use(b'1 Pan').if_parameter(b'1 Input On').has_value(b'On'),
                                          use(b'2 Pan').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'3 Pan').if_parameter(b'3 Input On').has_value(b'On'),
                                          b'',
                                          use(b'1 Volume').if_parameter(b'1 Input On').has_value(b'On'),
                                          use(b'2 Volume').if_parameter(b'2 Input On').has_value(b'On'),
                                          use(b'3 Volume').if_parameter(b'3 Input On').has_value(b'On'),
                                          b'Dry')}))), 
   b'Flanger': IndexedDict((
              (
               BANK_MAIN_KEY,
               {BANK_PARAMETERS_KEY: (
                                      b'LFO Amount', b'Sync',
                                      use(b'Frequency').if_parameter(b'Sync').has_value(b'Free').else_use(b'Sync Rate'),
                                      b'Delay Time', b'Hi Pass', b'Env. Modulation', b'Feedback', b'Dry/Wet')}),
              (
               b'Envelope',
               {BANK_PARAMETERS_KEY: (
                                      b'Env. Attack', b'Env. Release', b'Env. Modulation', b'Hi Pass',
                                      b'Delay Time', b'Feedback', b'Polarity', b'Dry/Wet')}),
              (
               b'LFO / S&H',
               {BANK_PARAMETERS_KEY: (
                                      b'LFO Amount', b'LFO Waveform', b'Sync',
                                      use(b'Frequency').if_parameter(b'Sync').has_value(b'Free').else_use(b'Sync Rate'),
                                      use(b'').if_parameter(b'LFO Waveform').has_value(b'S&H Width').else_use(b'LFO Stereo Mode').if_parameter(b'Sync').has_value(b'Free').else_use(b'LFO Offset'),
                                      use(b'LFO Width (Random)').if_parameter(b'LFO Waveform').has_value(b'S&H Width').else_use(b'LFO Phase').if_parameter(b'Sync').has_value(b'Sync').else_use(b'LFO Phase').if_parameter(b'LFO Stereo Mode').has_value(b'Phase').else_use(b'LFO Spin'),
                                      b'', b'')}))), 
   b'FrequencyShifter': IndexedDict((
                       (
                        b'FreqDrive',
                        {BANK_PARAMETERS_KEY: (
                                               b'Mode',
                                               use(b'Ring Mod Frequency').if_parameter(b'Mode').has_value(b'Ring Modulation').else_use(b'Coarse'),
                                               b'Wide', b'Fine',
                                               use(b'Drive On/Off').if_parameter(b'Mode').has_value(b'Ring Modulation'),
                                               use(b'Drive').if_parameter(b'Drive On/Off').has_value(b'On').and_parameter(b'Mode').has_value(b'Ring Modulation'),
                                               b'LFO Amount', b'Dry/Wet')}),
                       (
                        b'LFO / S&H',
                        {BANK_PARAMETERS_KEY: (
                                               b'LFO Amount', b'LFO Waveform', b'Sync',
                                               use(b'LFO Frequency').if_parameter(b'Sync').has_value(b'Free').else_use(b'Sync Rate'),
                                               use(b'').if_parameter(b'LFO Waveform').has_value(b'S&H Width').else_use(b'LFO Stereo Mode').if_parameter(b'Sync').has_value(b'Free').else_use(b'LFO Offset'),
                                               use(b'LFO Width (Random)').if_parameter(b'LFO Waveform').has_value(b'S&H Width').else_use(b'LFO Phase').if_parameter(b'Sync').has_value(b'Sync').else_use(b'LFO Phase').if_parameter(b'LFO Stereo Mode').has_value(b'Phase').else_use(b'LFO Spin'),
                                               b'', b'')}))), 
   b'Gate': IndexedDict((
           (
            b'Gate',
            {BANK_PARAMETERS_KEY: (
                                   b'Threshold', b'Return', b'FlipMode', b'LookAhead',
                                   b'Attack', b'Hold', b'Release', b'Floor')}),
           (
            b'Sidechain',
            {BANK_PARAMETERS_KEY: (
                                   b'S/C On',
                                   use(b'S/C Gain').if_parameter(b'S/C On').has_value(b'On'),
                                   use(b'S/C Mix').if_parameter(b'S/C On').has_value(b'On'),
                                   b'S/C Listen', b'S/C EQ On',
                                   use(b'S/C EQ Type').if_parameter(b'S/C EQ On').has_value(b'On'),
                                   use(b'S/C EQ Freq').if_parameter(b'S/C EQ On').has_value(b'On'),
                                   use(b'').if_parameter(b'S/C EQ On').has_value(b'Off').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'Low Shelf').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'High Shelf').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'Bell').else_use(b'S/C EQ Q'))}))), 
   b'GlueCompressor': IndexedDict((
                     (
                      b'Compression',
                      {BANK_PARAMETERS_KEY: (
                                             b'Threshold', b'Ratio', b'Attack', b'Release',
                                             b'Peak Clip In', b'Range', b'Makeup', b'Dry/Wet')}),
                     (
                      b'Sidechain',
                      {BANK_PARAMETERS_KEY: (
                                             b'S/C On',
                                             use(b'S/C Gain').if_parameter(b'S/C On').has_value(b'On'),
                                             use(b'S/C Mix').if_parameter(b'S/C On').has_value(b'On'),
                                             b'', b'S/C EQ On',
                                             use(b'S/C EQ Type').if_parameter(b'S/C EQ On').has_value(b'On'),
                                             use(b'S/C EQ Freq').if_parameter(b'S/C EQ On').has_value(b'On'),
                                             use(b'').if_parameter(b'S/C EQ On').has_value(b'Off').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'Low Shelf').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'High Shelf').else_use(b'S/C EQ Gain').if_parameter(b'S/C EQ Type').has_value(b'Bell').else_use(b'S/C EQ Q'))}))), 
   b'GrainDelay': IndexedDict((
                 (
                  b'Pitch',
                  {BANK_PARAMETERS_KEY: (
                                         b'Frequency', b'Pitch', b'Delay Mode',
                                         use(b'Time Delay').if_parameter(b'Delay Mode').has_value(b'Off').else_use(b'Beat Delay'),
                                         b'Random', b'Spray', b'Feedback', b'DryWet')}),
                 (
                  b'Time',
                  {BANK_PARAMETERS_KEY: (
                                         b'Delay Mode',
                                         use(b'Time Delay').if_parameter(b'Delay Mode').has_value(b'Off').else_use(b'Beat Delay'),
                                         b'Beat Swing', b'Feedback', b'', b'', b'', b'DryWet')}))), 
   b'Limiter': IndexedDict((
              (
               BANK_MAIN_KEY,
               {BANK_PARAMETERS_KEY: (
                                      b'Gain', b'Ceiling', b'Link Channels', b'Lookahead',
                                      b'Auto',
                                      use(b'Release time').if_parameter(b'Auto').has_value(b'Off'),
                                      b'', b'')}),)), 
   b'Looper': IndexedDict((
             (
              BANK_MAIN_KEY,
              {BANK_PARAMETERS_KEY: (
                                     b'State', b'Speed', b'Reverse', b'Quantization',
                                     b'Monitor', b'Song Control', b'Tempo Control', b'Feedback')}),)), 
   b'MultibandDynamics': IndexedDict((
                        (
                         BANK_MAIN_KEY,
                         {BANK_PARAMETERS_KEY: (
                                                use(b'Above Threshold (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Above Ratio (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Above Threshold (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Above Ratio (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Above Threshold (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Above Ratio (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                b'Master Output', b'Amount')}),
                        (
                         b'Low Band',
                         {BANK_PARAMETERS_KEY: (
                                                b'Band Activator (Low)',
                                                use(b'Input Gain (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Below Threshold (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Below Ratio (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Above Threshold (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Above Ratio (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Attack Time (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                use(b'Release Time (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'))}),
                        (
                         b'Mid Band',
                         {BANK_PARAMETERS_KEY: (
                                                b'Band Activator (Mid)',
                                                use(b'Input Gain (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Below Threshold (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Below Ratio (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Above Threshold (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Above Ratio (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Attack Time (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                use(b'Release Time (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'))}),
                        (
                         b'High Band',
                         {BANK_PARAMETERS_KEY: (
                                                b'Band Activator (High)',
                                                use(b'Input Gain (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Below Threshold (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Below Ratio (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Above Threshold (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Above Ratio (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Attack Time (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                use(b'Release Time (High)').if_parameter(b'Band Activator (High)').has_value(b'On'))}),
                        (
                         b'Mix & Split',
                         {BANK_PARAMETERS_KEY: (
                                                use(b'Output Gain (Low)').if_parameter(b'Band Activator (Low)').has_value(b'On'),
                                                b'Low-Mid Crossover',
                                                use(b'Output Gain (Mid)').if_parameter(b'Band Activator (Mid)').has_value(b'On'),
                                                b'Mid-High Crossover',
                                                use(b'Output Gain (High)').if_parameter(b'Band Activator (High)').has_value(b'On'),
                                                b'Peak/RMS Mode', b'Amount', b'Master Output')}),
                        (
                         b'Sidechain',
                         {BANK_PARAMETERS_KEY: (
                                                b'S/C On',
                                                use(b'S/C Mix').if_parameter(b'S/C On').has_value(b'On'),
                                                use(b'S/C Gain').if_parameter(b'S/C On').has_value(b'On'),
                                                b'', b'Time Scaling', b'Soft Knee On/Off', b'', b'')}))), 
   b'Overdrive': IndexedDict((
                (
                 BANK_MAIN_KEY,
                 {BANK_PARAMETERS_KEY: (
                                        b'Filter Freq', b'Filter Width', b'Drive', b'Tone',
                                        b'Preserve Dynamics', b'', b'', b'Dry/Wet')}),)), 
   b'Pedal': IndexedDict((
            (
             b'Global',
             {BANK_PARAMETERS_KEY: (
                                    b'Type', b'Gain', b'Output', b'Bass', b'Mid', b'Treble', b'Sub', b'Dry/Wet')}),
            (
             b'EQ',
             {BANK_PARAMETERS_KEY: (
                                    b'', b'', b'', b'Bass', b'Mid', b'Treble', b'', b'Mid Freq')}))), 
   b'Phaser': IndexedDict((
             (
              BANK_MAIN_KEY,
              {BANK_PARAMETERS_KEY: (
                                     b'Poles', b'Frequency', b'Feedback', b'Env. Modulation',
                                     b'LFO Amount', b'LFO Sync',
                                     use(b'LFO Frequency').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'LFO Sync Rate'),
                                     b'Dry/Wet')}),
             (
              b'Envelope',
              {BANK_PARAMETERS_KEY: (
                                     b'Poles', b'Type',
                                     use(b'').if_parameter(b'Type').has_value(b'Space').else_use(b'Color'),
                                     b'Frequency', b'Feedback', b'Env. Modulation', b'Env. Attack', b'Env. Release')}),
             (
              b'LFO',
              {BANK_PARAMETERS_KEY: (
                                     b'LFO Amount', b'LFO Waveform', b'LFO Sync',
                                     use(b'LFO Frequency').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'LFO Sync Rate'),
                                     use(b'').if_parameter(b'LFO Waveform').has_value(b'S&H Width').else_use(b'LFO Stereo Mode').if_parameter(b'LFO Sync').has_value(b'Free').else_use(b'LFO Offset'),
                                     use(b'LFO Width (Random)').if_parameter(b'LFO Waveform').has_value(b'S&H Width').else_use(b'LFO Phase').if_parameter(b'LFO Sync').has_value(b'Sync').else_use(b'LFO Phase').if_parameter(b'LFO Stereo Mode').has_value(b'Phase').else_use(b'LFO Spin'),
                                     b'', b'')}))), 
   b'Redux': IndexedDict((
            (
             BANK_MAIN_KEY,
             {BANK_PARAMETERS_KEY: (
                                    b'Bit On',
                                    use(b'Bit Depth').if_parameter(b'Bit On').has_value(b'On'),
                                    b'Sample Mode',
                                    use(b'Sample Hard').if_parameter(b'Sample Mode').has_value(b'Hard').else_use(b'Sample Soft'),
                                    b'', b'', b'', b'')}),)), 
   b'Resonator': IndexedDict((
                (
                 BANK_MAIN_KEY,
                 {BANK_PARAMETERS_KEY: (
                                        use(b'Frequency').if_parameter(b'Filter On').has_value(b'On'),
                                        b'Decay', b'Color',
                                        use(b'I Gain').if_parameter(b'I On').has_value(b'On'),
                                        use(b'II Gain').if_parameter(b'II On').has_value(b'On'),
                                        use(b'III Gain').if_parameter(b'III On').has_value(b'On'),
                                        b'Width', b'Dry/Wet')}),
                (
                 b'Global',
                 {BANK_PARAMETERS_KEY: (
                                        b'Mode', b'Decay', b'Const', b'Color',
                                        b'', b'Width', b'Global Gain', b'Dry/Wet')}),
                (
                 b'Filter',
                 {BANK_PARAMETERS_KEY: (
                                        b'Filter On',
                                        use(b'Frequency').if_parameter(b'Filter On').has_value(b'On'),
                                        use(b'Filter Type').if_parameter(b'Filter On').has_value(b'On'),
                                        b'', b'', b'', b'', b'')}),
                (
                 b'Mode I & II',
                 {BANK_PARAMETERS_KEY: (
                                        b'I On',
                                        use(b'I Note').if_parameter(b'I On').has_value(b'On'),
                                        use(b'I Tune').if_parameter(b'I On').has_value(b'On'),
                                        use(b'I Gain').if_parameter(b'I On').has_value(b'On'),
                                        b'II On',
                                        use(b'II Pitch').if_parameter(b'II On').has_value(b'On'),
                                        use(b'II Tune').if_parameter(b'II On').has_value(b'On'),
                                        use(b'II Gain').if_parameter(b'II On').has_value(b'On'))}),
                (
                 b'Mode III & IV',
                 {BANK_PARAMETERS_KEY: (
                                        b'III On',
                                        use(b'III Pitch').if_parameter(b'III On').has_value(b'On'),
                                        use(b'III Tune').if_parameter(b'III On').has_value(b'On'),
                                        use(b'III Gain').if_parameter(b'III On').has_value(b'On'),
                                        b'IV On',
                                        use(b'IV Pitch').if_parameter(b'IV On').has_value(b'On'),
                                        use(b'IV Tune').if_parameter(b'IV On').has_value(b'On'),
                                        use(b'IV Gain').if_parameter(b'IV On').has_value(b'On'))}),
                (
                 b'Mode V',
                 {BANK_PARAMETERS_KEY: (
                                        b'V On',
                                        use(b'V Pitch').if_parameter(b'V On').has_value(b'On'),
                                        use(b'V Tune').if_parameter(b'V On').has_value(b'On'),
                                        use(b'V Gain').if_parameter(b'V On').has_value(b'On'),
                                        b'', b'', b'', b'')}),
                (
                 b'Mix',
                 {BANK_PARAMETERS_KEY: (
                                        use(b'I Gain').if_parameter(b'I On').has_value(b'On'),
                                        use(b'II Gain').if_parameter(b'II On').has_value(b'On'),
                                        use(b'III Gain').if_parameter(b'III On').has_value(b'On'),
                                        use(b'IV Gain').if_parameter(b'IV On').has_value(b'On'),
                                        use(b'V Gain').if_parameter(b'V On').has_value(b'On'),
                                        b'', b'', b'')}),
                (
                 b'Pitch',
                 {BANK_PARAMETERS_KEY: (
                                        use(b'I Note').if_parameter(b'I On').has_value(b'On'),
                                        use(b'II Pitch').if_parameter(b'II On').has_value(b'On'),
                                        use(b'III Pitch').if_parameter(b'III On').has_value(b'On'),
                                        use(b'IV Pitch').if_parameter(b'IV On').has_value(b'On'),
                                        use(b'V Pitch').if_parameter(b'V On').has_value(b'On'),
                                        b'', b'', b'')}))), 
   b'Reverb': IndexedDict((
             (
              BANK_MAIN_KEY,
              {BANK_PARAMETERS_KEY: (
                                     b'PreDelay',
                                     use(b'In Filter Freq').if_parameter(b'In LowCut On').has_value(b'On').else_use(b'ER Shape').if_parameter(b'In HighCut On').has_value(b'Off').else_use(b'In Filter Freq'),
                                     use(b'Chorus Amount').if_parameter(b'Chorus On').has_value(b'On').else_use(b'ER Level'),
                                     b'Stereo Image', b'Room Size', b'DecayTime',
                                     use(b'HiShelf Gain').if_parameter(b'HiShelf On').has_value(b'On').else_use(b'Diffuse Level'),
                                     b'Dry/Wet')}),
             (
              b'Global',
              {BANK_PARAMETERS_KEY: (
                                     b'Chorus On',
                                     use(b'Chorus Rate').if_parameter(b'Chorus On').has_value(b'On'),
                                     use(b'Chorus Amount').if_parameter(b'Chorus On').has_value(b'On'),
                                     b'Quality', b'Freeze On', b'Flat On', b'ER Level', b'Diffuse Level')}),
             (
              b'Diffusion Network',
              {BANK_PARAMETERS_KEY: (
                                     b'HiShelf On',
                                     use(b'HiShelf Freq').if_parameter(b'HiShelf On').has_value(b'On'),
                                     use(b'HiShelf Gain').if_parameter(b'HiShelf On').has_value(b'On'),
                                     b'LowShelf On',
                                     use(b'LowShelf Freq').if_parameter(b'LowShelf On').has_value(b'On'),
                                     use(b'LowShelf Gain').if_parameter(b'LowShelf On').has_value(b'On'),
                                     b'Density', b'Scale')}),
             (
              b'Input/Reflections',
              {BANK_PARAMETERS_KEY: (
                                     b'In LowCut On', b'In HighCut On',
                                     use(b'In Filter Freq').if_parameter(b'In LowCut On').has_value(b'On').else_use(b'').if_parameter(b'In HighCut On').has_value(b'Off').else_use(b'In Filter Freq'),
                                     use(b'In Filter Width').if_parameter(b'In LowCut On').has_value(b'On').else_use(b'').if_parameter(b'In HighCut On').has_value(b'Off').else_use(b'In Filter Width'),
                                     b'ER Spin On',
                                     use(b'ER Spin Rate').if_parameter(b'ER Spin On').has_value(b'On'),
                                     use(b'ER Spin Amount').if_parameter(b'ER Spin On').has_value(b'On'),
                                     b'ER Shape')}))), 
   b'Saturator': IndexedDict((
                (
                 BANK_MAIN_KEY,
                 {BANK_PARAMETERS_KEY: (
                                        b'Drive', b'Type', b'Color',
                                        use(b'Base').if_parameter(b'Color').has_value(b'On'),
                                        use(b'Frequency').if_parameter(b'Color').has_value(b'On'),
                                        use(b'Width').if_parameter(b'Color').has_value(b'On'),
                                        use(b'Depth').if_parameter(b'Color').has_value(b'On'),
                                        b'Output')}),
                (
                 b'Waveshaper',
                 {BANK_PARAMETERS_KEY: (
                                        b'Type',
                                        use(b'WS Drive').if_parameter(b'Type').has_value(b'Waveshaper'),
                                        use(b'WS Curve').if_parameter(b'Type').has_value(b'Waveshaper'),
                                        use(b'WS Depth').if_parameter(b'Type').has_value(b'Waveshaper'),
                                        use(b'WS Lin').if_parameter(b'Type').has_value(b'Waveshaper'),
                                        use(b'WS Damp').if_parameter(b'Type').has_value(b'Waveshaper'),
                                        use(b'WS Period').if_parameter(b'Type').has_value(b'Waveshaper'),
                                        b'Dry/Wet')}),
                (
                 b'Output',
                 {BANK_PARAMETERS_KEY: (
                                        b'', b'', b'', b'', b'', b'Soft Clip', b'Output', b'Dry/Wet')}))), 
   b'StereoGain': IndexedDict((
                 (
                  b'Utility',
                  {BANK_PARAMETERS_KEY: (
                                         use(b'').if_parameter(b'Channel Mode').has_value(b'Right').else_use(b'Left Inv').if_parameter(b'Mute').has_value(b'Off'),
                                         use(b'').if_parameter(b'Channel Mode').has_value(b'Left').else_use(b'Right Inv').if_parameter(b'Mute').has_value(b'Off'),
                                         use(b'Channel Mode').if_parameter(b'Mute').has_value(b'Off'),
                                         use(b'').if_parameter(b'Mute').has_value(b'On').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Left').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Right').else_use(b'').if_parameter(b'Mono').is_available(True).and_parameter(b'Mono').has_value(b'On').else_use(b'Stereo Width').if_parameter(b'Stereo Width').is_available(True).else_use(b'Mid/Side Balance'),
                                         use(b'').if_parameter(b'Mute').has_value(b'On').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Left').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Right').else_use(b'Mono'),
                                         use(b'Balance').if_parameter(b'Mute').has_value(b'Off'),
                                         use(b'').if_parameter(b'Mute').has_value(b'On').else_use(b'Gain').if_parameter(b'Gain').is_available(True).else_use(b'Gain (Legacy)'),
                                         b'Mute')}),
                 (
                  b'Low Freq',
                  {BANK_PARAMETERS_KEY: (
                                         use(b'').if_parameter(b'Mute').has_value(b'On').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Left').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Right').else_use(b'').if_parameter(b'Mono').is_available(True).and_parameter(b'Mono').has_value(b'On').else_use(b'Bass Mono').if_parameter(b'Bass Mono').is_available(True),
                                         use(b'').if_parameter(b'Mute').has_value(b'On').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Left').else_use(b'').if_parameter(b'Channel Mode').has_value(b'Right').else_use(b'').if_parameter(b'Mono').is_available(True).and_parameter(b'Mono').has_value(b'On').else_use(b'Bass Freq').if_parameter(b'Bass Freq').is_available(True),
                                         b'',
                                         use(b'DC Filter').if_parameter(b'Mute').has_value(b'Off'),
                                         b'', b'', b'', b'')}))), 
   b'Vinyl': IndexedDict((
            (
             b'Global',
             {BANK_PARAMETERS_KEY: (
                                    b'Tracing On',
                                    use(b'Tracing Drive').if_parameter(b'Tracing On').has_value(b'On'),
                                    use(b'Tracing Freq.').if_parameter(b'Tracing On').has_value(b'On'),
                                    use(b'Tracing Width').if_parameter(b'Tracing On').has_value(b'On'),
                                    b'Pinch On', b'Global Drive', b'Crackle Density', b'Crackle Volume')}),
            (
             b'Pinch',
             {BANK_PARAMETERS_KEY: (
                                    b'Pinch On',
                                    use(b'Pinch Soft On').if_parameter(b'Pinch On').has_value(b'On'),
                                    use(b'Pinch Mono On').if_parameter(b'Pinch On').has_value(b'On'),
                                    use(b'Pinch Width').if_parameter(b'Pinch On').has_value(b'On'),
                                    use(b'Pinch Drive').if_parameter(b'Pinch On').has_value(b'On'),
                                    use(b'Pinch Freq.').if_parameter(b'Pinch On').has_value(b'On'),
                                    b'Crackle Density', b'Crackle Volume')}))), 
   b'Vocoder': IndexedDict((
              (
               BANK_MAIN_KEY,
               {BANK_PARAMETERS_KEY: (
                                      b'Formant Shift', b'Attack Time', b'Release Time', b'Unvoiced Level',
                                      b'Gate Threshold', b'Filter Bandwidth', b'Envelope Depth', b'Dry/Wet')}),
              (
               b'Carrier',
               {BANK_PARAMETERS_KEY: (
                                      b'Noise Rate', b'Noise Crackle', b'Upper Pitch Detection', b'Lower Pitch Detection',
                                      b'Oscillator Pitch', b'Oscillator Waveform', b'', b'')}),
              (
               b'Global',
               {BANK_PARAMETERS_KEY: (
                                      b'Formant Shift', b'Attack Time', b'Release Time', b'Mono/Stereo',
                                      b'Output Level', b'Gate Threshold', b'Envelope Depth', b'Dry/Wet')}),
              (
               b'Filters/Voicing',
               {BANK_PARAMETERS_KEY: (
                                      b'Filter Bandwidth', b'Upper Filter Band', b'Lower Filter Band', b'Precise/Retro',
                                      b'Unvoiced Level', b'Unvoiced Sensitivity', b'Unvoiced Speed', b'Enhance')})))}
PARAMETERS_BLACKLIST_FOR_CPP_SANITY_CHECK = {b'OriginalSimpler': (
                      b'Start', b'End', b'Sensitivity', b'Mode',
                      b'Playback', b'Pad Slicing', b'Multi Sample', b'Warp',
                      b'Warp Mode', b'Voices', b'Preserve', b'Loop Mode',
                      b'Envelope', b'Grain Size Tones', b'Grain Size Texture',
                      b'Flux', b'Formants', b'Envelope Complex Pro', b'Gain'), 
   b'InstrumentVector': (
                       b'Osc 1 Effect Type', b'Osc 2 Effect Type', b'Osc 1 Table', b'Osc 2 Table',
                       b'Osc 1 Category', b'Osc 2 Category', b'Osc 1 Pitch', b'Osc 2 Pitch',
                       b'Unison Mode', b'Mono On'), 
   b'Delay': (
            b'L Sync Enum', b'R Sync Enum')}