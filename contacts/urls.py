from django.urls import path
from .views import ContactList, ContactDetail


urlpatterns = [
    path('api/contacts/', ContactList.as_view(), name='contact-list'),
    path('api/contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
]