from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
    })

def post_detail(request, pk):
    pass

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")