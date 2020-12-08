import json

from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from chat.models import Message
from .form import MessageForm

@login_required
def index(request):
    form = MessageForm()
    return render(request, 'chat/chat.html', {'form': form})

@login_required
def save(request):
    if request.is_ajax():
        if 'multipart/form-data' not in str(request.META.get('CONTENT_TYPE', '')):
            request.POST = json.loads(request.body.decode('utf-8'))
    message = Message()
    posted_files = None
    if request.FILES:
        posted_files = request.FILES
    message.message = request.POST.get('message')
    message.author = request.user
    if posted_files:
        message.image_file = posted_files.get('image')
    message.save()

    res = {'success': True, 'id': message.id}
    return HttpResponse(json.dumps(res))
