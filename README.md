### creating network
```
sudo docker network create example_net
```

### address already in use
if u seen message:
```
Error starting userland proxy: listen tcp4 0.0.0.0:6379: bind: address already in use
```
Check who using this port:  
```
sudo apt-get install net-tools
sudo netstat -nlpt |grep 6379
```
And when u see:
```
tcp        0      0 127.0.0.1:6379          0.0.0.0:*               LISTEN      885/redis-server 12 
tcp6       0      0 ::1:6379                :::*                    LISTEN      885/redis-server 12
```
stop him:
```
sudo /etc/init.d/redis-server stop
```
