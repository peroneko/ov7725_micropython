"""
OV7725_INIT for OV7725

by Peroneko
"""
from machine import Pin
from sccb_driver import sccb_read_byte
from sccb_driver import sccb_write_byte
import time
import socket
# ov7725寄存器定义
REG_GAIN = 0x00
REG_BLUE = 0x01
REG_RED = 0x02
REG_GREEN = 0x03
REG_BAVG = 0x05
REG_GAVG = 0x06
REG_RAVG = 0x07
REG_AECH = 0x08
REG_COM2 = 0x09
REG_PID = 0x0A
REG_VER = 0x0B
REG_COM3 = 0x0C
REG_COM4 = 0x0D
REG_COM5 = 0x0E
REG_COM6 = 0x0F
REG_AEC = 0x10
REG_CLKRC = 0x11
REG_COM7 = 0x12
REG_COM8 = 0x13
REG_COM9 = 0x14
REG_COM10 = 0x15
REG_REG16 = 0x16
REG_HSTART = 0x17
REG_HSIZE = 0x18
REG_VSTRT = 0x19
REG_VSIZE = 0x1A
REG_PSHFT = 0x1B
REG_MIDH = 0x1C
REG_MIDL = 0x1D
REG_LAEC = 0x1F
REG_COM11 = 0x20
REG_BDBase = 0x22
REG_BDMStep = 0x23
REG_AEW = 0x24
REG_AEB = 0x25
REG_VPT = 0x26
REG_REG28 = 0x28
REG_HOutSize = 0x29
REG_EXHCH = 0x2A
REG_EXHCL = 0x2B
REG_VOutSize = 0x2C
REG_ADVFL = 0x2D
REG_ADVFH = 0x2E
REG_YAVE = 0x2F
REG_LumHTh = 0x30
REG_LumLTh = 0x31
REG_HREF = 0x32
REG_DM_LNL = 0x33
REG_DM_LNH = 0x34
REG_ADoff_B = 0x35
REG_ADoff_R = 0x36
REG_ADoff_Gb = 0x37
REG_ADoff_Gr = 0x38
REG_Off_B = 0x39
REG_Off_R = 0x3A
REG_Off_Gb = 0x3B
REG_Off_Gr = 0x3C
REG_COM12 = 0x3D
REG_COM13 = 0x3E
REG_COM14 = 0x3F
REG_COM16 = 0x41
REG_TGT_B = 0x42
REG_TGT_R = 0x43
REG_TGT_Gb = 0x44
REG_TGT_Gr = 0x45
REG_LC_CTR = 0x46
REG_LC_XC = 0x47
REG_LC_YC = 0x48
REG_LC_COEF = 0x49
REG_LC_RADI = 0x4A
REG_LC_COEFB = 0x4B
REG_LC_COEFR = 0x4C
REG_FixGain = 0x4D
REG_AREF1 = 0x4F
REG_AREF6 = 0x54
REG_UFix = 0x60
REG_VFix = 0x61
REG_AWBb_blk = 0x62
REG_AWB_Ctrl0 = 0x63
REG_DSP_Ctrl1 = 0x64
REG_DSP_Ctrl2 = 0x65
REG_DSP_Ctrl3 = 0x66
REG_DSP_Ctrl4 = 0x67
REG_AWB_bias = 0x68
REG_AWBCtrl1 = 0x69
REG_AWBCtrl2 = 0x6A
REG_AWBCtrl3 = 0x6B
REG_AWBCtrl4 = 0x6C
REG_AWBCtrl5 = 0x6D
REG_AWBCtrl6 = 0x6E
REG_AWBCtrl7 = 0x6F
REG_AWBCtrl8 = 0x70
REG_AWBCtrl9 = 0x71
REG_AWBCtrl10 = 0x72
REG_AWBCtrl11 = 0x73
REG_AWBCtrl12 = 0x74
REG_AWBCtrl13 = 0x75
REG_AWBCtrl14 = 0x76
REG_AWBCtrl15 = 0x77
REG_AWBCtrl16 = 0x78
REG_AWBCtrl17 = 0x79
REG_AWBCtrl18 = 0x7A
REG_AWBCtrl19 = 0x7B
REG_AWBCtrl20 = 0x7C
REG_AWBCtrl21 = 0x7D
REG_GAM1 = 0x7E
REG_GAM2 = 0x7F
REG_GAM3 = 0x80
REG_GAM4 = 0x81
REG_GAM5 = 0x82
REG_GAM6 = 0x83
REG_GAM7 = 0x84
REG_GAM8 = 0x85
REG_GAM9 = 0x86
REG_GAM10 = 0x87
REG_GAM11 = 0x88
REG_GAM12 = 0x89
REG_GAM13 = 0x8A
REG_GAM14 = 0x8B
REG_GAM15 = 0x8C
REG_SLOP = 0x8D
REG_DNSTh = 0x8E
REG_EDGE0 = 0x8F
REG_EDGE1 = 0x90
REG_DNSOff = 0x91
REG_EDGE2 = 0x92
REG_EDGE3 = 0x93
REG_MTX1 = 0x94
REG_MTX2 = 0x95
REG_MTX3 = 0x96
REG_MTX4 = 0x97
REG_MTX5 = 0x98
REG_MTX6 = 0x99
REG_MTX_Ctrl = 0x9A
REG_BRIGHT = 0x9B
REG_CNST = 0x9C
REG_UVADJ0 = 0x9E
REG_UVADJ1 = 0x9F
REG_SCAL0 = 0xA0
REG_SCAL1 = 0xA1
REG_SCAL2 = 0xA2
REG_SDE = 0xA6
REG_USAT = 0xA7
REG_VSAT = 0xA8
REG_HUECOS = 0xA9
REG_HUESIN = 0xAA
REG_SIGN = 0xAB
REG_DSPAuto = 0xAC

