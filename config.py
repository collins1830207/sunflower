# -*- coding:utf-8 -*-
import os

SECRET_KEY = 'collins123321'

SITE_TITLE = '向日葵'
SITE_SUBTITLE = '活出自己'

POST_PATH = './source/_posts/'
PAGE_PATH = './source/_pages/'
GENERATED_PATH = './web/static/generated/'
DEFAULT_CATEGORY = 'default category'
DEFAULT_TAG = ['other']

BLOG_DAT = './web/static/generated/data.dat'

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME') or 'web'
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD') or 'password'

