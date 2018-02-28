## PortScanIdentification
版本: V1.0  
一款扫描指定IP地址，获取开放端口并且识别端口服务的脚本


    [root@localhost PortScanIdentification]# python scan.py -h
    usage: scan.py [-h] [-path PATH] [-url URL] [-banner]
    
    optional arguments:
      -h, --helpshow this help message and exit
      -path PATH, --path PATH
    filePath default:/tools/ip.txt
      -url URL, --url URL   url address
      -banner, --banner get port banner info.
### 参数说明:
-path 指定masscan需要的iL的地址(扫描的IP文件)  
-url 下载URL的内容到/tmp/myIp.txt 并且iL的值为/tmp/myIp.txt  
-banner 识别端口服务,结果会存入Mongodb

### 脚本流程：
调用masscan扫描器对ip.txt文件中的IP地址进行端口扫描，并将结果存入Mongodb的PortInfo集合  
如果需要识别端口服务，使用-banner参数，它会在接下来对已经扫描出来的结果通过Nmap的-sV参数进行端口识别，并将结果存入Mongodb的BannerInfo集合，存入前会清空BannerInfo集合

getBannerInfoInMongodb.py 直接查看所有的端口识别结果

    [root@localhost PortScanIdentification]# python getBannerInfoInMongodb.py 
    186.75.16.21	40810	ssh OpenSSH 6.6.1
    137.50.3.42		40810	ssh OpenSSH 5.3
    143.59.45.89	40810	ssh OpenSSH 6.6.1
    166.75.45.56	80		http Apache httpd 2.2.15
    116.75.55.56	40810	ssh OpenSSH 5.3
    156.75.16.165	80		http nginx
    146.75.12.93	80		http Apache httpd 2.2.15
    136.75.6.82		80		http Apache httpd 2.2.15
    126.75.82.171	80		http Apache httpd 2.2.15
    11.50.4.111		80		http Apache httpd 2.2.15
    13.59.121.3		80		http nginx
    13.59.111.193	80		http nginx
    