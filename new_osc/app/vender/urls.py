from django.urls import path,include
from .views import (
    VenderView,
)
urlpatterns = [
    path(
        'vender/',
        VenderView,
        name='vender'
    ),
]