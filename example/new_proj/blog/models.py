from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField(verbose_name="Title of blog", null=False, db_comment="title of the blog")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title