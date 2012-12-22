from __future__ import absolute_import
from   celery   import Celery

CELERY_BROKER = 'amqp://guest@localhost:5672//'

celery = Celery('tasks',
                backend = 'amqp',
                broker  = CELERY_BROKER,
                include = ['proj.tasks'])

# Optional configuration, see the application user guide.
celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)
