from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home page view
def home(request):
    return HttpResponse("Welcome to the Django Backend!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Ensure your app URLs are included
    path('', home),  # Add this line to handle the root URL
]
