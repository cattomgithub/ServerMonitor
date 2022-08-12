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