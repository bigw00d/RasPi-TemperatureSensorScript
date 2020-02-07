#!/usr/bin/python
import time
import smbus

msleep = lambda x: time.sleep(x/1000.0)

ADDR = 0x40

i2c = smbus.SMBus(1)

CMD_READ_TEMP_HOLD = 0xe3
CMD_READ_HUM_HOLD = 0xe5
CMD_READ_TEMP_NOHOLD = 0xf3
CMD_READ_HUM_NOHOLD = 0xf5
CMD_WRITE_USER_REG = 0xe6
CMD_READ_USER_REG = 0xe7
CMD_SOFT_RESET= 0xfe

def getValueTemp():
    val = getValue(CMD_READ_TEMP_HOLD)
    temp = -46.85 + (175.72 * val / 65536)
    return temp

def getValueHumid():
    val = getValue(CMD_READ_HUM_HOLD)
    humid = -6 + (125.0 * val / 65536)
    return humid

def getValue(adr):
    i2c.write_byte(ADDR, adr)
    msleep(100)
    data = i2c.read_i2c_block_data(ADDR, adr, 3)
    msleep(100)
    tmp = data[0]
    tmp = tmp<<8
    tmp = tmp | data[1]
    tmp = tmp & 0xFFFC
    return tmp

i2c.write_byte(ADDR, CMD_SOFT_RESET)
msleep(100)

# i2c.write_byte(ADDR, CMD_READ_TEMP_HOLD)
# msleep(100)

# data = i2c.read_i2c_block_data(ADDR, CMD_READ_TEMP_HOLD, 3)
# msleep(100)

# t1 = 256*data[0] + data[1]
# temp = (t1/65536.0) * 175.72 - 46.85

temp = getValueTemp()
# print('Temperature:' + str(temp))
print('Temperature   : {:.2f}'.format(temp))

humid = getValueHumid()
# print('Humidity:' + str(humid))
print('Humidity   : {:.2f}'.format(humid))
