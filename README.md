# Server Monitor

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

This project is to practice Python and shell skills.


## Directory Structure
```
.
├── env
│   ├── bin
│   ├── public_vassals  # uWSGI vassals of public panel
│   ├── main_vassals    # uWSGI vassals of main
│   └── ...
├── main.py
├── main_wsgi.py        # main wsgi entrypoint
├── manage.py
├── node_config.py
├── node.py
├── panel
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates        # HTML file
│   └── ...
├── public
│   ├── settings.py      # Django config
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── random_secret_key.py
├── README.md
├── requirements.txt
├── server_monitor       # install script
├── systemd              # systemd service file
│   ├── main.uwsgi.service
│   ├── node.monitor.service
│   └── public.uwsgi.service
└── uwsgi                # uwsgi config
    ├── main_uwsgi.ini
    ├── public_uwsgi.ini
    └── uwsgi_params
```

## Usage

```bash
cd /root && git clone https://github.com/cattomgithub/ServerMonitor.git
cd ServerMonitor && chmod +x server_monitor
./server_monitor
```