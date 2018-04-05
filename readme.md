# DuerOS-Modularization
# 终端执行 sh install.sh 进行依赖安装
## 运行环境及依赖
* Python2.7.14
* gstreamer1.0
* gstreamer1.0-plugins-good
* gstreamer1.0-plugins-ugly
* python-gi
* python-gst
* gir1.2-gstreamer-1.0
### 本项目代码来源链接：https://github.com/MyDuerOS/DuerOS-Python-Client
### 作者是百度大神刘才权，其简书主页：https://www.jianshu.com/u/bf03aa158e75 博客主页 https://caiquanliu.github.io/
### 本人详细教程链接： https://developer.dueros.baidu.com/didp/forum/topic/show?topicId=245089
### 本项目为修改自定义唤醒词版本，默认喊“小白”可以唤醒，可在配置文件config.ini中修改唤醒词模型。
### 请修改为自己的DuerOS设备开放平台上创建的音箱产品的ID，需要进行远程桌面树莓派进行百度开发者账号授权。
#### vim /home/pi/DuerOS-Modularization/config.ini
#### CLIENT_ID = '你的CLIENT_ID'
#### CLIENT_SECRET = '你的CLIENT_SECRET'
### 授权：sh auth.sh 或者 ./auth.sh
### 语音唤醒：sh wakeup_trigger_start.sh 或者 ./wakeup_trigger_start.sh
### 回车唤醒：sh enter_trigger_start.sh 或者 ./enter_trigger_start.sh
