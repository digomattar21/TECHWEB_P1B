from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

class Note(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    tag = models.ForeignKey(to=Tag,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return ('{0}.{1}').format(self.id, self.content)


    

