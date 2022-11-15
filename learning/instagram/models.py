from django.db import models
from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True)   # 필드에 이미지 저장 경로(문자열)가 저장됨
    # python은 스크립트 언어기에, 위에서부터 차례대로 코드를 실행시키며 class를 인식한다. 그렇기에, Post 보다 아래에 있는 Tag class는 문자열로 지정.
    tag_set = models.ManyToManyField('Tag', blank=True) # Tag가 없는 Post도 있기에 blank=True
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    # Java의 toString과 유사
    def __str__(self):
        # return f"Post object ({self.id})"
        return self.message

    def message_length(self):
        return len(self.message)
    message_length.short_description = "메시지 글자 수"

    def get_absolute_url(self):
        # return reverse('instagram:post_detail', args=[self.pk])
        return resolve_url('instagram:post_detail', pk=self.pk)

# Post : Comment = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True}) # DB에 post_id라는 필드가 생성됨
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name