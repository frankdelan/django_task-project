from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Task


# Create your views here.
def show_page(request) -> HttpResponseRedirect | HttpResponse:
    """Display main page and send data to database"""
    if request.method == 'POST':
        if request.POST.get('id'):
            index = request.POST['id']
            Task.objects.filter(pk=int(index)).delete()
            return HttpResponseRedirect(reverse('main_page'))
        else:
            title: str = request.POST['task_name']
            info: str = request.POST['task_info']
            user: str = request.user
            query = Task(task_name=title, task_info=info, task_user=user)
            query.save()
            return HttpResponseRedirect(reverse('main_page'))
    tasks = Task.objects.all()
    return render(request, 'page.html', {'tasks': tasks})
