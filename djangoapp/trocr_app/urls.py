from django.urls import path
from . import views
from . import urls
urlpatterns = [
    path('trocr/', views.TrocrEndpoint.as_view(), name='trocr'),
]
