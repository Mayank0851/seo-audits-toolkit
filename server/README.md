## Introduction

Useful endpoints:

- https://localhost:8000/admin -> Django Admin framework
- https://localhost:8000/ -> API REST framework

## Installation

- Redis-server running

### Django

```Bash
cd osat
pip3 install -r requirements.txt
pip3 install celery
```

### Database

Go to `osat/settings.py`
Change the values you need in

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'osat',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "TEST"),
        'HOST': 'osat.ctcghdbvsxw2.eu-west-3.rds.amazonaws.com',
        'PORT': '5432',
    }
}
```

### Running

**You need to have a Redis server running on your machine.**

If you want to run the project.

- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

And in another terminal run:

`celery -A osat  worker -l info`

`celery -A osat beat -l info`

### Changes to models

If you make a change to a model simply run

- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

### Creating a new plugin

- `python3 manage.py startapp <nameofyourplugin>`

This will create a new folder.

In `Django_SEO/settings.py` add your app in INSTALLED_APPS:

```Python
INSTALLED_APPS = [
    'extractor.apps.ExtractorConfig', ### This is the app from the Extractor Folder
    ....
```

Copy and modify the code from extractor to help you start:

- admin.py -> Change the model
- serializers -> Adapt the create method with your celery task
- tasks -> Modify to suit your needs
- Views -> Change the filter and ordering fields

Then you need to add your app to `osat/urls.py` ->

````Python
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'api/extractor', ExtractorViewSet)
### Add your root here

## Troubleshooting Network Errors

If you are facing network errors, particularly during login, follow these steps to resolve the issue:

### 1. Check Docker Network Configuration

The network error can occur if Docker containers are not on the same network or if the network configuration is missing. Follow these steps:

1. **Inspect Docker Network**: Ensure that your web, database, and Redis services are on the same network.

2. **Update Docker Compose**: Ensure all services are in the same custom network in your `docker-compose.yml`.


3. **Rebuild Containers**: After making changes, rebuild and restart the containers:
    ```bash
    docker-compose down
    docker-compose up --build
    ```

### 2. Verify Database and Redis Connection

Ensure that Django is correctly connecting to the PostgreSQL database and Redis. Check these settings:

1. **Database Settings**: Make sure the database host is set correctly in `settings.py`. For Docker, it should match the container name or IP:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'osat',
            'USER': 'postgres',
            'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "TEST"),
            'HOST': 'db',  # Adjust based on your Docker setup
            'PORT': '5432',
        }
    }
    ```

2. **Redis Settings**: Update the Celery settings to point to the Redis container:
    ```python
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    ```

3. **Test Connections**: Check if the containers are running and the services are reachable:
    ```bash
    docker ps

### 3. Ensure Correct Port Mapping

Verify that Docker is correctly exposing the ports for the web application and services:

1. **Port Mapping**: In `docker-compose.yml`, ensure the ports are correctly mapped:
    ```yaml
    services:
      web:
        ports:
          - "8000:8000"
      db:
        ports:
          - "5432:5432"
      redis:
        ports:
          - "6379:6379"
    ```

### 4. Update Django's Allowed Hosts

Ensure that Django is configured to accept connections from the correct hosts.

1. **Allowed Hosts**: In `settings.py`, update the `ALLOWED_HOSTS` to include the correct IPs or hostnames:
    ```python
    ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']
    ```
````
