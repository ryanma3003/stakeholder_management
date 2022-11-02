# Simindi

Simindi adalah aplikasi untuk melakukan kegiatan monitoring dan pengelolaan data stakeholder industri. Aplikasi ini dibangun dengan menggunakan django framework 4.11.

## Installation

Clone repositori.

```git
git clone https://github.com/ryanma3003/stakeholder_management.git
```

## Create your own virtual environment

```python
python3 -m venv venvsource 

#activate virtual environment
venv/bin/activate
```

## Install the requirements
```python
pip install -r requirements.txt
```

## Make your migrations
Sisakan hanya file ‘__init__.py’ dalam setiap folder migrations dalam app project.

Di dalam terminal jalankan perintah berikut
```python
$ python manage.py makemigrations
$ python manage.py migrate
```

## Create a new superuser
Dalam terminal lanjutkan perintah berikut
```python
$ python manage.py createsuperuser
```

## Running the app

```python
$ python manage.py runserver
```

## License