Sensor_Config = [
    # Clock config
    (REG_CLKRC, 0x00),
    # QVGA RGB565
    (REG_COM7, 0x46),
    (REG_HSTART, 0x3f),
    (REG_HSIZE, 0x50),
    (REG_VSTRT, 0x03),
    (REG_VSIZE, 0x78),
    (REG_HREF, 0x00),
    (REG_HOutSize, 0x50),
    (REG_VOutSize, 0x78),
    (REG_EXHCH, 0x00),

    # DSP control
    (REG_TGT_B, 0x7f),
    (REG_FixGain, 0x09),
    (REG_AWB_Ctrl0, 0xe0),
    (REG_DSP_Ctrl1, 0xff),
    (REG_DSP_Ctrl2, 0x20),
    (REG_DSP_Ctrl3, 0x00),
    (REG_DSP_Ctrl4, 0x00),

    # AGC AEC AWB
    (REG_COM8, 0xf0),
    (REG_COM4, 0x81),  # Pll AEC CONFIG
    (REG_COM6, 0xc5),
    (REG_COM9, 0x21),
    (REG_BDBase, 0xFF),
    (REG_BDMStep, 0x01),
    (REG_AEW, 0x34),
    (REG_AEB, 0x3c),
    (REG_VPT, 0xa1),
    (REG_EXHCL, 0x00),
    (REG_AWBCtrl3, 0xaa),
    (REG_COM8, 0xff),
    (REG_AWBCtrl1, 0x5d),

    (REG_EDGE1, 0x0a),
    (REG_DNSOff, 0x01),
    (REG_EDGE2, 0x01),
    (REG_EDGE3, 0x01),

    (REG_MTX1, 0x5f),
    (REG_MTX2, 0x53),
    (REG_MTX3, 0x11),
    (REG_MTX4, 0x1a),
    (REG_MTX5, 0x3d),
    (REG_MTX6, 0x5a),
    (REG_MTX_Ctrl, 0x1e),

    (REG_BRIGHT, 0x00),
    (REG_CNST, 0x25),
    (REG_USAT, 0x65),
    (REG_VSAT, 0x65),
    (REG_UVADJ0, 0x81),
    # (REG_SDE,     0x20),  # 黑白
    (REG_SDE, 0x06),  # 彩色 调节SDE这个寄存器还可以实现其他效果

    # GAMMA config
    (REG_GAM1, 0x0c),
    (REG_GAM2, 0x16),
    (REG_GAM3, 0x2a),
    (REG_GAM4, 0x4e),
    (REG_GAM5, 0x61),
    (REG_GAM6, 0x6f),
    (REG_GAM7, 0x7b),
    (REG_GAM8, 0x86),
    (REG_GAM9, 0x8e),
    (REG_GAM10, 0x97),
    (REG_GAM11, 0xa4),
    (REG_GAM12, 0xaf),
    (REG_GAM13, 0xc5),
    (REG_GAM14, 0xd7),
    (REG_GAM15, 0xe8),
    (REG_SLOP, 0x20),

    (REG_HUECOS, 0x80),
    (REG_HUESIN, 0x80),
    (REG_DSPAuto, 0xff),
    (REG_DM_LNL, 0x00),
    (REG_BDBase, 0x99),
    (REG_BDMStep, 0x03),
    (REG_LC_RADI, 0x00),
    (REG_LC_COEF, 0x13),
    (REG_LC_XC, 0x08),
    (REG_LC_COEFB, 0x14),
    (REG_LC_COEFR, 0x17),
    (REG_LC_CTR, 0x05),

    (REG_COM3, 0xd0),  # Horizontal mirror image

    # Night mode auto frame rate control
    (REG_COM5, 0xf5),  # 在夜视环境下，自动降低帧率，保证低照度画面质量
    # (REG_COM5,    0x31),  # 夜视环境帧率不变
]

