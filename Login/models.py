from django.db import models
from django.utils import timezone

# Create your models here.


class Example2(models.Model):
    none = models.CharField(max_length=256, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.none

    class Meta:
        db_table = 'Example2'