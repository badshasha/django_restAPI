from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view('GET','POST')
def drinkList(request):
    # get all the drinks
    all_drinks =  Drink.objects.all()

    # send to client
    serializer = DrinkSerializer(all_drinks, many=True)
    return JsonResponse({'data':serializer.data}, safe=False)

    # add decorator 