sccb_write_byte(0x12, 0x80)  # 刷新所有寄存器至默认值

Ov7725_vsync = 0  # 全局变量，用于跟踪 VSYNC 状态


def ov7725_scan():
    if sccb_read_byte(0x0b) == 33:
        return True
    else:
        return False


def ov7725_reg_init():
    loadnum = 0
    regnum = 77
    if ov7725_scan():
        print("####OV7725 detected####")
    else:
        print("####Cannot find ov7725,Please check the connect####")
    for reg, data in Sensor_Config:
        if sccb_write_byte(reg, data):
            loadnum = loadnum + 1
    if loadnum == regnum:
        print("####Reg configured successful####")


VSYNC_PIN = Pin(46, Pin.IN)  # VSYNC 引脚，输入模式
OE_PIN = Pin(12, Pin.OUT , Pin.PULL_UP)  # FIFO 输出使能，引脚，输出模式
WRST_PIN = Pin(9, Pin.OUT ,  Pin.PULL_UP)  # FIFO 写复位，引脚，输出模式
RRST_PIN = Pin(10, Pin.OUT , Pin.PULL_UP)  # FIFO 读复位，引脚，输出模式
RCLK_PIN = Pin(21, Pin.OUT , Pin.PULL_UP)  # FIFO 读时钟，引脚，输出模式
WE_PIN = Pin(11, Pin.OUT , Pin.PULL_UP)  # FIFO 写使能，引脚，输出模式
pins = [Pin(pin_num,Pin.IN,Pin.PULL_UP) for pin_num in range(42, 34, -1)] #FIFO数据引脚




# FIFO 控制函数
def FIFO_WRST_L():
    WRST_PIN.value(0)
    


def FIFO_WRST_H():
    WRST_PIN.value(1)
    


def FIFO_WE_L():
    WE_PIN.value(0)
    


def FIFO_WE_H():
    WE_PIN.value(1)
    


# 中断处理函数
def vsync_irq_handler(pin):
    global Ov7725_vsync

    if Ov7725_vsync == 0:
        FIFO_WRST_L()  # 拉低使 FIFO 写(数据 from 摄像头)指针复位
        FIFO_WE_H()  # 拉高使 FIFO 写允许
        Ov7725_vsync = 1
        FIFO_WRST_H()  # 允许使 FIFO 写(数据 from 摄像头)指针继续
    elif Ov7725_vsync == 1:
        FIFO_WE_L()  # 拉低使 FIFO 写暂停
        Ov7725_vsync = 2




def vsync_init():
    vsync_pin = Pin(VSYNC_PIN, Pin.IN, Pin.PULL_UP)

    #	 配置中断
    vsync_pin.irq(trigger=Pin.IRQ_FALLING, handler=vsync_irq_handler)

    print("VSYNC GPIO configured and interrupt handler set")


def FIFO_PREPARE():
    RRST_PIN.value(0)  # FIFO_RRST_L
    RCLK_PIN.value(0)  # FIFO_RCLK_L
    RCLK_PIN.value(1)  # FIFO_RCLK_H
    RCLK_PIN.value(0)  # FIFO_RCLK_L
    RRST_PIN.value(1)  # FIFO_RRST_H
    
    RCLK_PIN.value(1)  # FIFO_RCLK_H


def img_transfer():
    with open("data.txt", "w") as file:
        
        for i in range (0,320):
            for j in range (0,240):
                RCLK_PIN.value(0)
                
                data1 = [pin.value() for pin in pins]
                RCLK_PIN.value(1)
                
                RCLK_PIN.value(0)
                
                data2 = [pin.value() for pin in pins]
                RCLK_PIN.value(1)
                
                high_byte = int(''.join(map(str, data1)), 2)
                low_byte = int(''.join(map(str, data2)), 2)
                combined = (high_byte << 8) | low_byte
                hex_value = f"{combined:04x}"
                file.write(hex_value)

    

OE_PIN.value(0)
WE_PIN.value(1)
ov7725_reg_init()
vsync_init()



