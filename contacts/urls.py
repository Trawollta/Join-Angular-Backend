from django.urls import path
from .views import ContactList, ContactDetail, ContactCreate, ContactDelete

urlpatterns = [
    path('api/contacts/', ContactList.as_view(), name='contact-list'),
    path('api/contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    path('api/contacts/create/', ContactCreate.as_view(), name='contact-create'),
    path('api/contacts/delete/<int:pk>/', ContactDelete.as_view(), name='contact-delete'),
]
