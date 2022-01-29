from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	caption = models.TextField(default="",max_length=200)
	image = models.ImageField(blank=True, null=True)
	author = models.CharField(default="", max_length=120)

	def __str__(self):
		return self.title