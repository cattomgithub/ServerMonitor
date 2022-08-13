# Server Monitor

## Description

## Directory Structure

## Usage

```bash
sudo apt -y update && apt -y upgrade && apt -y autoremove
sudo apt -y install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3.8-venv python3.8-dev gcc

cd /root && git clone https://github.com/cattomgithub/ServerMonitor.git
cd ServerMonitor && mkdir env
python3 -m venv /root/ServerMonitor/env

source /root/ServerMonitor/env/bin/activate

pip install -r requirements.txt
```

### Public panel
```bash
cd /root/nginx_data/monitor && mkdir static
cd /root/ServerMonitor/ && python manage.py collectstatic

cd /root/ServerMonitor/env/ && mkdir public_vassals
sudo ln -s /root/ServerMonitor/uwsgi/public_uwsgi.ini /root/ServerMonitor/env/public_vassals/

sudo ln -s /root/ServerMonitor/systemd/public.uwsgi.service /etc/systemd/system/public.uwsgi.service
sudo systemctl daemon-reload
systemctl enable public.uwsgi.service
systemctl start public.uwsgi.service

sudo cp /root/ServerMonitor/uwsgi/uwsgi_params /root/nginx_data/monitor/uwsgi_params
```

### Main
```bash
source /root/ServerMonitor/env/bin/activate
cd /root/ServerMonitor/env/ && mkdir main_vassals
sudo ln -s /root/ServerMonitor/uwsgi/main_uwsgi.ini /root/ServerMonitor/env/main_vassals/
sudo ln -s /root/ServerMonitor/systemd/main.uwsgi.service /etc/systemd/system/main.uwsgi.service
sudo systemctl daemon-reload
systemctl enable main.uwsgi.service
systemctl start main.uwsgi.service
```

### Node
```bash
sudo ln -s /root/ServerMonitor/systemd/node.monitor.service /etc/systemd/system/node.monitor.service
sudo systemctl daemon-reload
systemctl enable node.monitor.service
systemctl start node.monitor.service
```

uwsgi -s /root/nginx_data/monitor/main.sock --manage-script-name --mount /root/ServerMonitor=main:app

   git fetch --all &&  git reset --hard origin/master && git pull