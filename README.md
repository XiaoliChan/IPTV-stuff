# IPTV-stuff
CMCC IPTV sources update &amp; convert tools

### System Requirements
1. Linux
2. Python 3

### Usage
1. Run `./updateSource.sh` if you can get CMCC IPTV sources directly (optional).
2. Run `python3 GetURL.py` for detail. (Remeber, default udpxy address is 192.168.1.1:8888)

![image](https://user-images.githubusercontent.com/30458572/115889402-7c205a00-a486-11eb-8866-8b60ba87186d.png)

### Screenshots
1. Update/get CMCC IPTV live sources.

![image](https://user-images.githubusercontent.com/30458572/115865108-70269f00-a46a-11eb-83df-b215902b8639.png)

2. Start to convert sources format that udpxy can be distinguish.

![image](https://user-images.githubusercontent.com/30458572/115889815-dd482d80-a486-11eb-945c-fa60a57acbc4.png)

3. Output file.

![image](https://user-images.githubusercontent.com/30458572/115865675-3d30db00-a46b-11eb-8ee1-cad7690db087.png)

### Special
1. If you have already setup router-on-a-stick (单臂路由) between the normal internet and IPTV internet, 
you can try to add a static route to get the CMCC IPTV sources without access modem. (Special thanks to [LGA1150](https://github.com/LGA1150))

![image](https://user-images.githubusercontent.com/30458572/115866999-14114a00-a46d-11eb-9892-647540aede2e.png)
