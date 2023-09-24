from django.urls import path, include
from .views import (
    FileAPIView,
)

urlpatterns = [
    path('upload/', FileAPIView.as_view({'post': 'upload'})),
    path('files/', FileAPIView.as_view({'get': 'list'}))
]
