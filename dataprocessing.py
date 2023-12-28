import matplotlib.pyplot as plt
import math
#############################################################
'''
lut2reg reg2lut     105byte 2 84data / 84data 2 105byte

'''
#############################################################
def lut2reg(lutdata):
    regdata = []
    for i in range(math.ceil(len(lutdata)/4)):
        regdata.append(lutdata[i * 4] // 4)
        regdata.append(lutdata[i * 4 + 1] // 16 + (lutdata[i * 4] % 4) * 64)
        regdata.append(lutdata[i * 4 + 2] // 64 + (lutdata[i * 4 + 1] % 16) * 16)
        regdata.append(lutdata[i * 4 + 3] // 256 + (lutdata[i * 4 + 2] % 64) * 4)
        regdata.append(lutdata[i * 4 + 3] % 256)
    return regdata

def reg2lut(regdata):
    lutData = []
    for i in range(math.ceil(len(regdata)/5)):
        lutData.append(regdata[i * 5] * 4 + regdata[i * 5 + 1] // 64)
        lutData.append((regdata[i * 5 + 1] % 64) * 16 + regdata[i * 5 + 2] // 16)
        lutData.append((regdata[i * 5 + 2] % 16) * 64 + regdata[i * 5 + 3] // 4)
        lutData.append((regdata[i * 5 + 3] % 4) * 256 + regdata[i * 5 + 4])
    return lutData

def skewlut(lutdata,k=1.0):
    new_lutData = []
    for i in range(len(lutdata)):
        new_lutData.append(round(lutdata[i] * k))
    return new_lutData

def panlut(lutdata,b = 0):
    new_lutData = []
    for i in range(len(lutdata)):
        new_lutData.append(lutdata[i] + b)
    return new_lutData

def uw2dbm(power):
    power = float(power)/10000.0
    if power == 0:
        return '-Inf'
    dbm = math.log10(power)*10
    return dbm

def dbm2uw(power):
    p = power / 10.0 + 4
    power_uw = int(10 ** (p))
    return power_uw

def adc2dbm(adc=[0,0]):
    p_adc = adc[0]*256 + adc[1]
    dbm = uw2dbm(p_adc)
    return dbm

def adc2vcc(adc=[0,0]):
    v_adc = adc[0]*256 + adc[1]
    vcc = v_adc/10000.0
    return vcc

def adc2temp(adc=[0,0]):
    t_adc = adc[0] * 256 + adc[1]
    temp = t_adc / 256.0
    return temp

def adc2current(adc=[0,0]):
    i_adc = adc[0]*256 + adc[1]
    ibias = i_adc / 500.0
    return ibias

def adc2ddm(adc=[0,0,0,0,0,0,0,0,0,0]):
    ddm = {}
    ddm['temp'] = adc2temp(adc[0:2])
    ddm['vcc'] = adc2vcc(adc[2:4])
    ddm['ibias'] = adc2current(adc[4:6])
    ddm['txp'] = adc2dbm(adc[6:8])
    ddm['rxp'] = adc2dbm(adc[8:10])
    return ddm

def char_float_32(chardata):
    M = (((chardata[1] & 0x7F) << 16)|(chardata[2] << 8)|(chardata[3]))/8388608.0 + 1.0
    E = ((chardata[0] & 0x7F) <<1) | (chardata[1] >> 7)
    S = chardata[0] >> 7
    value = ((-1) ** S) * (2 ** (E - 127)) * M
    return value

def float_32_char(floatdata):
    if(floatdata >= 0):
        S = 0
    else:
        S = 1
    intdata = int(floatdata)
    f_data = floatdata
    flag = 0
    if floatdata >= 1:
        while intdata != 1:
            flag += 1
            intdata = intdata // 2
    else:
        while f_data < 1:
            flag -= 1
            f_data *= 2
    E = 127 + flag
    M = round((floatdata - (2 ** flag)) * (2 ** (23 - flag)))
    value = (S * (2 ** 31)) + (E * (2 ** 23)) + (M)
    chardata = [(value // 16777216),((value & 0xFF0000) // 65536),((value & 0xFF00) // 256),
                (value % 256)]
    return chardata

def int2char(intdata):
    if intdata > 0:
        return [(intdata//256),(intdata % 256)]
    else:
        intdata = 65536 + intdata
        return [(intdata // 256), (intdata % 256)]

def char2int(chardata):
    if chardata[0] & 0x80:
        value = ((chardata[0] * 256) + chardata[1]) - 65536
    else:
        value = (chardata[0] * 256) + chardata[1]
    return value

def char2dac(chardata):
    dac = (chardata[0] * 4) + (chardata[1] & 0x03)
    return dac

def dac2char(dac):
    chardata = [(dac // 4),(dac % 4)]
    return chardata

def saveslope(slope):
    slope = round(slope * 256)
    slopereg = [(slope // 256),(slope % 256)]
    return slopereg

def getslope(slopedata):
    slope_int = slopedata[0] * 256 + slopedata[1]
    slope = slope_int / 256.0
    return slope

def saveoffset(offset):
    offset = int2char(round(offset))
    return offset

def getoffset(offsetdata):
    offset_uint = offsetdata[0] * 256 + offsetdata[1]
    if offset_uint > 32767:
        offset = offset_uint - 65536
    else:
        offset = offset_uint
    return offset

def setbit(num,bit):
    num |= (0x01 << bit)
    return num

def clrbit(num,bit):
    num &= ~(0x01 << bit)
    return num

def index_setbit(num,bit,Value=False):
    if(Value):
        result = setbit(num,bit)
    else:
        result = clrbit(num,bit)
    return result

def index_readbit(num,bit):
    mark = 0x01 << bit
    if(num & mark):
        return True
    else:
        return False


if __name__ == '__main__':
    LUTData = [16, 16, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 24, 24, 24, 25, 25, 26,
               26, 26, 27, 28, 29, 30, 31, 32, 34, 34, 36, 37, 38, 40, 41, 43, 44, 45, 46, 49, 50, 53, 56, 58, 61, 63,
               65, 69, 73, 78, 82, 87, 91, 96, 100, 105, 111, 119, 126, 133, 140, 147, 153, 160, 167, 174, 181, 188,
               195, 202, 208, 216, 222, 229, 236, 243, 250, 257]
    # plt.plot(LUTData)
    # regdata = []
    # regdata = lut2reg(LUTData)
    # l1 = ['{:#04x}'.format(i) for i in regdata]
    # print(l1)
    # LUTData_new = reg2lut(regdata)
    # plt.plot(LUTData_new)
    # print(LUTData_new)
    # LUTData_skew = skewlut(LUTData_new,1.5)
    # plt.plot(LUTData_skew)
    # LUTData_pan = panlut(LUTData,-10)
    # plt.plot(LUTData_pan)
    # plt.show()
    ########################################3
    # from ch341_usb_iic import *
    # i2c = USBI2C()
    # adc = []
    # i2c.read_array(0xA2,0x60,10,adc)
    # print(adc)
    # ddm = adc2ddm(adc)
    # print(ddm)
    #######################################
    # chardata = [64,73,15,208]
    # chardata = [64,73,15,219]
    # testdata = char_float_32(chardata)
    # print(testdata)
    # print(char_float_32(float_32_char(1)))
    # print(float_32_char(1))
    #######################################
    # print(char2int(int2char(-128)))
    #######################################
    # print(dac2char(627))
    #
    # print(getoffset([0x80,0x89]))
    # print(getoffset([0xFF, 0xFF]))
    # print(getoffset([0x7F, 0xFF]))
    # print(getoffset([0x0, 0x0]))
    # print(getslope([0x01,0xd5]))

    print(char2dac([0x56,0x03]))
    print(char2dac([0x80,0x03]))