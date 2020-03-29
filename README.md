### Install system dependencies
```
sudo apt-get install python3.6-dev libmysqlclient-dev
```
### Clone project from Git

```
git clone --progress  --single-branch --branch <branch> <repo name>
```

### Create Python virtual environment in side the cloned git repo

```
mkdir vm
virtualenv -p python3.6 vm/
source vm/bin/activate

```

### Install Django and other dependencies
```
python -m pip install -r requirements.txt
```
### Run TXM
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```