from django.urls import path, re_path, register_converter
from . import views


class YearConverter:
    regex = r'20\d{2}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

register_converter(YearConverter, 'year')

app_name = 'instagram'

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # path('<int:pk>/', views.post_detail),    # 매핑된 Converter의 to_python에 맞게 변환된 값이 인자로 전달
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P20\d{2})/', views.archives_year),
    path('archives/<year:year>/', views.archives_year, name='post_archive'),
]