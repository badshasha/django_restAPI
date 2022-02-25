@api_view(['GET','PUT','DELETE'])
def drinkinfo(request,id):

    # validate information and find the object
    # try:
    #     drink = Drink.objects.filter(pk=id)
    # except Drink.DoesNotExists:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    drink = get_object_or_404(Drink,pk=id)

    if request.method == 'GET':
        serialize = DrinkSerializer(drink)
        return Response(serialize.data)


    elif request.method == 'PUT':

        serializer = DrinkSerializer(drink , data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':        
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
