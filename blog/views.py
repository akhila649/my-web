from django.shortcuts import render
from .models import Post

def post_list(request):
    posts=Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
    return render(request,'blog/main.html',{'posts':posts})

# Create your views here.
