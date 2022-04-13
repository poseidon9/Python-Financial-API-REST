from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Company

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email']

# Serializers define the API representation.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Company
		fields = ['name', 'description', 'symbol', 'market_values', 'img']
