echo 'Install DuerOS-Modular Python Dependency Library Now!'
sudo apt-get update
sudo chmod 777 wakeup_trigger_start.sh auth.sh enter_trigger_start.sh
sudo apt-get install -y python-dateutil gir1.2-gstreamer-1.0 python-pyaudio libatlas-base-dev python-dev python-configparser openssl
sudo pip install tornado hyper
sudo ./aip/setup.py install