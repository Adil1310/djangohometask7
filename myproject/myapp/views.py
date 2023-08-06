from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User

# Create your views here.

def get_id_info(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)
        user_info = user.get_id()
        return HttpResponse(user_info)
    except User.DoesNotExist:
        return HttpResponse('User ID does not exist.')

def totalsum(request):
    total_sum = User.sum()
    return HttpResponse(f'Sum of all ages: {total_sum}')
    