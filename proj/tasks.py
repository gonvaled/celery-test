from __future__                  import absolute_import
from   proj.celery               import celery

@celery.task
def add(x, y):
    return x + y

print "This should only be executed in the worker"
