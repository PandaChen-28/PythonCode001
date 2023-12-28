import serial
import serial.tools.list_ports
import time
import threading

def show_port():
    port_list = list(serial.tools.list_ports.comports())
    print(port_list)

    if len(port_list)== 0:
        print("无可用串口")
    else:
        for i in range(0,len(port_list)):
            print(port_list[i])
    #print(time.time())
##发送
# d=bytes.fromhex('10 11 12 34 3f')
# s.write(d)
# s.close()


DATA = ""  # 读取的数据
DATA_ALL = bytearray(40960)
DATA_LEN = 0
NOEND = True  # 是否读取结束
DATA_IN_FLAG = 0
START_TIME = 0


# 读数据的本体
def read_data(ser):
    global DATA, NOEND, DATA_IN_FLAG, START_TIME, DATA_ALL, DATA_LEN
    START_TIME = time.time()
    NOEND = True
    # 循环接收数据（此为死循环，可用线程实现）
    while NOEND:
        if ser.in_waiting:
            START_TIME = time.time()
            DATA_IN_FLAG = 1
            length = ser.in_waiting

            DATA = ser.read(length)  # 注意 ser.read了之后 in_waiting马上变成0了

            # DATA_ALL = bytearray(DATA_LEN+length)
            for i in range(0, length):
                DATA_ALL[DATA_LEN + i] = DATA[i]

            # print("DATA_LEN=%d"%(DATA_LEN))
            DATA_LEN += length
            # DATA = ser.read(ser.in_waiting).decode("gbk")
            # print("\n>> receive: ", DATA, "\n>>", end="")
            # print(">>", end="")

            if (DATA == "quit"):
                print("oppo seri has closen.\n>>", end="")


        else:
            if DATA_IN_FLAG:
                # print("time.time() - START_TIME = %d \r\n"%(time.time()))
                if time.time() - START_TIME > 0.010:  # 串口超时10ms
                    DATA_PRINT = bytearray(DATA_LEN)
                    for i in range(0, DATA_LEN):
                        DATA_PRINT[i] = DATA_ALL[i]
                    message_read = DATA_PRINT.decode('gbk')
                    print(DATA_PRINT.decode('gbk'))
                    START_TIME = time.time()
                    DATA_IN_FLAG = 0
                    DATA_LEN = 0
                    NOEND = False
                    return message_read


# 打开串口
def open_seri(portx, bps, timeout):
    ret = False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)

        # 判断是否成功打开
        if (ser.is_open):
            ret = True
            th = threading.Thread(target=read_data, args=(ser,))  # 创建一个子线程去等待读数据
            th.start()
    except Exception as e:
        print("error!", e)

    return ser, ret


# 关闭串口
def close_seri(ser):
    global NOEND
    NOEND = False
    ser.close()


# 写数据
def write_to_seri(ser, text):
    res = ser.write(text.encode("gbk"))  # 写
    return res


# 读数据
def read_from_seri():
    global DATA
    data = DATA
    DATA = ""  # 清空当次读取
    return data

def main():
    show_port()
    port = input("输入串口名：")
    ser, ret = open_seri(port, 9600, None)  # 串口com3、bps为115200，等待时间为永久
    text = '\r'
    write_to_seri(ser, text)
    MESSAGE_READ = read_data(ser)
    text = "show gpon onu state\n"
    write_to_seri(ser, text)
    MESSAGE_READ = read_data(ser)
    print('this is print message:\n')
    print(MESSAGE_READ)
    flag = 'working'
    while True:
        if MESSAGE_READ.find(flag) >= 0:
            # print('good')
            text = 'no onu 1\n'
            write_to_seri(ser, text)
            MESSAGE_READ = read_data(ser)
            text = 'onu 1 type ZTE-F601 sn  YHTC7B36FE7A\n'
            write_to_seri(ser, text)
            MESSAGE_READ = read_data(ser)
        else:
            # print('not good')
            time.sleep(1)
            text = "show gpon onu state\n"
            write_to_seri(ser, text)
            MESSAGE_READ = read_data(ser)
    input("Press Enter to return to the home page.")

if __name__ == "__main__":
    main()
    # ser, ret = open_seri("COM4", 115200, None) # 串口com3、bps为115200，等待时间为永久
    # if ret == True: # 判断串口是否成功打开
    #     count = write_to_seri(ser, "exit")
    #     print("写入总字节数：", count)

    # 打开一个串口


    # while True:
    #     text = input(">>")
    #     write_to_seri(ser, text)
    #     if text == "quit":
    #         close_seri(ser)
    #         print("bye!")
    #         break
