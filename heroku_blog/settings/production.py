from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config(
    default='postgres://1uafnjhscmsbkcg:082e94145f842ea5a330676463889164505b99ef6a954a57114e0bf51985a80e@ec2-54-235-120-39.compute-1.amazonaws.com:5432/d1am9vqieen0vu'
)
