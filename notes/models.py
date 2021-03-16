from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return ('{0}.{1}').format(self.id, self.content)