from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import serializers, models


# Create your views here.

@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def auto(request, id=None):
    match (request.method):
        case 'GET':
            autos = models.Auto.objects.all()
            serialized_autos = serializers.SerializedAuto(autos, many=True)
            return Response(serialized_autos.data, status=status.HTTP_200_OK)
        case 'POST':
            serializer = serializers.SerializedAuto(data=request.data, partial=False)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            autos = models.Auto.objects.all()
            serialized_autos = serializers.SerializedAuto(autos, many=True)
            return Response(serialized_autos.data, status=status.HTTP_201_CREATED)
        case 'PATCH':
            auto = models.Auto.objects.get(id=id)
            updated_auto = serializers.SerializedAuto(auto, data=request.data, partial=True)
            if updated_auto.is_valid():
                updated_auto.save()
            else:
                return Response(updated_auto.errors, status=status.HTTP_400_BAD_REQUEST)
            autos = models.Auto.objects.all()
            serialized_autos = serializers.SerializedAuto(autos, many=True)
            return Response(serialized_autos.data, status=status.HTTP_200_OK)
        case 'PUT':
            auto = models.Auto.objects.get(id=id)
            updated_auto = serializers.SerializedAuto(auto, data=request.data, partial=False)
            if updated_auto.is_valid():
                updated_auto.save()
            else:
                return Response(updated_auto.errors, status=status.HTTP_400_BAD_REQUEST)
            autos = models.Auto.objects.all()
            serialized_autos = serializers.SerializedAuto(autos, many=True)
            return Response(serialized_autos.data, status=status.HTTP_200_OK)
        case 'DELETE':
            auto = models.objects.get(id=id)
            auto.delete()
            autos = models.Auto.objects.all()
            serialized_autos = serializers.SerializedAuto(autos, many=True)
            return Response(serialized_autos.data, status=status.HTTP_200_OK)
        case _:
            return Response({
                "error": True,
                "msg": "Try again later"
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def owner(request, id):
    match (request.method):
        case 'GET':
            owners = models.Owner.objects.all()
            serialized_owners = serializers.SerializedOwner(owners, many=True)
            return Response(serialized_owners.data, status=status.HTTP_200_OK)
        case 'POST':
            return Response({}, status=status.HTTP_201_CREATED)
        case 'PATCH':
            return Response({}, status=status.HTTP_200_OK)
        case 'PUT':
            return Response({}, status=status.HTTP_200_OK)
        case 'DELETE':
            return Response({}, status=status.HTTP_200_OK)
        case _:
            return Response({
                "error": True,
                "msg": "Try again later"
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def autos_passport(request, id):
    match (request.method):
        case 'GET':
            autos_passport = models.AutosPassport.objects.all()
            serialized_autos_passport = serializers.SerializedAutosPassport(autos_passport, many=True)
            return Response(serialized_autos_passport.data, status=status.HTTP_200_OK)
        case 'POST':
            return Response({}, status=status.HTTP_201_CREATED)
        case 'PATCH':
            return Response({}, status=status.HTTP_200_OK)
        case 'PUT':
            return Response({}, status=status.HTTP_200_OK)
        case 'DELETE':
            return Response({}, status=status.HTTP_200_OK)
        case _:
            return Response({
                "error": True,
                "msg": "Try again later"
            }, status=status.HTTP_400_BAD_REQUEST)
