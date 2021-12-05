from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.views import Response


class HelloApiView(APIView):
    """api view de prueba"""
    def get(self, request, format= None):
        an_apiview= [
            'METODOS HTTP COMO FUNCIONES , (GET,POST,PATCH,PUT,DELETe)',
            'ES SIMILAR'
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})