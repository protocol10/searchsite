from django.db import models

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=100)
	phone_no=models.CharField(max_length=100)
	city=models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
