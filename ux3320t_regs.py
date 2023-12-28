from global_register import *

Const.UX3320T_Controls = 0x03

Const.UX3320T_Chip_ID = "UX3320S1"

PW1_Set = Register()
PW1_Set.table = Const.UX3320T_Controls
PW1_Set.register = 0xd3
PW1_Set.length = 4
PW1_Set.name = "PW1 Settings"

PW2_Set = Register()
PW2_Set.table = Const.UX3320T_Controls
PW2_Set.register = 0xd7
PW2_Set.length = 4
PW2_Set.name = "PW2 Settings"

Security = Register()
Security.table  = Const.UX3320T_Controls
Security.register = 0xef
Security.length = 1
Security.name = "SYS_STATUS1"
Security.bitdir[1] = "Security[1:0] bit1 00:user; 01:PW1; 10:PW2; 11:Undefined"
Security.bitdir[0] = "Security[1:0] bit0 00:user; 01:PW1; 10:PW2; 11:Undefined"

Bias_lut_en = Bit_Ctrl()
Bias_lut_en.table = Const.UX3320T_Controls
Bias_lut_en.register = 0x82
Bias_lut_en.bitnum = 7
Bias_lut_en.bitdir = ["Set BIAS LUT enable. 0:Disable; 1:Enable."]

Mod_lut_en = Bit_Ctrl()
Mod_lut_en.table = Const.UX3320T_Controls
Mod_lut_en.register = 0x82
Mod_lut_en.bitnum = 6
Mod_lut_en.bitdir = ["Set MOD LUT enable. 0:Disable; 1:Enable."]

TX_Lpow = Bit_Ctrl()
TX_Lpow.table = Const.UX3320T_Controls
TX_Lpow.register = 0x82
TX_Lpow.bitnum = 5
TX_Lpow.bitdir = ["TX Power control bit. 0:Normal; 1:Low power."]

Close_loop = Bit_Ctrl()
Close_loop.table = Const.UX3320T_Controls
Close_loop.register = 0x82
Close_loop.bitnum = 3
Close_loop.bitdir = ["Select the close/open loop mode. 0:Open loop; 1:Close loop."]

TX_Inpolsw = Bit_Ctrl()
TX_Inpolsw.table = Const.UX3320T_Controls
TX_Inpolsw.register = 0x82
TX_Inpolsw.bitnum = 2
TX_Inpolsw.bitdir = ["Select the polarity of the signal channel.0:In-phase; 1:Reverse."]

Bias_max = Register()
Bias_max.table = Const.UX3320T_Controls
Bias_max.register = 0x84
Bias_max.length = 1
Bias_max.name = "BIAS MAX"

Bias_dacc = Register()
Bias_dacc.table = Const.UX3320T_Controls
Bias_dacc.register = 0x85
Bias_dacc.length = 2
Bias_dacc.name = "BIAS DAC Control"

Mod_dacc = Register()
Mod_dacc.table = Const.UX3320T_Controls
Mod_dacc.register = 0x87
Mod_dacc.length = 2
Mod_dacc.name = "MOD DAC Control"

Bias_max_protect = Bit_Ctrl()
Bias_max_protect.table = Const.UX3320T_Controls
Bias_max_protect.register = 0x89
Bias_max_protect.bitnum = 7
Bias_max_protect.bitdir = ["The protection function of bias over-current. 0:Disable; 1:Enable."]

Burst_Continuous = Bit_Ctrl()
Burst_Continuous.table = Const.UX3320T_Controls
Burst_Continuous.register = 0x8a
Burst_Continuous.bitnum = 7
Burst_Continuous.bitdir = ["Set the operating mode of LDD. 0:Burst mode; 1:Continuous mode."]

Start_en = Bit_Ctrl()
Start_en.table = Const.UX3320T_Controls
Start_en.register = 0x8a
Start_en.bitnum = 2
Start_en.bitdir = ["APC circuit enable bit. 0:Disable; 1:Enable"]

BEN_pch = Bit_Ctrl()
BEN_pch.table = Const.UX3320T_Controls
BEN_pch.register = 0x8a
BEN_pch.bitnum = 1
BEN_pch.bitdir = ["Select the polarity of the BEN signal. 0:In-phase; 1:Reverse"]

Fault_CTRL = Register()
Fault_CTRL.table = Const.UX3320T_Controls
Fault_CTRL.register = 0x8b
Fault_CTRL.length = 1
Fault_CTRL.name = "Fault Controls."
Fault_CTRL.bitdir = ["Fault polarity.0:High level alarm;1:Low level alram.",
                     "Reserved.",
                     "Rogue ONU is detected.",
                     "BIAS >= BIASMAX",
                     "BIASP short to ground.",
                     "LDOP or LDON short to ground.",
                     "Whether internal current source is working properly.",
                     "VDD>4.3V or VDD<2.5V."]

PA_Set = Register()
PA_Set.table = Const.UX3320T_Controls
PA_Set.register = 0x8c
PA_Set.length = 2
PA_Set.name = "PA Control"

NTX_PD = Bit_Ctrl()
NTX_PD.table = Const.UX3320T_Controls
NTX_PD.register = 0x8e
NTX_PD.bitnum = 7
NTX_PD.bitdir = "TX not PD mode."

TXD0_sleep1 = Bit_Ctrl()
TXD0_sleep1.table = Const.UX3320T_Controls
TXD0_sleep1.register = 0x91
TXD0_sleep1.bitnum = 4
TXD0_sleep1.bitdir = ["Multiplexing control of pin 9."]

