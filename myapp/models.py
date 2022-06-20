from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class OrderDetails(models.Model):

    SERVICES_TYPE = [
    ('DC', 'Dryclean'),
    ('IR', 'IRON'),
    ('WS', 'Washing'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=3, choices=SERVICES_TYPE)
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    amount = models.FloatField()

    def __str__(self):
        return self.service_type



