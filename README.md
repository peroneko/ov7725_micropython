# ov7725_micropython
ov7725_driver_by_micropython

由于现有的代码都是基于C语言的 于是手搓了一个ov7725的驱动 兼容stm32野火ov7725摄像头模块
一个简单的ov7725(带fifo)的驱动
其中包含sccb协议和ov7725的初始化
测试用例包含在irq中 配置一下pin脚 运行即用 
使用FIFO_PREPARE() - img_transfer() 读取输出一帧图片至data.txt 
接下来在电脑上使用test.py即可将data.txt生成为图片
使用Ov7725_sync = 0 归零指针 再循环即可读取第二张图片



file:
--sccb_driver.py
--irq.py
--test.py



