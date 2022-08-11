import requests
import json

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.core import serializers
from random import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializer import AccountSerializer, DataHandlerSerializer, DestinationSerializer, HeadersSerializer
from .models import Account, Destination, Headers

# Create your views here.


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == "GET":
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, pk):
    account = get_object_or_404(Account, account_id=pk)
    if request.method == "GET":
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = AccountSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        account.delete()
        return Response("Record delted")


@api_view(['GET', 'POST'])
def destination_list(request):
    if request.method == "GET":
        queryset = Destination.objects.all()
        serializer = DestinationSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DestinationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, id=pk)
    if request.method == "GET":
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = DestinationSerializer(destination, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        destination.delete()
        return Response("Record delted")


@api_view(['GET', 'POST'])
def header_list(request):
    if request.method == "GET":
        queryset = Headers.objects.all()
        serializer = HeadersSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = HeadersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def header_detail(request, pk):
    header = get_object_or_404(Headers, id=pk)
    if request.method == "GET":
        serializer = HeadersSerializer(header)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = HeadersSerializer(header, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        header.delete()
        return Response("Record delted")


@api_view(['GET'])
def get_accounts_destination(request, pk):
    account = Account.objects.get(account_id=pk)
    queryset = Destination.objects.filter(account=account)
    serializer = DestinationSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def data_handler(request):
    if request.method == "POST":
        print("-------------printing------------------")
        # print(request.headers)
        # print(request.data)
        data = request.data
        if request.headers['Authorization']:
            token = request.headers['Authorization']
            print(token)

            app_secret_token = token.split(" ")[1]
            print(app_secret_token)
            account = Account.objects.get(app_secret_token=app_secret_token)
            destinations = Destination.objects.filter(account=account)
            for destination in destinations:
                url = destination.url
                print(destination.headers.app_id)
                headers = {
                    "APP_ID": f"{destination.headers.app_id}",
                    "APP_SECRET": f"{destination.headers.app_secret}",
                    "ACTION": f"{destination.headers.action}",
                    "Content-type": f"{destination.headers.content_type}",
                    "Action": f"{destination.headers.action}",
                }

                if destination.http == "GET":
                    print(is_json(data))
                    if is_json(data):
                        r = requests.get(f"{url}?query=" %
                                         json.dumps(data), headers=headers)
                        return Response(r.status_code)
                    else:
                        return Response({"error": "Invalid Data"}, status=status.HTTP_406_NOT_ACCEPTABLE)
                elif destination.http == "POST" or destination.http == "PUT":
                    r = requests.get(url, data=json.dumps(
                        data), headers=headers)
                    print(r.status_code)
                    return Response(r.status_code)
        else:
            return Response({"error": "Unauthenticate user"}, status=status.HTTP_401_UNAUTHORIZED)