TX_PD = Register()
TX_PD.table = Const.UX3320T_Controls
TX_PD.register = 0x92
TX_PD.length = 2
TX_PD.name = "TX not PD mod TX Power Value."

In_Ext = Bit_Ctrl()
In_Ext.table = Const.UX3320T_Controls
In_Ext.register = 0xd1
In_Ext.bitnum = 6
In_Ext.bitdir = "Set to enable the internal calibration."

Debug_en = Bit_Ctrl()
Debug_en.table = Const.UX3320T_Controls
Debug_en.register = 0xD1
Debug_en.bitnum = 5
Debug_en.bitdir = "Debug mode enable."

Fault_state = Register()
Fault_state.table = Const.UX3320T_Controls
Fault_state.register = 0xdd
Fault_state.length = 1
Fault_state.name = "Fault status"
Fault_state.bitdir = ["Reserved.",
                     "Reserved.",
                     "Rogue ONU is detected.",
                     "BIAS >= BIASMAX",
                     "BIASP short to ground.",
                     "LDOP or LDON short to ground.",
                     "Whether internal current source is working properly.",
                     "VDD>4.3V or VDD<2.5V."]

BiasCT_R = Register()
BiasCT_R.table = Const.UX3320T_Controls
BiasCT_R.register = 0xde
BiasCT_R.length = 2
BiasCT_R.name = "BIAS Current DA"

IMOD_DAC = Register()
IMOD_DAC.table = Const.UX3320T_Controls
IMOD_DAC.register = 0xe0
IMOD_DAC.length = 2
IMOD_DAC.name = "MOD Current DA"

BIAS_LUT_Status = Register()
BIAS_LUT_Status.table = Const.UX3320T_Controls
BIAS_LUT_Status.register = 0xe2
BIAS_LUT_Status.length = 2
BIAS_LUT_Status.name = "BIAS TLUT index current DA"

MOD_LUT_Status = Register()
MOD_LUT_Status.table = Const.UX3320T_Controls
MOD_LUT_Status.register = 0xe4
MOD_LUT_Status.length = 2
MOD_LUT_Status.name = "MOD TLUT index current DA"

APD_DAC_S = Register()
APD_DAC_S.table = Const.UX3320T_Controls
APD_DAC_S.register = 0xe6
APD_DAC_S.length = 2
APD_DAC_S.name = "APD Current DA"

Sys_status = Register()
Sys_status.table = Const.UX3320T_Controls
Sys_status.register = 0xe8
Sys_status.length = 1
Sys_status.name = "STATUS"
Sys_status.bitdir = ["Reserved",
                     "TXP_CLR1",
                     "TXP_CLR",
                     "DA_STATE",
                     "LA_STATE",
                     "TX_STATE",
                     "ROP_STATE1",
                     "ROP_STATE0"]

Temp_adc = Register()
Temp_adc.table = Const.UX3320T_Controls
Temp_adc.register = 0xe9
Temp_adc.length = 2
Temp_adc.name = "Temp ADC"

RX_ADC_Value = Register()
RX_ADC_Value.table = Const.UX3320T_Controls
RX_ADC_Value.register = 0xeb
RX_ADC_Value.length = 2
RX_ADC_Value.name = "RX ADC Value"

Debug_data = Register()
Debug_data.table = Const.UX3320T_Controls
Debug_data.register = 0xed
Debug_data.length = 2
Debug_data.name = "Debug data."

TX_ADC_Value = Register()
TX_ADC_Value.table = Const.UX3320T_Controls
TX_ADC_Value.register = 0xf3
TX_ADC_Value.length = 2
TX_ADC_Value.name = "TX ADC Value"

Chip_ID = Register()
Chip_ID.table = Const.UX3320T_Controls
Chip_ID.register = 0xf5
Chip_ID.length = 8
Chip_ID.name = "Chip ID"

RAM_CTRL = RAM_Test_Range()
RAM_CTRL.table = 0x03
RAM_CTRL.startaddress = 0x80
RAM_CTRL.endaddress = 0xD2
RAM_CTRL.length = 83
RAM_CTRL.cs_en = 0xA2
RAM_CTRL.cs_en_d = 0xEF
RAM_CTRL.slaveaddress_set = 0xD0
RAM_CTRL.pw1_set = 0xD3
RAM_CTRL.pw2_set = 0xD7
RAM_CTRL.name = "Table03h_CTRL_RAM"

RAM_04H_BIAS = RAM_Test_Range()
RAM_04H_BIAS.table = 0x04
RAM_04H_BIAS.startaddress = 0x80
RAM_04H_BIAS.endaddress = 0xE8
RAM_04H_BIAS.length = 105
RAM_04H_BIAS.name = "Table04h_BIASLUT_RAM"

RAM_05H_MOD = RAM_Test_Range()
RAM_05H_MOD.table = 0x05
RAM_05H_MOD.startaddress = 0x80
RAM_05H_MOD.endaddress = 0xE8
RAM_05H_MOD.length = 105
RAM_05H_MOD.name = "Table05h_MODLUT_RAM"

RAM_06H_APD = RAM_Test_Range()
RAM_06H_APD.table = 0x06
RAM_06H_APD.startaddress = 0x80
RAM_06H_APD.endaddress = 0xE8
RAM_06H_APD.length = 105
RAM_06H_APD.name = "Table06h_APDLUT_RAM"

RAM_TEST_UX3320T = [RAM_04H_BIAS,RAM_05H_MOD,RAM_06H_APD,RAM_CTRL]
