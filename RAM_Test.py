from dataprocessing import *
import math
from ch341_usb_iic import USBI2C
from global_register import *
from time import *
import ux3362s_regs as UX3362S
import ux3320b_reg as UX3320B
import ux3320c_regs as UX3320C
import ux3320t_regs as UX3320T
import ux3320s_regs as UX3320S
import ux3261_regs as UX3261
import ux3262_regs as UX3262
import ux3361_regs as UX3361
import gol

def Test_ram(item=A0_RAM):
    i2c = USBI2C()
    data_ff = []
    data_aa = []
    data_55 = []
    data_00 = []
    flag_t = True
    if item.slaveaddress == 0xA0:
        item.slaveaddress = gol.get_value('gol_A0')
    else:
        item.slaveaddress = gol.get_value('gol_A2')
    for i in range(256):
        data_ff.append(0xFF)
        data_aa.append(0xAA)
        data_55.append(0x55)
        data_00.append(0x00)
    test_data = [data_ff,data_aa,data_55,data_00]
    i2c.write(item.slaveaddress,0x7f,item.table)
    print("Select table : {}".format(item.table))
    for j in test_data:
        if item.name == "Table80h_CTRL_RAM" or item.name == "Table03h_CTRL_RAM":
            reg_csen = item.cs_en - item.startaddress
            reg_sadd = item.slaveaddress_set - item.startaddress
            reg_allwrite = item.all_write - item.startaddress
            reg_pw1 = item.pw1_set - item.startaddress
            reg_pw2 = item.pw2_set - item.startaddress
            j[reg_csen] = j[reg_csen]&item.cs_en_d
            j[reg_sadd] = item.slaveaddress
            j[reg_allwrite] = j[reg_allwrite]&item.all_write_d
            for index in range(4):
                j[reg_pw1+index] = 0xFF
                j[reg_pw2 + index] = 0xFF
        i2c.write_16bytes(item.slaveaddress, item.startaddress, item.length, j)
        sleep(0.1)
        read_data = []
        i2c.read_array(item.slaveaddress, item.startaddress, item.length,read_data)
        for i in range(item.length):
            if read_data[i] != j[i] :
                print(item.name + " Register 0x%02x"%(i+item.startaddress) + " write data 0x%02x"%j[i] + " and read data is 0x%02x"%read_data[i])
                flag_t = False
        if flag_t :
            print(item.name + " Register write data %02x Test.            PASS!!!"%j[i])

def get_chip_id(item):
    i2c = USBI2C()
    item.slaveaddress = gol.get_value('gol_A2')
    regdata = []
    chip_id = ""
    i2c.write(item.slaveaddress,0x7f,item.table)
    print("Select table : {}".format(item.table))
    i2c.read_array(item.slaveaddress,item.register,item.length,regdata)
    for i in regdata:
        chip_id = chip_id + chr(i)
    return chip_id

def ux_chip_diff(item):
    i2c = USBI2C()
    item.slaveaddress = gol.get_value('gol_A2')
    i2c.write(item.slaveaddress,0x7f,item.table)
    print("Select table : {}".format(item.table))
    i2c.write(item.slaveaddress,0x80,0xAA)
    sleep(0.1)
    regdata = i2c.read(item.slaveaddress,0x80)
    if regdata == 0xaa :
        regdata = i2c.read(item.slaveaddress,item.register)
        if regdata == 0xff :
            return "UX3328S"
        else:
            return "UX3320B"
    else:
        return "Unknown chip type !!!"

def RAM_Test(ChipName="null"):
    if ChipName == "UX3362S":
        chip_id = get_chip_id(UX3362S.Chip_ID)
        print("Chip_ID is " + chip_id)
        if chip_id == UX3362S.Const.UX3362S_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3362S.RAM_TEST_UX3362S:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3320B":
        chip_id = ux_chip_diff(UX3320B.Chip_ID)
        print("Chip_ID is " + chip_id)
        if chip_id == UX3320B.Const.UX3320B_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3320B.RAM_TEST_UX3320B:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3320C":
        chip_id = get_chip_id(UX3320C.Chip_ID)
        print("Chip_ID is " + chip_id)
        if chip_id == UX3320C.Const.UX3320C_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3320C.RAM_TEST_UX3320C:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3320T":
        chip_id = get_chip_id(UX3320T.Chip_ID)
        print("Chip_ID is " + chip_id)
        if chip_id == UX3320T.Const.UX3320T_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3320T.RAM_TEST_UX3320T:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3320S":
        chip_id = get_chip_id(UX3320T.Chip_ID)
        print("Chip_ID is " + chip_id)
        if chip_id == UX3320S.Const.UX3320S_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3320S.RAM_TEST_UX3320S:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3261":
        chip_id = get_chip_id(UX3261.Chip_ID)
        print("Chip_ID is " + chip_id)
        print(UX3261.Const.UX3261_Chip_ID)
        print("printf end")
        if chip_id == UX3261.Const.UX3261_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3261.RAM_TEST_UX3261:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3262":
        chip_id = get_chip_id(UX3262.Chip_ID)
        print("Chip_ID is " + chip_id)
        print(UX3262.Const.UX3262_Chip_ID)
        print("printf end")
        if chip_id == UX3262.Const.UX3262_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3262.RAM_TEST_UX3262:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    elif ChipName == "UX3361":
        chip_id = get_chip_id(UX3361.Chip_ID)
        print("Chip_ID is " + chip_id)
        if chip_id == UX3361.Const.UX3361_Chip_ID:
            for i in RAM_Test_8472:
                Test_ram(i)
            for i in UX3361.RAM_TEST_UX3361:
                Test_ram(i)
        else:
            print("Chip ID is error !!!")
    else:
        print("Chip ID is error !!!")

def Show_RAM():
    i2c = USBI2C()
    slaveaddress_a0 = gol.get_value('gol_A0')
    slaveaddress_a2 = gol.get_value('gol_A2')
    data_a0 = []
    i2c.read_array(slaveaddress_a0,0,128,data_a0)
    i2c.read_array(slaveaddress_a0,128, 128, data_a0)
    print("          ",end="")
    for i in range(16):
        print("%02x     |"%i,end=" ")
    print("")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(math.ceil(len(data_a0)/16)):
        data = data_a0[i*16:i*16+16]
        print("0x%02x   :|"%(i*16),end=" ")
        for j in data:
            print("%02x     |"%j,end=" ")
        print("")

if __name__ == '__main__':
    Show_RAM()