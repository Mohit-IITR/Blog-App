from rest_framework import serializers
from .models import *

class blogDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogs
        fields = '__all__'

class tagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
