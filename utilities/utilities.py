from os import getenv

def test_utility():
    print('Hello World!')


run_on = 'local'

ENVIRONMENT = 'production'

if ENVIRONMENT == 'production':
    URL = 'https://www.google.com/'
    USERNAME = 'production_user'
    PASSWORD = 'production_password'
elif ENVIRONMENT == 'development':
    USERNAME = 'development_user'
    PASSWORD = 'development_password'
elif ENVIRONMENT == 'qa':
    pass
else:
    USERNAME = 'default_user'
    PASSWORD = 'default_password'
