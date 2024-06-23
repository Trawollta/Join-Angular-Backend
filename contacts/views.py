from rest_framework import generics
from .models import Contact
from .serializers import ContactListSerializer
from django.contrib.auth.models import User

class ContactList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ContactListSerializer

# wofür diesen Endpunkt?
class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
