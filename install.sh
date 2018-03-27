echo 'Install DuerOS-Modular Python Dependency Library Now!'
sudo apt-get update
sudo apt install gstreamer1.0
sudo apt install gstreamer1.0-plugins-good
sudo apt install gstreamer1.0-plugins-ugly
sudo apt install python-gi
sudo apt install gir1.2-gstreamer-1.0
sudo apt install python-gst0.1
sudo chmod 777 wakeup_trigger_start.sh auth.sh enter_trigger_start.sh
sudo apt-get install -y python-dateutil gir1.2-gstreamer-1.0 python-pyaudio libatlas-base-dev python-dev python-configparser openssl mplayer
sudo pip install gi
sudo pip install tornado
sudo pip install hyper
sudo python2 ./aip/setup.py install