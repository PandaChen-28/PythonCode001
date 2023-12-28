import re #导入正则表达式模块
import os #导入操作系统模块
import global_register as gl
from RAM_Test import *
from Tools import *
from ch341_usb_iic import USBI2C
from ddmi_read import *
import gol



def menu():
    print("""
    ╔----------------UX Chip I2C Test menu----------------╗
    |    ============ Feature selection ============      |
    |    1:I2C Rate select.                               |
    |    2:search slave address.                          |
    |    3:RAM test.                                      |
    |    4:Modify the slave address.                      |
    |    5:Show DDMI Value                                |
    |    6:Show RAM data.                                 |
    |                                                     |
    |                                                     |
    ╚-----------------------------------------------------╝
    """)
def main():
    gol._init()
    gol.set_value('gol_A2',0xA2)
    gol.set_value('gol_A0',0xA0)
    ctrl = True
    while(ctrl):
        menu()
        option = input("Please enter your choice :")
        option_str = re.sub("\D","",option)
        if option_str in ['1','2','3','4','5','6']:
            option_int = int(option_str)
            if option_int == 1:
                i2c_rate_sel()
            elif option_int == 2:
                search_slave_address()
            elif option_int == 3:
                RAM_Test_ChipID()
            elif option_int == 4:
                print("Current slave_add_A2:{}".format(gol.get_value('gol_A2')))
                print("Current slave_add_A0:{}".format(gol.get_value('gol_A0')))
                slave_addr_str = input("Please input the new salve address value:")
                slave_addr_str = re.sub("\D","",slave_addr_str)
                slave_addr_int = int(slave_addr_str)
                gol.set_value('gol_A2', slave_addr_int&0xFE)
                gol.set_value('gol_A0', slave_addr_int&0xFC)
                print("Current slave_add_A2:{}".format(gol.get_value('gol_A2')))
                print("Current slave_add_A0:{}".format(gol.get_value('gol_A0')))
                input("Press Enter to return to the home page.")
            elif option_int == 5:
                ddm = ddmi_read("ddm")
                print("Temperature  :       {}℃".format(ddm['temp']))
                print("Voltage      :       {}V".format(ddm['vcc']))
                print("BIAS Current :       {}mA".format(ddm['ibias']))
                print("TX Power     :       {}dbm".format(ddm['txp']))
                print("RX Power     :       {}dbm".format(ddm['rxp']))
                input("Press Enter to return to the home page.")
            elif option_int == 6:
                Show_RAM()
                input("Press Enter to return to the home page.")


def i2c_rate_sel():
    i2c = USBI2C()
    print('''
    ==============================
    Rate selection:
                    0:20kHz
                    1:100kHz
                    2:400kHz
                    3:750kHz
    ==============================
    ''')
    rate_sel = input("Please enter the rate number:")
    rate_sel = re.sub("\D","",rate_sel)
    if rate_sel in ['0','1','2','3',]:
        if rate_sel == '0':
            flag = i2c.rate_sel("20kHz")
            if flag == 1:
                print("Set I2C clock rate 20kHz success!")
        elif rate_sel == '1':
            flag = i2c.rate_sel("100kHz")
            if flag == 1:
                print("Set I2C clock rate 100kHz success!")
        elif rate_sel == '2':
            flag = i2c.rate_sel("400kHz")
            if flag == 1:
                print("Set I2C clock rate 400kHz success!")
        elif rate_sel == '3':
            flag = i2c.rate_sel("750kHz")
            if flag == 1:
                print("Set I2C clock rate 750kHz success!")
    else:
        print("Rate number is undefined !!!")
        sleep(3)
    input("Press Enter to return to the home page.")

def search_slave_address():
    i2c = USBI2C()
    checkreg = input("Please enter a register address that can be confirmed:")
    checkreg_str = re.sub("\D","",checkreg)
    checkreg = int(checkreg_str)
    if checkreg in range(256):
        print("Searching ...")
        slaveaddr = search_slaveaddress(checkreg)
        print("The responding slave address is found:{}".format(slaveaddr))
    input("Press Enter to return to the home page.")

def RAM_Test_ChipID():
    print('''
    The current version supports chip ID:
    UX3320B     UX3320C     UX3320S     UX3320T
    UX3362S     UX3261      UX3262      UX3361
    
    ''')
    chipid = input("Please enter the chip name(exp:UX3320B):")
    RAM_Test(chipid)
    input("Press Enter to return to the home page.")
if __name__ == "__main__":
    main()