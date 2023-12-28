from dataprocessing import *
from ch341_usb_iic import USBI2C
from global_register import *
from time import *
import gol
import ux3320t_regs as UX3320T

def ddmi_read(item):
    slave_add_A2 = gol.get_value('gol_A2')
    i2c = USBI2C()
    adcreg = []
    if item == "temp":
        i2c.read_array(slave_add_A2,Const.ddmi_temp,2,adcreg)
        tempadc = adc2temp(adcreg)
        return tempadc
    elif item == "vcc":
        i2c.read_array(slave_add_A2, Const.ddmi_vcc, 2, adcreg)
        vccadc = adc2vcc(adcreg)
        return vccadc
    elif item == "bias":
        i2c.read_array(slave_add_A2, Const.ddmi_bias, 2, adcreg)
        biasadc = adc2current(adcreg)
        return biasadc
    elif item == "txpower":
        i2c.read_array(slave_add_A2, Const.ddmi_txp, 2, adcreg)
        txadc = adc2dbm(adcreg)
        return txadc
    elif item == "rxpower":
        i2c.read_array(slave_add_A2, Const.ddmi_rxp, 2, adcreg)
        rxadc = adc2dbm(adcreg)
        return rxadc
    elif item == "ddm":
        i2c.read_array(slave_add_A2,Const.ddmi_temp,10,adcreg)
        ddmi = adc2ddm(adcreg)
        return ddmi
    else:
        return "item error,calibration failed!!!"

def entry_PWE(PWE):
    i2c = USBI2C()
    i2c.write_array(PWE_entry.slaveaddress,PWE_entry.register,PWE_entry.length,PWE)
    security = []
    i2c.write(UX3320T.Security.slaveaddress,0x7f,UX3320T.Security.table)
    i2c.read_array(UX3320T.Security.slaveaddress,UX3320T.Security.register,UX3320T.Security.length,security)
    print(security)
    return security

if __name__ == '__main__':
    mytest_temp = ddmi_read('vcc')
    print(mytest_temp)
    ddmi_test = ddmi_read('ddm')
    print(ddmi_test)
    PWE_TEST = [0xff,0xff,0xff,0xff]
    S_TEST = entry_PWE(PWE_TEST)
    print(S_TEST)