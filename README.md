# Server Monitor

## Description

## Directory Structure

## Usage

### Public panel
```bash
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt install python3.8-venv python3.8-dev gcc

cd /root && git clone https://github.com/cattomgithub/ServerMonitor.git
cd ServerMonitor && mkdir env
python3 -m venv /root/ServerMonitor/env

source /root/ServerMonitor/env/bin/activate

pip install django uwsgi

cd /root/nginx_data/monitor && mkdir static
cd /root/ServerMonitor/ && python manage.py collectstatic

cd /root/ServerMonitor/env/
mkdir uwsgi_vassals
sudo ln -s /root/ServerMonitor/uwsgi/public_uwsgi.ini /root/ServerMonitor/env/uwsgi_vassals/

sudo ln -s /root/ServerMonitor/systemd/emperor.uwsgi.service /etc/systemd/system/emperor.uwsgi.service
systemctl enable emperor.uwsgi.service
systemctl start emperor.uwsgi.service

sudo cp /root/ServerMonitor/uwsgi/uwsgi_params /root/nginx_data/monitor/uwsgi_params
```

### Main
```bash
source /root/ServerMonitor/env/bin/activate
pip install flask
```