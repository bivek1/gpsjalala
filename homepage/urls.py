from django.urls import path
from .views import *
app_name = "agent"



urlpatterns = [

    path('', homepage, name = "homepage"),
    path('login/', Login, name ="login"),
    path('vechile-details/<int:id>/<int:track_no>/fullinformation', VechileDetails, name ="vechile"),
    
]