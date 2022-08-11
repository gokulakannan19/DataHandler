from rest_framework import serializers
from .models import Account, Destination, Headers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'account_name',
                  'email_id', 'website', 'app_secret_token']


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'url', 'http', 'account', 'headers']


class HeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headers
        fields = ['app_id', 'app_secret', 'action',
                  'content_type', 'accept', 'destination']


class DataHandlerSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=255)
