# 脚本说明

## run_zmap.sh

注意为了方便，ip 和子网掩码直接硬编码了。

运行方式：

```
# 在默认常用端口上进行 zmap
bash run_zmap.sh

# 在指定端口上进行 zmap
bash run_zmap.sh <port1> [port2, ...]
```

运行时会询问是否跳过已有输出文件的端口，若不跳过则会向输出文件名后加 `_<ind>` 以避免文件冲突。


# 测试

远程服务器：ubuntu@120.53.3.109

`sudo autossh -NR 8888:localhost:8888 ubuntu@120.53.3.109`

于是连接：

```
sudo autossh ubuntu@120.53.3.109
sudo autossh -p 8888 l1eisure@localhost
```

## 协作文档

https://www.processon.com/diagraming/5fd503d95653bb06f3394cf0

https://docs.qq.com/doc/DVEhwbXJJc2NuRG9H

## 工具

* traceroute <ip>
* ping -R <ip>
* nmap <ip>
* nmap -sP <ip>: 扫描网段存活主机
* zmap 

```
 - You can start Nessus Scanner by typing /bin/systemctl start nessusd.service
 - Then go to https://yyr-OMEN-by-HP-Laptop-15-dh0xxx:8834/ to configure your scanner
```

## 结果

* 183.172.0.0/16: 寝室无线网
* 183.173.0.0/16: 教室无线网
* 59.66.0.0/16: 有线网
* 118.229.[1~4].0: 大量 BGP，推测为清华主干网。另外118.229.0.0中还有若干其他学校的自治域。118.229.0.0/19 ?
* 166.111.0.0/16: 有大量清华网站服务器；
* 202.112.0.0/16：全国教育网。

* 183.172.3.75: 打印机
* http://183.172.158.194:8080/: 目录访问？

## traceroute

测试ip：183.172.127.211

183.172.147.113

trace 一下 info:

```
yyr@yyr-OMEN-by-HP-Laptop-15-dh0xxx:~$ traceroute info.tsinghua.edu.cn
traceroute to info.tsinghua.edu.cn (166.111.4.98), 30 hops max, 60 byte packets
 1  _gateway (183.172.120.1)  11.613 ms  11.846 ms  12.144 ms
 2  172.17.2.25 (172.17.2.25)  12.504 ms  12.492 ms  12.461 ms
 3  118.229.2.78 (118.229.2.78)  12.428 ms  12.396 ms  12.363 ms
 4  118.229.9.6 (118.229.9.6)  12.280 ms  12.263 ms  12.643 ms
 5  166.111.4.98 (166.111.4.98)  12.550 ms  12.523 ms  12.490 ms
```

## zmap

```
# 其中 166.111.4.1 是 info.tsinghua.edu.cn 的 IP，扫描出了大量网站服务器
zmap -p 80 -B 1Mbps 166.111.4.1/16

# 179 端口为 BGP 端口，从 118.229.0.0/16 中扫描除了大量 BGP，推测是与其他自治域接触的网段
zmap -p 179 -B 1Mbps 118.229.0.0/16
```

## 问题记录

### 关于 TTL

ping 时发现 TTL 初始值有时是 255，有时是 64。

原因：首先不同操作系统 TTL 初始值不同，所以推测显示的为返回包的 TTL。

