"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.urls import path, include
from rest_framework import routers
from app import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
	#Testing
#router.register(r'users', views.UserViewSet)

urlpatterns = [
		#Testing
	#path('', include(router.urls)),
	
	path('api-auth/', include('rest_framework.urls')),
    path('companies/', views.CompanyList.as_view()),
    path('companies/<str:pk>', views.CompanyDetail.as_view()),
    path('test/', views.Test.as_view())
]
