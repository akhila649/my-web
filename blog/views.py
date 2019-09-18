from django.shortcuts import render


def main(request):
    return render(request,'blog/main.html')

def wm_home(request):
    return render(request, 'blog/wm-home.html')

def upload(request):
    return render(request, 'blog/upload.html')

def feedback(request):
    return render(request, 'blog/feedback.html')
   

