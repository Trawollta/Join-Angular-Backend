from django.urls import path
from .views import ContactList, ContactDetail
# from .views import CurrentUserView

urlpatterns = [
    path('api/contacts/', ContactList.as_view(), name='contact-list'),
    path('api/contacts/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
    # path('current_user/', CurrentUserView.as_view(), name='current_user'),
]