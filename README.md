# DuerOS-Modular
# 终端执行 sh install.sh 进行依赖安装
## Python环境：Python2.7.14
### 本项目代码来源链接：https://github.com/MyDuerOS/DuerOS-Python-Client
### 作者是百度大神刘才权，其简书主页：https://www.jianshu.com/u/bf03aa158e75 博客主页 https://caiquanliu.github.io/
### 本人详细教程链接： https://developer.dueros.baidu.com/didp/forum/topic/show?topicId=245089
### 本项目为修改自定义唤醒词版本，默认喊“小白”可以唤醒，可在配置文件config.ini中修改唤醒词模型。
### 请修改为自己的DuerOS设备开放平台上创建的音箱产品的ID，需要进行远程桌面树莓派进行百度开发者账号授权。
#### 安装远程桌面包 sudo apt-get install -y tightvncserver xrdp
#### vim /home/pi/DuerOS-Modular/config.ini
#### CLIENT_ID = '你的CLIENT_ID'
#### CLIENT_SECRET = '你的CLIENT_SECRET'
### 赋予最高权限 chmod 777 wakeup_trigger_start.sh auth.sh enter_trigger_start.sh
### 授权：sh auth.sh 或者 ./auth.sh
### 语音唤醒：sh wakeup_trigger_start.sh 或者 ./wakeup_trigger_start.sh
### 回车唤醒：sh enter_trigger_start.sh 或者 ./enter_trigger_start.sh
