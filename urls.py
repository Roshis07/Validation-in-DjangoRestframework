from django.urls import path, include
from .views import user_list, user_details  # Import your view

urlpatterns = [

    path('users_List/', user_list, name='user-details'),
    path('<int:pk>/', user_details, name='user-details'),
    # Use the view function without quotes
]
