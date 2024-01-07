from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
count = 0


# Create your views here.
@api_view(['GET', 'POST'])
def test(request):
    global count
    if request.method == 'GET':
        data = count
    elif request.method == 'POST':
        count += 1
        data = count
    return Response({'data': data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def reset(request):
    global count
    if request.method == 'POST':
        count = 0
    return Response({'data': count}, status=status.HTTP_200_OK)