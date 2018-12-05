from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    name = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.search_date)

