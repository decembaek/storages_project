from django.db import models

# Create your models here.


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 이 모델은 db에 올라가지 않음, 정의만 가능
        abstract = True
