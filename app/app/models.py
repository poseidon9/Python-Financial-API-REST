# import the standard Django Model
# from built-in library
import uuid
from django.db import models

# declare a new model with a name "Company"
class Company(models.Model):
		# fields of the model
	UIID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 100, blank = True)
	symbol = models.CharField(max_length = 10)
	market_values = models.TextField()
	last_modified = models.DateTimeField(auto_now_add = True)
	img = models.ImageField(upload_to = "images/", null = True)
 
		# renames the instances of the model
		# with their title name
	def __str__(self):
		return self.title