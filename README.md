# Server Monitor - Deploy

1. Update the Server

```bash
sudo apt update
sudo apt upgrade
```

2. Set up a Virtual Environment for Python

```bash
sudo apt install python3.8-venv
mkdir ServerMonitor
cd ServerMonitor && mkdir env
python3 -m venv /root/ServerMonitor/env/ve
```

3. Activate the virtual environment

```bash
source /root/ServerMonitor/env/ve/bin/activate
```
> `which python`
> 
> Verify that you are working from within your virtual environment by taking a look at where the Python binary is located.

4. Install the Django web framework using the pip package installer.

```bash
pip install django
```

5. Clone the project from remote

```bash
cd /root/ServerMonitor/ && git clone https://github.com/cattomgithub/ServerMonitor.git
```

6. Test the django Server

```bash
ufw allow 8000
cd ServerMonitor
python manage.py runserver 0.0.0.0:8000
```

7. Install uWSGI

```bash
sudo apt install python3.8-dev gcc
pip install uwsgi
```

8. Test uWSGI with django

```bash
uwsgi --http :8000 --module public.wsgi
```
