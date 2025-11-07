from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.TextField(verbose_name="Title of note", null=False, db_comment="title of the note")
    content = models.TextField(verbose_name="Content of the note")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title