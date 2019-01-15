# MyDuerOS

# 项目亮点

- 主要选项实现配置化，包括唤醒词路径，配置等
- 加入百度语音合成，可以自定义回复
- 通过DCS协议返回的json实现语义理解，相当于只使用语音识别和百度语音理解
- 更多请自行发掘

# 项目来源

[DuerOS-Python-Client](https://github.com/MyDuerOS/DuerOS-Python-Client)  

# 原项目作者

百度刘才权  
[Github主页](https://github.com/CaiquanLiu)  
[简书主页](https://www.jianshu.com/u/bf03aa158e75)  
[博客主页](https://caiquanliu.github.io/)  

# 项目教程

[本人详细的DuerOS教程](https://developer.dueros.baidu.com/didp/forum/topic/show?topicId=245089)  

# 唤醒词

默认是**小白**   
[唤醒词训练地址](https://snowboy.kitt.ai/hotword/351)  

# 修改步骤

- 请修改为自己的DuerOS设备开放平台上创建的音箱产品的ID，需要百度开发者账号授权。
- 修改根目录下配置文件`config.ini`    
```shell
vim config.ini
```
- app_id = "百度语音合成产品ID"
- client_id = '你的CLIENT_ID'
- client_secret = '你的CLIENT_SECRET'
- snowboyPmdl = "唤醒词路径"
- 需要赋予最高权限才可执行 
```shell
chmod 777 wakeup_trigger_start.sh auth.sh enter_trigger_start.sh 
```
- ./auth.sh
- ./wakeup_trigger_start.sh
- ./enter_trigger_start.sh
- 或者在Shell脚本前添加sh
- sh auth.sh
- sh wakeup_trigger_start.sh
- sh enter_trigger_start.sh

# 说明

- 时间有限，项目基本停止维护
