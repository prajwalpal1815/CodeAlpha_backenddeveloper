from django.urls import path
from .views import EventList, EventDetail, RegisterEvent

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('register/', RegisterEvent.as_view()),
]

