import re

from django import forms
from .models import Post

# form.is_valid() 호출 당시
# 1. form.full_clean() 호출
#     a. 각 필드 객체 별 Type에 맞춰(+ model단에서 정의 된 필드별 validators) 유효성 검사
#     b. Form 객체 내에서 필드 이름 별로 clean_필드명() 함수가 있다면, 호출해서 유효성 검사 및 값 반환
#     c. clean() 함수(두개 이상의 필드에 대한 clean함수)가 있다면 호출해서 유효성 검사
# 2. 에러 유무에 따른 True, False 반환


# 가급적이면 모든 validators는 모델에 정의하고, ModelForm을 통해 모델의 validators 정보도 같이 가져오는 것이 좋음
# clean이 필요할 때 -> 특정 Form에서 1회성 유효성 검사 루틴이 필요할 때 / 다수 필드값에 걸쳐서, 유효성 검사가 필요할 때 / 필드 값을 변경할 필요가 있을 때(validator로 값 변경 불가) 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'photo', 'tag_set', 'is_public']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)
        return message
