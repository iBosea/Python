# -*- coding:utf-8 -*-
from IPy import *
i=1
va=input('请输入你要重复使用程序的次数:')
while i <= int(va):
    ip = raw_input('请输入您的第%s次查询IP地址或网段的值:'%i)
    while len(ip) == 0:
        print '亲亲(。・∀・)ノ为什么你不输入呢?再来一遍吧'
        ip = raw_input('请输入您的第%s次查询IP地址或网段的值:'%i)
    ips = IP(ip)
    if len(ips) <= 1:
        ifa = IP(ips).iptype()
        if ifa == 'PRIVATE':
            print '您输入的地址为私有地址'
            print '您输入的IP经过二进制转换后为:' + ips.strBin()
            print '您输入的IP经过16进制转换后为:' +ips.strHex()
        else:
            print '您输入的地址为公网地址'
            print '您输入的IP经过二进制转换后为:' + ips.strBin()
            print '您输入你IP经过16进制转换后为:' + ips.strHex()
    else:
        print '您输入的网段子网个数有:' +str(ips.len())
        print '您输入的网段子网掩码地址为:' +str(ips.netmask())
        print '您输入的网段广播地址为:' +str(ips.broadcast())
        print '您输入的网段网络ID为:' +str(ips.net())
    i += 1
