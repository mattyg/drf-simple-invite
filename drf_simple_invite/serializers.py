from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})
