from dataclasses import field
from django.forms import ModelForm

from .models import *


class OrderDetailsForm(ModelForm):
    class Meta:
        model = OrderDetails
        fields = '__all__'
