#coding=utf-8
import os
import math
from ctypes import *
from time import *

class USBI2C():
    os.add_dll_directory(os.path.dirname(os.path.realpath(__file__)))
    ch341 = windll.LoadLibrary("CH341DLL.DLL")

    def __init__(self, usb_dev=0):
        self.usb_id = usb_dev
        if USBI2C.ch341.CH341OpenDevice(self.usb_id) != 1:
            USBI2C.ch341.CH341SetStream(self.usb_id, 0x82)
            USBI2C.ch341.CH341CloseDevice(self.usb_id)
        else:
            print("USB CH341 Open Failed!")

    def rate_sel(self,rate):
        if USBI2C.ch341.CH341OpenDevice(self.usb_id) != -1:
            if rate == "20kHz":
                mode = 0
            elif rate == "100kHz":
                mode = 1
            elif rate == "400kHz":
                mode = 2
            elif rate == "750kHz":
                mode = 3
            else:
                mode = 1
            USBI2C.ch341.CH341SetStream(self.usb_id,mode)
            USBI2C.ch341.CH341CloseDevice(self.usb_id)
            return 1
        else:
            print("USB CH341 Open Failed!")
            return 0

    def read(self, slaveaddr, regaddr):
        if USBI2C.ch341.CH341OpenDevice(self.usb_id) != -1:
            obuf = (c_byte * 2)()
            ibuf = (c_byte * 1)()
            obuf[0] = slaveaddr
            obuf[1] = regaddr
            USBI2C.ch341.CH341StreamI2C(self.usb_id, 2, obuf, 1, ibuf)
            USBI2C.ch341.CH341CloseDevice(self.usb_id)
            return ibuf[0] & 0xFF
        else:
            print("USB CH341 Open Failed!")
            return 0

    def read_array(self, slaveaddr, regaddr, num, readdata):
        if USBI2C.ch341.CH341OpenDevice(self.usb_id) != -1:
            obuf = (c_byte * 2)()
            ibuf = (c_byte * num)()
            obuf[0] = slaveaddr
            obuf[1] = regaddr
            USBI2C.ch341.CH341StreamI2C(self.usb_id, 2, obuf, num, ibuf)
            USBI2C.ch341.CH341CloseDevice(self.usb_id)
            for i in range(num):
                readdata.append(ibuf[i] & 0xFF)
        else:
            print("USB CH341 Open Failed!")

    def write(self, slaveaddr, regaddr, dat):
        if USBI2C.ch341.CH341OpenDevice(self.usb_id) != -1:
            obuf = (c_byte * 3)()
            ibuf = (c_byte * 1)()
            obuf[0] = slaveaddr
            obuf[1] = regaddr
            obuf[2] = dat & 0xff
            USBI2C.ch341.CH341StreamI2C(self.usb_id, 3, obuf, 0, ibuf)
            USBI2C.ch341.CH341CloseDevice(self.usb_id)
            sleep(0.1)
        else:
            print("USB CH341 Open Failed!")

    def write_array(self, slaveaddr, regaddr, num, writedata):
        if USBI2C.ch341.CH341OpenDevice(self.usb_id) != -1:
            num_w = num + 2
            obuf = (c_byte * num_w)()
            ibuf = (c_byte * 1)()
            obuf[0] = slaveaddr
            obuf[1] = regaddr
            for i in range(num):
                obuf[i + 2] = writedata[i] & 0xFF
            # obuf[2] = dat & 0xff
            USBI2C.ch341.CH341StreamI2C(self.usb_id, num_w, obuf, 0, ibuf)
            USBI2C.ch341.CH341CloseDevice(self.usb_id)
            sleep(0.1)
        else:
            print("USB CH341 Open Failed!")
    def write_16bytes(self,slaveaddr,regaddr,num,writedata):
        if ((regaddr + num - 1) & 0xf0) == (regaddr & 0xf0):
            self.write_array(slaveaddr,regaddr,num,writedata)
        else:
            write_length =  0x10 - (regaddr & 0x0F)
            start_addr = regaddr
            n = num
            do_num = math.ceil((n-write_length)/16) + math.ceil(write_length/16)
            for i in range(do_num):
                data_w = writedata[i*16:i*16+write_length]
                self.write_array(slaveaddr,start_addr,write_length,data_w)
                sleep(0.1)
                n = n - write_length
                start_addr = start_addr + write_length
                if n >= 16 :
                    write_length = 16
                else:
                    write_length = n

if __name__ == '__main__':
    usb_i2c = USBI2C()
    print(usb_i2c.rate_sel("750kHz"))
    readdata = usb_i2c.read(0xA2,0)
    print(readdata)
    writearray = [0x50,0x00,0x81,0x00]
    usb_i2c.write_array(0xA2,0x00,4,writearray)
    readarray = []
    usb_i2c.read_array(0xA2,0x00,16,readarray)
    print(readarray)