from django.urls import path
from .views import fan_control, consumption_query

urlpatterns = [
    path('fan_control/', fan_control, name='fan_control'),
    path('consumption_query/', consumption_query, name='consumption_query'),
]
