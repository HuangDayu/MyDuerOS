echo 'Remove And Uninstall DuerOS-Modularization Python Dependency Library Now!'
sudo apt-get update
sudo apt remove -y gstreamer1.0
sudo apt remove -y gstreamer1.0-plugins-good
sudo apt remove -y gstreamer1.0-plugins-ugly
sudo apt remove -y python-gi
sudo apt remove -y gir1.2-gstreamer-1.0
sudo apt remove -y gir1.2-gtk-3.0
sudo apt remove -y python-gst-1.0
sudo apt remove -y python-dateutil
sudo apt remove -y python-pyaudio
sudo apt remove -y libatlas-base-dev
sudo apt remove -y python-dev
sudo apt remove -y python-configparser
sudo apt remove -y openssl
sudo apt remove -y mplayer
sudo pip uninstall gi
sudo pip uninstall tornado
sudo pip uninstall hyper