
'''
 * Copyright 2024 
 * Licensed under the MIT license 
 * @author txf
 * @date 2024-04-04 09:08:08
'''

import pywifi
from pywifi import const # 引入一个常量
import  time

def scan_wifi() : 

    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    interface.scan()
    time.sleep(1)
    results = interface.scan_results()

    for network in results : 
        print(f"SSID:{network.ssid}, 信号强度:{network.signal} ")

scan_wifi()