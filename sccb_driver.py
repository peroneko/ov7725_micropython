"""
SCCB_DRIVER for OV7725

by Peroneko
"""
from machine import Pin
import time

# 定义引脚
SCL_PIN = 48  # 根据实际接线情况调整
SDA_PIN = 47  # 根据实际接线情况调整

#定义OV7725地址
OV7725_ADDR = 0x42

# 初始化引脚
scl = Pin(SCL_PIN, Pin.PULL_UP)
sda = Pin(SDA_PIN, Pin.OPEN_DRAIN)

# 设置引脚初始状态
scl.value(1)
sda.value(1)

def sccb_delay():
    time.sleep_us(1000)  # 微秒级延时，根据需要调整


def sccb_start():
    sda.value(1)
    scl.value(1)
    sccb_delay()
    if not sda.value():
        return False  # SDA 线为低电平则总线忙
    sda.value(0)
    sccb_delay()
    if sda.value():
        return False  # SDA 线为高电平则总线出错
    sda.value(0)
    sccb_delay()
    return True

def sccb_stop():
    scl.value(0)
    sccb_delay()
    sda.value(0)
    sccb_delay()
    scl.value(1)
    sccb_delay()
    sda.value(1)
    sccb_delay()

def sccb_ack():
    scl.value(0)
    sccb_delay()
    sda.value(0)
    sccb_delay()
    scl.value(1)
    sccb_delay()
    scl.value(0)
    sccb_delay()

def sccb_no_ack():
    scl.value(0)
    sccb_delay()
    sda.value(1)
    sccb_delay()
    scl.value(1)
    sccb_delay()
    scl.value(0)
    sccb_delay()

def sccb_wait_ack():
    scl.value(0)
    sccb_delay()
    sda.value(1)
    sccb_delay()
    scl.value(1)
    sccb_delay()
    if sda.value():
        scl.value(0)
        return False
    scl.value(0)
    return True

def sccb_send_byte(data):
    for i in range(8):
        scl.value(0)
        if data & 0x80:
            sda.value(1)
        else:
            sda.value(0)
        data <<= 1
        sccb_delay()
        scl.value(1)
        sccb_delay()
    scl.value(0)

def sccb_receive_byte():
    data = 0
    sda.value(1)
    for i in range(8):
        data <<= 1
        scl.value(0)
        sccb_delay()
        scl.value(1)
        if sda.value():
            data |= 1
        sccb_delay()
    scl.value(0)
    return data



def sccb_write_byte(write_address, send_byte):
    if not sccb_start():
        return False
    sccb_send_byte(OV7725_ADDR)
    if not sccb_wait_ack():
        sccb_stop()
        return False
    sccb_send_byte(write_address)
    sccb_wait_ack()
    sccb_send_byte(send_byte)
    sccb_wait_ack()
    sccb_stop()
    return True

def sccb_read_byte(read_address):
    if not sccb_start():
        return None
    sccb_send_byte(OV7725_ADDR)
    if not sccb_wait_ack():
        sccb_stop()
        return None
    sccb_send_byte(read_address)
    sccb_wait_ack()
    sccb_stop()

    if not sccb_start():
        return None
    sccb_send_byte(OV7725_ADDR + 1)
    if not sccb_wait_ack():
        sccb_stop()
        return None

    data = sccb_receive_byte()
    sccb_no_ack()
    sccb_stop()
    return data
