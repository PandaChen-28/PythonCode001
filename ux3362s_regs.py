from global_register import *

Const.UX3362S_Controls = 0x80
Const.UX3362S_Controls_ext = 0x84
Const.UX3362S_BIASLUT = 0x81
Const.UX3362S_MODLUT = 0x82
Const.UX3362S_APDLUT = 0x83
Const.UX3362S_CHIPID = 0x87

Const.UX3362S_Chip_ID = "UX33630"

PW1_Set = Register()
PW1_Set.table = Const.UX3362S_Controls
PW1_Set.register = 0xE7
PW1_Set.length = 4
PW1_Set.name = "PW1 Settings"

PW2_Set = Register()
PW2_Set.table = Const.UX3362S_Controls
PW2_Set.register = 0xEB
PW2_Set.length = 4
PW2_Set.name = "PW2 Settings"

Security = Register()
Security.table  = Const.UX3362S_Controls
Security.register = 0xfd
Security.length = 1
Security.name = "SYS_STATUS1"
Security.bitdir[1] = "Security[1:0] bit1 00:user; 01:PW1; 10:PW2; 11:Undefined"
Security.bitdir[0] = "Security[1:0] bit0 00:user; 01:PW1; 10:PW2; 11:Undefined"

Bias_lut_en = Bit_Ctrl()
Bias_lut_en.table = Const.UX3362S_Controls
Bias_lut_en.register = 0x83
Bias_lut_en.bitnum = 7
Bias_lut_en.bitdir = ["Set BIAS LUT enable. 0:Disable; 1:Enable."]

Mod_lut_en = Bit_Ctrl()
Mod_lut_en.table = Const.UX3362S_Controls
Mod_lut_en.register = 0x83
Mod_lut_en.bitnum = 6
Mod_lut_en.bitdir = ["Set MOD LUT enable. 0:Disable; 1:Enable."]

TX_Lpow = Bit_Ctrl()
TX_Lpow.table = Const.UX3362S_Controls
TX_Lpow.register = 0x83
TX_Lpow.bitnum = 5
TX_Lpow.bitdir = ["TX Power control bit. 0:Normal; 1:Low power."]

Close_loop = Bit_Ctrl()
Close_loop.table = Const.UX3362S_Controls
Close_loop.register = 0x83
Close_loop.bitnum = 4
Close_loop.bitdir = ["Select the close/open loop mode. 0:Open loop; 1:Close loop."]

TX_Inpolsw = Bit_Ctrl()
TX_Inpolsw.table = Const.UX3362S_Controls
TX_Inpolsw.register = 0x83
TX_Inpolsw.bitnum = 3
TX_Inpolsw.bitdir = ["Select the polarity of the signal channel.0:In-phase; 1:Reverse."]

Bias_max = Register()
Bias_max.table = Const.UX3362S_Controls
Bias_max.register = 0x85
Bias_max.length = 1
Bias_max.name = "BIAS MAX"

Bias_dacc = Register()
Bias_dacc.table = Const.UX3362S_Controls
Bias_dacc.register = 0x86
Bias_dacc.length = 2
Bias_dacc.name = "BIAS DAC Control"

Mod_dacc = Register()
Mod_dacc.table = Const.UX3362S_Controls
Mod_dacc.register = 0x88
Mod_dacc.length = 2
Mod_dacc.name = "MOD DAC Control"

Bias_max_protect = Bit_Ctrl()
Bias_max_protect.table = Const.UX3362S_Controls
Bias_max_protect.register = 0x8A
Bias_max_protect.bitnum = 5
Bias_max_protect.bitdir = ["The protection function of bias over-current. 0:Disable; 1:Enable."]

Burst_Continuous = Bit_Ctrl()
Burst_Continuous.table = Const.UX3362S_Controls
Burst_Continuous.register = 0x8B
Burst_Continuous.bitnum = 7
Burst_Continuous.bitdir = ["Set the operating mode of LDD. 0:Burst mode; 1:Continuous mode."]

Start_en = Bit_Ctrl()
Start_en.table = Const.UX3362S_Controls
Start_en.register = 0x9D
Start_en.bitnum = 1
Start_en.bitdir = ["APC circuit enable bit. 0:Disable; 1:Enable"]

BEN_pch = Bit_Ctrl()
BEN_pch.table = Const.UX3362S_Controls
BEN_pch.register = 0x8B
BEN_pch.bitnum = 2
BEN_pch.bitdir = ["Select the polarity of the BEN signal. 0:In-phase; 1:Reverse"]

