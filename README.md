# Setup project

## 1. Clone repo

Use [GitHub Desktop](https://desktop.github.com/) to clone the repository.

## 2. Setup virtualenv

`virtualenv venv`

## 3. Activate virtualenv

OS X / Linux:
`. venv/bin/activate`

Windows:
`venv\script\activate`

If success, prompt should start with: `(venv)`

## 4. Install Django and dependencies

`pip install -r requirements/local.txt`

## 5. Run Django

```
cd project
./manage.py runserver
```
