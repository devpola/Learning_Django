from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # PostForm에서 author을 제외한 필드의 유효성 검사만 진행했기에, author가 없어도 통과 했었음.
#             # form.save 시, commit을 False로 주어, post.save를 보류하고 / author을 따로 지정
#             post = form.save(commit=False)  # commit False로 줄 경우, 모델 인스턴스.save() 호출이 되지 않음
#             post.author = request.user  # 현재 로그인되어있는 User Instance를 대입
#             post.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#     })
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#     })

# @method_decorator(login_required, name='dispatch')
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
class PostDetailView(DetailView):   # template_name 지정되지 않았다면, 모델명으로 템플릿 경로 유추(instagram/post_detail.html)
    model = Post    # 모델명소문자 이름의 QuerySet을 template에 넘겨줌 / object라는 이름으로도 접근 가능
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 작성자 Check Tip
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#     })
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, '포스팅을 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # success_url = '/instagram/'
    success_url = reverse_lazy('instagram:post_list')


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")