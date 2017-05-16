from django.db import models

# This contains the different category from which the
# Blog belongs to. category will be unique.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	def __unicode__(self):
		return self.name

# Creating a blog table. It contains the blog title, and the URL 
# associated with it
class Blog(models.Model):
	name = models.CharField(max_length = 400, unique=True)
	url = models.URLField()
	def __unicode__(self):
		return self.name