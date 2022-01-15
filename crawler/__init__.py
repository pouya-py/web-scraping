from .celery_inst import app as celery_app


# this ensure that whenever django website load up it will load celery too.
__all__ = ('celery_app',)   