from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.TextField(verbose_name="Title of note", null=False, db_comment="title of the note")
    content = models.TextField(verbose_name="Content of the note")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title

class TextBlock(models.Model):
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='text_blocks')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']