# portfolio/managers.py

from django.db import models

class PublishedProjectManager(models.Manager):
    def get_query_set(self):
        return super(PublishedProjectManager, self).get_query_set().filter(status=self.model.STATUS_PUBLISHED)

class FeaturedProjectManager(models.Manager):
    def get_query_set(self):
        return super(FeaturedProjectManager, self).get_query_set().filter(status=self.model.STATUS_PUBLISHED).filter(featured=True)
