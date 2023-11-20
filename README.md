# e-Citizen Single Signon Integration

A demo on how to integrate the eCitizen single signon into a django web application.

## Getting Started

- Run following command in your terminal to clone this repository

```
git clone https://github.com/eCitizen-Kenya/oauth-django.git
```

If you are using SSH, use the following command

```
git clone git@github.com:eCitizen-Kenya/oauth-django.git
```


When you run the commands successfully, you should have a local version of this repository.

### Prerequisites

- A computer with Python 3 install. Check [here](https://realpython.com/installing-python/) for
  further [instructions](https://realpython.com/installing-python/)
- Access to the Internet
- An IDE of your choice e.g. Pycharm, VS Code, Sublime Text

### Installing
Navigate inside the project root folder and create a .env file. Inside it add the following keys with their respective values as provided by the eCitizen team:
```
SECRET_KEY=<Your Django Secret Key>
ECITIZEN_CLIENT_ID=<Your eCitizen client ID>
ECITIZEN_CLIENT_SECRET=<Your eCitizen Secret>
```

Navigate to ```settings.py``` and scroll to the bottom to find the ECITIZEN settings variable. Replace the following with your own values:
```
REDIRECT_URL_ON_LOGIN -> This should be a link to where the user should be redirected to after successfully logging in

ECITIZEN_REDIRECT_URI -> This should be a link to where ecitizen should send the authorization code used to request an access token

```

After this create a virtual environment and activate it. After this, run ```pip install -r requirements.txt``` to install the project dependencies. You can now run ```python3 manage.py migrate``` then ```python manage.py runserver``` to start the server.  Once the server is running, open your browser and enter ```http://localhost:8000``` and choose login with ecitizen. After successfull login, you should be redirect to REDIRECT_URL_ON_LOGIN in your settings.py.