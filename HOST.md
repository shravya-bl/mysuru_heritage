# HOSTING GUIDE (PERSONAL USE) - MYSURU HERITAGE

This version is simplified for your own private/personal use.
It intentionally skips advanced production hardening and secret-key environment setup.

## 1) What You Need

- Your project folder (this one)
- GitHub account
- Render account
- Working virtual environment

## 2) Prepare Project Locally

From the project root:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe manage.py makemigrations
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py check
```

## 3) Keep Settings Simple

In `mysuru_heritage/settings.py`, for personal use hosting, keep:

```python
DEBUG = True
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']
```

Also ensure static and media are set:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 4) Create `build.sh` in Root

Create a file named `build.sh` with:

```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

## 5) Push to GitHub

```powershell
git add .
git commit -m "setup hosting"
git push origin main
```

## 6) Deploy on Render

1. Go to Render Dashboard.
2. Click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Use these values:
   - Environment: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn mysuru_heritage.wsgi:application`
5. Click **Create Web Service**.

## 7) After Deploy

Open your deployed URL:

- `https://your-service-name.onrender.com/`

Create admin user once (Render Shell):

```bash
python manage.py createsuperuser
```

Then test:

- `/` login page
- `/landing/`
- `/places/`
- `/blog/`
- `/gallery/`
- `/admin/`

## 8) Personal-Use Notes

- SQLite is okay for your personal usage.
- If Render restarts/redeploys, uploaded files may get reset on free setup.
- If that becomes a problem, later you can move media to Cloudinary.

## 9) Quick Fixes

- If static files are missing: run `collectstatic` again.
- If app fails after deploy: check Render logs.
- If migration errors come: run `python manage.py migrate` in Render shell.
