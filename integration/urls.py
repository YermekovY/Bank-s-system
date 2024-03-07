from django.urls import include, path
from . import views


urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path("models/", views.models, name="models")
]
