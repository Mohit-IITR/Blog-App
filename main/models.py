from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tags(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags

class Blogs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)
    title = models.CharField(max_length=200, default="")
    small_desc= models.TextField()
    full_content = models.TextField()
    img= models.ImageField(upload_to="images/")

    def __str__(self):
        return self.author.name
