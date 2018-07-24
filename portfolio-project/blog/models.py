from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.name

    def summary(self):
        return self.text[:100]

    def pub_date(self):
        return self.created_at.strftime('%Y-%m-%d')
