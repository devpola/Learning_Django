from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Post


# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#     })

class PostListView(ListView):
    model = Post    # 모델명소문자_list 이름의 QuerySet을 template에 넘겨줌 / object_list로도 접근 가능
    pagenate_by = 10    # 페이징 처리 지원 -> 'page' 이름의 query string으로 사용가능 ex) ?page=2

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(message__icontains=q)
        return qs


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })

class PostDetailView(DetailView):
    model = Post    # 모델명소문자 이름의 QuerySet을 template에 넘겨줌 / object라는 이름으로도 접근 가능
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")