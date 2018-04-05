echo 'Install DuerOS-Modularization Python Dependency Library Now!'
sudo chmod 777 wakeup_trigger_start.sh auth.sh enter_trigger_start.sh
sudo apt-get update
sudo pip uninstall gi
sudo pip install tornado hyper
sudo apt install -y python-dateutil gir1.2-gstreamer-1.0 python-pyaudio libatlas-base-dev python-dev
sudo apt install -y python-requests python-gi python-configparser gstreamer1.0 openssl
sudo python2 ./aip/setup.py install