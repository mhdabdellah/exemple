from django.urls import include, path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('details/<int:id>', views.vehiculedetails, name='details'),
]