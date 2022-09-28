from django.db import models

class Users_db(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=40)

# Create your models here.