Fault_CTRL = Register()
Fault_CTRL.table = Const.UX3362S_Controls
Fault_CTRL.register = 0x8C
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
PA_Set.table = Const.UX3362S_Controls
PA_Set.register = 0x8D
PA_Set.length = 2
PA_Set.name = "PA Control"

NTX_PD = Bit_Ctrl()
NTX_PD.table = Const.UX3362S_Controls
NTX_PD.register = 0x8F
NTX_PD.bitnum = 7
NTX_PD.bitdir = "TX not PD mode."

TXD0_sleep1 = Bit_Ctrl()
TXD0_sleep1.table = Const.UX3362S_Controls
TXD0_sleep1.register = 0x92
TXD0_sleep1.bitnum = 4
TXD0_sleep1.bitdir = ["Multiplexing control of pin 9."]

TX_PD = Register()
TX_PD.table = Const.UX3362S_Controls
TX_PD.register = 0x93
TX_PD.length = 2
TX_PD.name = "TX not PD mod TX Power Value."

In_Ext = Bit_Ctrl()
In_Ext.table = Const.UX3362S_Controls
In_Ext.register = 0xE5
In_Ext.bitnum = 6
In_Ext.bitdir = "Set to enable the internal calibration."

Debug_en = Bit_Ctrl()
Debug_en.table = Const.UX3362S_Controls
Debug_en.register = 0xE5
Debug_en.bitnum = 5
Debug_en.bitdir = "Debug mode enable."

Fault_state = Register()
Fault_state.table = Const.UX3362S_Controls
Fault_state.register = 0xEF
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
BiasCT_R.table = Const.UX3362S_Controls
BiasCT_R.register = 0xF0
BiasCT_R.length = 2
BiasCT_R.name = "BIAS Current DA"

IMOD_DAC = Register()
IMOD_DAC.table = Const.UX3362S_Controls
IMOD_DAC.register = 0xF2
IMOD_DAC.length = 2
IMOD_DAC.name = "MOD Current DA"

BIAS_LUT_Status = Register()
BIAS_LUT_Status.table = Const.UX3362S_BIASLUT
BIAS_LUT_Status.register = 0xe9
BIAS_LUT_Status.length = 2
BIAS_LUT_Status.name = "BIAS TLUT index current DA"

MOD_LUT_Status = Register()
MOD_LUT_Status.table = Const.UX3362S_MODLUT
MOD_LUT_Status.register = 0xe9
MOD_LUT_Status.length = 2
MOD_LUT_Status.name = "MOD TLUT index current DA"

APD_DAC_S = Register()
APD_DAC_S.table = Const.UX3362S_APDLUT
APD_DAC_S.register = 0xe9
APD_DAC_S.length = 2
APD_DAC_S.name = "APD Current DA"

Sys_status = Register()
Sys_status.table = Const.UX3362S_Controls
Sys_status.register = 0xF4
Sys_status.length = 1
Sys_status.name = "STATUS"
Sys_status.bitdir = ["ROP_STATE0",
                     "ROP_STATE1",
                     "TX_STATE",
                     "LA_STATE",
                     "DA_STATE",
                     "DCDC_STATE",
                     "TXP_CLR",
                     "TXP_CLR1"
                     ]

Temp_adc = Register()
Temp_adc.table = Const.UX3362S_Controls
Temp_adc.register = 0xF7
Temp_adc.length = 2
Temp_adc.name = "Temp ADC"

RX_ADC_Value = Register()
RX_ADC_Value.table = Const.UX3362S_Controls
RX_ADC_Value.register = 0xF9
RX_ADC_Value.length = 2
RX_ADC_Value.name = "RX ADC Value"

APD_VOL = Register()
APD_VOL.table = Const.UX3362S_Controls
APD_VOL.register = 0xFB
APD_VOL.length = 2
APD_VOL.name = "APD_VOL"

Debug_data = Register()
Debug_data.table = Const.UX3362S_CHIPID
Debug_data.register = 0x87
Debug_data.length = 2
Debug_data.name = "Debug data."

Chip_ID = Register()
Chip_ID.table = Const.UX3362S_CHIPID
Chip_ID.register = 0x80
Chip_ID.length = 7
Chip_ID.name = "Chip ID"

