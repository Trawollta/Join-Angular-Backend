from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Contact
from .serializers import ContactListSerializer, ContactCreateSerializer, ContactUpdateSerializer, ContactDeleteSerializer

class ContactList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ContactListSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ContactUpdateSerializer

class ContactCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ContactCreateSerializer

class ContactDelete(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDeleteSerializer

    def delete(self, request, *args, **kwargs):
        try:
            contact = User.objects.get(pk=kwargs['pk'])
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response({"detail": "No Contact matches the given query."}, status=status.HTTP_404_NOT_FOUND)