from django.urls import path
from profiles_api import views
from django.urls import path


urlpatterns = [
   
    path('hello-view/',views.HelloApiView.as_view())
]