RAM_CTRL = RAM_Test_Range()
RAM_CTRL.table = 0x80
RAM_CTRL.startaddress = 0x80
RAM_CTRL.endaddress = 0xE6
RAM_CTRL.length = 103
RAM_CTRL.cs_en = 0xB7
RAM_CTRL.cs_en_d = 0xbf
RAM_CTRL.all_write = 0xb7
RAM_CTRL.all_write_d = 0x7f
RAM_CTRL.slaveaddress_set = 0xE4
RAM_CTRL.name = "Table80h_CTRL_RAM"

RAM_81H_BIAS = RAM_Test_Range()
RAM_81H_BIAS.table = 0x81
RAM_81H_BIAS.startaddress = 0x80
RAM_81H_BIAS.endaddress = 0xE8
RAM_81H_BIAS.length = 105
RAM_81H_BIAS.name = "Table81h_BIASLUT_RAM"

RAM_82H_MOD = RAM_Test_Range()
RAM_82H_MOD.table = 0x82
RAM_82H_MOD.startaddress = 0x80
RAM_82H_MOD.endaddress = 0xE8
RAM_82H_MOD.length = 105
RAM_82H_MOD.name = "Table82h_MODLUT_RAM"

RAM_83H_APD = RAM_Test_Range()
RAM_83H_APD.table = 0x83
RAM_83H_APD.startaddress = 0x80
RAM_83H_APD.endaddress = 0xE8
RAM_83H_APD.length = 105
RAM_83H_APD.name = "Table83h__APDLUT_RAM"

RAM_84H_APC = RAM_Test_Range()
RAM_84H_APC.table = 0x84
RAM_84H_APC.startaddress = 0x80
RAM_84H_APC.endaddress = 0xD3
RAM_84H_APC.length = 84
RAM_84H_APC.name = "Table84h_APC_RAM"

RAM_84H_TXEQ = RAM_Test_Range()
RAM_84H_TXEQ.table = 0x84
RAM_84H_TXEQ.startaddress = 0xD6
RAM_84H_TXEQ.endaddress = 0xDD
RAM_84H_TXEQ.length = 8
RAM_84H_TXEQ.name = "Table84h_TXEQ_RAM"

RAM_84H_CTRL = RAM_Test_Range()
RAM_84H_CTRL.table = 0x84
RAM_84H_CTRL.startaddress = 0xE0
RAM_84H_CTRL.endaddress = 0xEA
RAM_84H_CTRL.length = 11
RAM_84H_CTRL.name = "Table84h_CTRL_RAM"

RAM_85H_DarkC = RAM_Test_Range()
RAM_85H_DarkC.table = 0x85
RAM_85H_DarkC.startaddress = 0x80
RAM_85H_DarkC.endaddress = 0x94
RAM_85H_DarkC.length = 21
RAM_85H_DarkC.name = "Table85h_DarkCurrentLUT_RAM"

RAM_85H_RXEQ = RAM_Test_Range()
RAM_85H_RXEQ.table = 0x85
RAM_85H_RXEQ.startaddress = 0xA0
RAM_85H_RXEQ.endaddress = 0xAA
RAM_85H_RXEQ.length = 11
RAM_85H_RXEQ.name = "Table85h_RXEQLUT_RAM"

RAM_85H_RXPE = RAM_Test_Range()
RAM_85H_RXPE.table = 0x85
RAM_85H_RXPE.startaddress = 0xB0
RAM_85H_RXPE.endaddress = 0xB7
RAM_85H_RXPE.length = 8
RAM_85H_RXPE.name = "Table85h_RXPELUT_RAM"

RAM_85H_LOS = RAM_Test_Range()
RAM_85H_LOS.table = 0x85
RAM_85H_LOS.startaddress = 0xC0
RAM_85H_LOS.endaddress = 0xD4
RAM_85H_LOS.length = 21
RAM_85H_LOS.name = "Table85h_LOSLUT_RAM"

RAM_86H_TXEMP = RAM_Test_Range()
RAM_86H_TXEMP.table = 0x86
RAM_86H_TXEMP.startaddress = 0x80
RAM_86H_TXEMP.endaddress = 0xA9
RAM_86H_TXEMP.length = 42
RAM_86H_TXEMP.name = "Table86h_TXEMPLUT_RAM"

RAM_TEST_UX3362S = [RAM_CTRL,RAM_81H_BIAS,RAM_82H_MOD,RAM_83H_APD,RAM_84H_APC,RAM_84H_TXEQ,RAM_84H_CTRL,
                  RAM_85H_DarkC,RAM_85H_RXEQ,RAM_85H_RXPE,RAM_85H_LOS,RAM_86H_TXEMP]