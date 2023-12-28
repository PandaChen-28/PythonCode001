import gol
class Const():
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass
    def __setattr__(self, key, value):
        if key in self.__dict__.keys():             # 存在性验证
            raise self.ConstError("Can't change a const variable: '%s'" % key)
        if not key.isupper():                       # 语法规范验证
            raise self.ConstCaseError("Const variable must be combined with upper letters:'%s'" % key)
        self.__dict__[key] = value

class Register():
    def __init__(self):
        self.slaveaddress = slave_add_A2
        self.table = Const.table_controls
        self.register = 0x80
        self.length = 1
        self.default = 0x00
        self.name = "EEPROMIdenfier0"
        self.bitdir = ["-","-","-","-","-","-","-","-"]

class Bit_Ctrl():
    def __init__(self):
        self.slaveaddress = slave_add_A2
        self.table = Const.table_controls
        self.register = 0x82
        self.length = 1
        self.bitnum = 0
        self.bitdir = ["reserved"]

class RAM_Test_Range():
    def __init__(self):
        self.slaveaddress = slave_add_A2
        self.table = Const.table_controls
        self.startaddress = 0x00
        self.endaddress = 0x5f
        self.length = 96
        self.cs_en = 0xb7
        self.cs_en_d = 0xff
        self.all_write = 0xb7
        self.all_write_d = 0xff
        self.pw1_set = 0xFF
        self.pw2_set = 0xFF
        self.slaveaddress_set = 0xd0
        self.name = "A2_Lower_00_5F"

#iic相关参数
slave_add_A2 = 0xA2
slave_add_A0 = 0xA0

#8472协议内容
#监控上报相关
Const.ddmi_temp = 0x60
Const.ddmi_vcc = 0x62
Const.ddmi_bias = 0x64
Const.ddmi_txp = 0x66
Const.ddmi_rxp = 0x68

#选表
Const.table_sel = 0x7f
Const.table_0 = 0x00
Const.table_controls = 0x03
Const.table_controls_ext = 0x84
Const.table_biaslut = 0x04
Const.table_modlut = 0x05
Const.table_apdlut = 0x06
Const.table_apclut = 0x06
Const.table_darkcurrent = 0x07
Const.table_loslut = 0x07
Const.table_rxeqlut = 0x08
Const.table_txpelut = 0x08
Const.table_txamplut = 0x09

#设置相关
PWE_entry = Register()
PWE_entry.register = 0x7b
PWE_entry.length = 4
PWE_entry.name = "Password Entry"

STA_CTRL0 = Register()
STA_CTRL0.register = 0x6e
STA_CTRL0.length = 1
STA_CTRL0.name = "STA_CTRL0"
STA_CTRL0.bitdir = ["Data Ready Bar",
                    "LOS",
                    "TX Fault",
                    "Rogue TXP LOW",
                    "Reserved",
                    "Rogue ONU",
                    "Soft TX Disable Set",
                    "TX Disable State"]

A0_RAM = RAM_Test_Range()
A0_RAM.slaveaddress = slave_add_A0
A0_RAM.startaddress = 0
A0_RAM.endaddress = 0xff
A0_RAM.length = 256
A0_RAM.name = "A0_00_FF"

A2_Lower_RAM = RAM_Test_Range()
A2_Lower_RAM.name = "A2_Lower_00_5F"

A2_Lower_6A_6D = RAM_Test_Range()
A2_Lower_6A_6D.startaddress = 0x6a
A2_Lower_6A_6D.endaddress = 0x6d
A2_Lower_6A_6D.length = 4

A2_Lower_72_73 = RAM_Test_Range()
A2_Lower_72_73.startaddress = 0x72
A2_Lower_72_73.endaddress = 0x73
A2_Lower_72_73.length = 2
A2_Lower_72_73.name = "A2_Lower_72_73"

A2_Lower_76_7A = RAM_Test_Range()
A2_Lower_76_7A.startaddress = 0x76
A2_Lower_76_7A.endaddress = 0x7A
A2_Lower_76_7A.length = 5
A2_Lower_76_7A.name = "A2_Lower_76_7A"

Table0_RAM = RAM_Test_Range()
Table0_RAM.table = Const.table_0
Table0_RAM.startaddress = 0x80
Table0_RAM.endaddress = 0xFF
Table0_RAM.length = 128
Table0_RAM.name = "Table0_80_FF"

RAM_Test_8472 = [A0_RAM,A2_Lower_RAM,A2_Lower_6A_6D,A2_Lower_72_73,A2_Lower_76_7A,Table0_RAM]

# class BIASLUT():
#     def __init__(self):
#         self.saddress = slave_add_A2
#         self.table = Const.table_biaslut
#         self.startaddress = 0x80
#         self.length = 105


if __name__ == '__main__':
    print(Const.ddmi_temp)
    print(Const.ddmi_vcc)
