from rest_framework import fields, serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','phoneno','alternateno']
        extra_kwargs = {'password': {'write_only': True}}