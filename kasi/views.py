from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Stories, Comment
from .forms import CommentForm
from django.views.generic import TemplateView

# Create your views here.


def homePage(request):
    template_name = 'kasi/home.html'
    story_list = Stories.objects.order_by('pk')
    comments = Comment.objects.order_by('pk')
    return render(request, template_name, {'story_list':story_list, 'comments':comments})

def comment(request):
    if request.method =='POST':
       form = CommentForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('kasi:home')
    else:
        form = CommentForm()
        return render(request, 'kasi/form.html', {'form':form})
