# -*- coding: utf-8 -*-
import re, math
from telnetlib import Telnet
from dataprocessing import *
def get_config_data():
    Config = {}
    with open('Configuration.ini', 'r', encoding='utf-8')as f:
        read_data = f.read().split('\n')
        for i in read_data:
            data_key = i.split(' = ')
            if len(data_key) == 2:
                config_element = {data_key[0]: data_key[1]}
                Config.update(config_element)
    ip = Config['IP']
    user = Config['User']
    password = Config['Password']
    mod_set = Config['Mode_Select']
    flag = Config['Flag']
    cmd_read = Config['Cmd_Read']
    cmd_write = Config['Cmd_Write']
    max_read = int(Config['MaxRead'])
    max_write = int(Config['MaxWrite'])
    slave_add = '0x51'
    reg_add = '0x80'
    length_data = '1'
    read_buffer = []
    write_buffer = []


def Cmd_Login(con, UserName, Password, Mode_set='diag'):
    flag_Login = 'Login'
    flag_PWD = 'Password'
    flag_cmd = '#'
    flag_RTK = 'RTK.0>'
    data = con.read_until(flag_Login.encode(), 3)
    print(data.decode(errors='ignore'))
    con.write(UserName.encode() + b'\n')
    data = con.read_until(flag_PWD.encode(), 3)
    print(data.decode(errors='ignore'))
    con.write(Password.encode() + b'\n')
    data = con.read_until(flag_cmd.encode(), 3)
    print(data.decode(errors='ignore'))
    con.write(Mode_set.encode() + b'\n')
    data = con.read_until(flag_RTK.encode(), 3)
    print(data.decode(errors='ignore'))


def Cmd_ReadByte(con, SlaveAddress, RegAddress, Length, CMD, flag_Read):
    data_read = []
    Cnt = int(Length)
    S_Reg_0 = int(RegAddress, 16)
    for i in range(Cnt):
        S_Reg = S_Reg_0 + i
        RegAddress = ('{:#04x}'.format(S_Reg))
        rep = {'SlaveAddress': SlaveAddress, 'RegAddress': RegAddress}
        pattern = re.compile("|".join(rep.keys()))
        Str_cmd = pattern.sub(lambda m: rep[re.escape(m.group(0))], CMD)
        con.write(Str_cmd.encode() + b'\n')
        data_s = con.read_until(flag_Read.encode(), 3)
        data_s = str(data_s)
        data_s = data_s.split('\\r\\n\\r')[0]
        data_s = data_s.split('data:')[1]
        data_s = re.findall('0x(\w+)', data_s)
        for i in data_s:
            data_read.append(int(i, 16))
    return data_read

if __name__ == '__main__':
    ip = '192.168.1.1'
    # user = 'admin'
    # password = 'chzhdpl@246'
    # slave_add = '0x51'
    # reg_add = '0x0'
    # length_data = '1'
    # cmd_read = 'echo reg_get RegAddress > /proc/ux3326/debug'
    # flag = '#'
    # tn = Telnet(ip)
    # Cmd_Login(tn, user, password)
    # data_read = Cmd_ReadByte(tn, slave_add, reg_add, length_data, cmd_read, flag)
    # print(data_read)
    # txp = adc2dbm(data_read)
    # txp_uw = data_read[0]*256+data_read[1]
    # print(txp_uw)
    # print('tx power: {} dbm'.format(txp))
