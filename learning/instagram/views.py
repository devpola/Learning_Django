from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
    })

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'instagram/post_detail.html', {
        'post': post
    })

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")