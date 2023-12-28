from global_register import *

Const.UX3261_Controls = 0x03

Const.UX3261_Chip_ID = "UX3261"

Chip_ID = Register()
Chip_ID.table = 0x09
Chip_ID.register = 0x80
Chip_ID.length = 6
Chip_ID.name = "Chip ID"


RAM_CTRL = RAM_Test_Range()
RAM_CTRL.table = 0x03
RAM_CTRL.startaddress = 0x80
RAM_CTRL.endaddress = 0xD0
RAM_CTRL.length = 81
RAM_CTRL.cs_en = 0x9f
RAM_CTRL.cs_en_d = 0xEF
RAM_CTRL.slaveaddress_set = 0xCE
RAM_CTRL.pw1_set = 0xd1
RAM_CTRL.pw2_set = 0xd5
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

RAM_06H_APC = RAM_Test_Range()
RAM_06H_APC.table = 0x06
RAM_06H_APC.startaddress = 0x80
RAM_06H_APC.endaddress = 0xB1
RAM_06H_APC.length = 50
RAM_06H_APC.name = "Table06h_APCLUT_RAM"

RAM_07H_LOS = RAM_Test_Range()
RAM_07H_LOS.table = 0x07
RAM_07H_LOS.startaddress = 0x80
RAM_07H_LOS.endaddress = 0x94
RAM_07H_LOS.length = 21
RAM_07H_LOS.name = "Table07h_LOSLUT_RAM"

RAM_08H_TXEQRXPE = RAM_Test_Range()
RAM_08H_TXEQRXPE.table = 0x08
RAM_08H_TXEQRXPE.startaddress = 0x80
RAM_08H_TXEQRXPE.endaddress = 0x8E
RAM_08H_TXEQRXPE.length = 15
RAM_08H_TXEQRXPE.name = "Table08h_TXEQRXPELUT_RAM"

RAM_08H_TXEMP = RAM_Test_Range()
RAM_08H_TXEMP.table = 0x08
RAM_08H_TXEMP.startaddress = 0x90
RAM_08H_TXEMP.endaddress = 0x9A
RAM_08H_TXEMP.length = 11
RAM_08H_TXEMP.name = "Table08h_TXEMPLUT_RAM"

RAM_TEST_UX3261 = [RAM_04H_BIAS,RAM_05H_MOD,RAM_06H_APC,RAM_07H_LOS,RAM_08H_TXEQRXPE,RAM_08H_TXEMP,RAM_CTRL]