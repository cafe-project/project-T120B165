from django.urls import path
from .views import registration, example_view, HelloView

urlpatterns = [
    path('register/', registration, name='register'),
    path('example/', example_view, name='example'),
    path('hello/', HelloView.as_view(), name='hello'),
]