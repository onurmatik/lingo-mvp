from django.contrib import admin
from django.urls import path
from lingo.meetings.views import meeting_create, meeting_list


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', meeting_list, name='index'),
    path('meetings/create/', meeting_create, name='meeting_create'),
]
