from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from .models import Meeting


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['language', 'time', 'meeting_url', 'password']


@login_required
def meeting_create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.host = request.user
            meeting.save()
            return redirect('index')
    else:
        form = MeetingForm()
    return render(
        request,
        template_name='meetings/meeting_form.html',
        context={
            'form': form,
        }
    )


def meeting_list(request):
    return render(
        request,
        template_name='meetings/meeting_list.html',
        context={
            'meetings': Meeting.objects.filter(time__gt=timezone.now()),
        }
    )
