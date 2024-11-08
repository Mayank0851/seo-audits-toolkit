<p align="center"><img src="./docs/images/OSAT.png" width="180px" /></p>

# Open source Audits Toolkit

**OSAT** is a collection of tools created help you in your quest for a better website. All of these tools have been grouped into a single web app.

I've grown tired of SEO agencies making us pay hundreds of euros for simple tools. I decided to develop **OSAT** to help users find issues on their website and increase their SEO for free.

<p align="center"><img src="./docs/images/osat-demo.gif" width="700px" /></p>

## Why you need it

- It's **free**, easy and open source.
- It has a growing list of features
- It's easy to install

## Features

- **Authentification** - A fully featured authentification system for the front & back
- **RBAC/Organizations** - Create different organizations and give different access to each org to your users.
- **Lighthouse Score** - Run [Lighthouse](https://developers.google.com/web/tools/lighthouse) Audits and keep track of your scores
- **SERP Rank** - Get the rank of your website on google for specific queries
- **Keywords Finder** - Find all the keywords of an article.
- **Extract Headers/Links/Images** - Easily extract all the links on your website and their status codes, the headers of a page and all the images.
- **Sitemap Extractor** - Extract all the urls of a website from its sitemap
- **Summarizer** - Summarize any text from any length. Awesome for excerpt !
- **Security Audit** - Audit Headers, Redirect, etc to make sure you website is secure.

## Demo

Go to [demo.primates.dev](https://demo.primates.dev) <br>
**Login**: demo <br>
**Password**: demodemo <br>

Admin part is [api.primates.dev/admin](https://api.primates.dev/admin)

## Installation

```Bash
git clone https://github.com/StanGirard/seo-audits-toolkit
cd seo-audits-toolkit
docker-compose pull ## docker-compose build if you want to build it on your own
docker-compose --env-file .env-example up -d
```

Init the project

```Bash
docker exec -it osat-server python manage.py flush
docker exec -it osat-server python manage.py loaddata init_data.json
```

## Dashboard

You can access the dashboard by going to [localhost:3000](http://localhost:3000)

**Login**: admin
**Password**: admin

## Config

If needed create a `.env` file with information that you would like to change

## Configuration

### Create organization

You need to go to `Org -> Organization` and create a new organization. You can create as many as you want. Organization are used in order to implement RBAC in the project and only display information about an organization to users of this organization. Here is a quicklinkg to access it [http://localhost:8000/admin/org/website/](http://localhost:8000/admin/org/website/)

### Add user to organization

Once your organization is created. You need to add your users to this organization.
Go to `Organizations -> Organizations Users` and add your users to the organization you want. [http://localhost:8000/admin/organizations/organizationuser/](http://localhost:8000/admin/organizations/organizationuser/)

## Useful Links

- **Webapp** [http://localhost:3000](http://localhost:3000)
- **Admin Dashboard** [http://localhost:8000/admin](http://localhost:8000/admin)
- **Swagger like interface** [http://localhost:8000](http://localhost:8000)

## Contributions

Please feel free to add any contribution.
If you've been working on a script that could be integrated in this app. Please feel free to do it. Don't hesitate to open issues to ask questions. I've tried to document the code as much as I could to ease the integration

### Backend

You can just add a django module and I'll take care of intregrating it in the front.

### Frontend

I've used React Admin to build the front-end. If you want to help me improve the UI or add new functionnalites. Please feel free to contribute.

## Disclaimers

I'm not a python nor a frontend developer.

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
   ```

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

```









```
