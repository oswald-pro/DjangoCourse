# DjangoCourse
Django tutorials for beginners


## Steps
### Step1: Create a project directory
### Step2: Create a virtualenv inside the project dir
```
pip install virtualenv
```
```
virtualenv env_site
```
### Step3: activate the virtualenv
on macOS
```
source env_site/bin/activate
```
### Step4: Install Django insite the project dir
```
pip install django
```
### Step5: Start the Django project 
for my case project_name = django001
```
django-admin startproject django001
```

### Step6: access the django001 dir and list files
```
cd django001
```
then
```
ls
```
### Step7: still from the django001 dir. run the project (manage.py file)
```
python manage.py runserver
```
### Step8: still from the django001 dir. let's create a new app
for my case app_name = africa
```
python manage.py startapp africa
```

## To make update to the DB
```
python manage.py makemigrations
```
## To make create to the DB
```
python manage.py migrate
```
## How to populate a DB using django shell
```
python manage.py shell
```
Example:
```
In [1]: from africa.models import Trip #import
In [2]: trip1 = Trip(origin="Congo Brazzaville", destination="Ghana", nights =2, price=5000) #define values
In [3]: trip1.save() # to save values
In [4]: trip1 # to display
```
## How to populate a DB using django admin GUI

#### Create a super user account
```
python manage.py createsuperuser
```
for my case username : oswald and password : 1234





















