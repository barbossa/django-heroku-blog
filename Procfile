web: gunicorn heroku_blog.wsgi --log-file -
worker: celery worker -A heroku_blog -E -l info