from ch341_usb_iic import USBI2C

def search_slaveaddress(checkreg):
    i2c = USBI2C()
    addr = []
    for i in range(128):
        i2c.write(i*2,checkreg,1)
        data = i2c.read(i*2,checkreg)
        if data == 1:
            addr.append(hex(i*2))
    return addr

if __name__ == '__main__':
    slave_add = search_slaveaddress(0x00)
    print(slave_add)