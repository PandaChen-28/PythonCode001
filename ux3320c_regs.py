from global_register import *

Const.UX3320C_Controls = 0x03

Const.UX3320C_Chip_ID = "UX3320C"

Chip_ID = Register()
Chip_ID.table = Const.UX3320C_Controls
Chip_ID.register = 0xF3
Chip_ID.length = 7
Chip_ID.name = "Chip ID"


RAM_CTRL = RAM_Test_Range()
RAM_CTRL.table = 0x03
RAM_CTRL.startaddress = 0x80
RAM_CTRL.endaddress = 0xD2
RAM_CTRL.length = 83
RAM_CTRL.cs_en = 0xA2
RAM_CTRL.cs_en_d = 0xEF
RAM_CTRL.slaveaddress_set = 0xD0
RAM_CTRL.pw1_set = 0xd4
RAM_CTRL.pw2_set = 0xd8
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

RAM_TEST_UX3320C = [RAM_04H_BIAS,RAM_05H_MOD,RAM_06H_APD,RAM_CTRL]