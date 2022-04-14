from datetime import datetime

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from django.contrib.auth.models import User
from app.models import Company
from app.serializers import UserSerializer, CompanySerializer

import yfinance as yahooFinance

def errorLog(error_type, error_msg):
	#append to file without worrying about closing
	with open("error_log.txt", 'a') as error_file:
		error_file.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ":   " + error_type + "\n")
		for error_key in error_msg:
			if isinstance(error_key, list):
				error_file.write(error_key + ": " + error_msg[error_key][0] + "\n")
			else:
				error_file.write(error_key + "\n")
		error_file.write("\n")




class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]



class CompanyList(APIView):
	"""
	List all companies, or create a new company.
	"""
	def get(self, request, format=None):
		companies = Company.objects.all()
		serializer = CompanySerializer(companies, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CompanySerializer(data=request.data)
		if serializer.is_valid():
			# Here We are getting the Ticker financial information
			# We need to pass a symbol as an argument for that
			ticker = yahooFinance.Ticker(request.data["symbol"])
			if len(ticker.info.keys()) > 3: 
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				errorLog("POST", "Symbol " + request.data["symbol"] + " is not registered in the NY Stock Exchange")
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		errorLog("POST", serializer.errors)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(APIView):
	"""
	Retrieve, update or delete a company instance.
	"""
	def get_object(self, pk):
		try:
			return Company.objects.get(pk=pk)
		except Company.DoesNotExist:
			errorLog("404", "Company " + pk + " not found!")
			raise Http404

	def get(self, request, pk, format=None):
		company = self.get_object(pk)
		company = CompanySerializer(company)
		return Response(company.data)

	def put(self, request, pk, format=None):
		company = self.get_object(pk)
		serializer = CompanySerializer(company, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		errorLog(serializer.errors)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		company = self.get_object(pk)
		company.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class Test(APIView):
	"""
	test purposes
	"""
	def get(self, request, format=None):
		return Response(status=status.HTTP_200_OK)