echo 'Install DuerOS-Modularization Python Dependency Library Now!'
sudo chmod 777 wakeup_trigger_start.sh auth.sh enter_trigger_start.sh
sudo apt-get update
sudo apt install -y python-requests
sudo apt install -y python-configparser
sudo apt install -y python-dateutil
sudo apt install -y openssl
sudo apt install -y python-gi
sudo apt install -y python-dateutil gir1.2-gstreamer-1.0 python-pyaudio libatlas-base-dev python-dev
sudo apt install -y gstreamer1.0
sudo apt install -y mplayer
sudo pip uninstall gi
sudo pip install tornado
sudo pip install hyper
sudo python2 ./aip/setup.py install