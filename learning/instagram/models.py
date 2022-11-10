from django.db import models

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True)   # 필드에 이미지 저장 경로(문자열)가 저장됨
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString과 유사
    def __str__(self):
        # return f"Post object ({self.id})"
        return self.message

    def message_length(self):
        return len(self.message)
    message_length.short_description = "메시지 글자 수"