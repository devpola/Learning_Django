from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# # 등록법 1
# admin.site.register(Post)
#
# # 등록법 2
# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)

# 등록법 2 변형 -> 장식자 사용
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'photo_tag', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    search_fields = ['message']
    list_filter = ['is_public']

    def photo_tag(self, post):
        if post.photo:  # post에 photo 데이터가 없을 때, url 데이터 접근 시 ValueError 발생
            return mark_safe(f'<img src="{post.photo.url}" style="width:75px" />')     # mark_safe를 통해, 문자열을 태그로 인식
        return None

    # admin에서도 custum field 생성 가능 - model에서 정의한 custom field보다 우선순위 높음
    # def message_length(self, post):
    #     return len(post.message)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass