from rest_framework import serializers
from account.models import User


class RegisterSerializer(serializers.modelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta():
        model = User
        fields = ('username', 'email', 'birth_year', 'password')
