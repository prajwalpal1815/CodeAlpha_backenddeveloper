from rest_framework import generics
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RegisterEvent(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
