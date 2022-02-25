
from rest_framework import serializers
from .models import Drink
# python object to json contain all the information

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:  # targeting infor
        model = Drink
        fields = ['id','name','description']
