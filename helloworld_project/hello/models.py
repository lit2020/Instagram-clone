from django.db import models as m
from datetime import date
# Create your models here.

# Feed 모델 생성
class Feed(m.Model):
   content = m.TextField()
   image = m.TextField()
   profile_image = m.TextField()
   user_id = m.TextField()
   like_count = m.IntegerField()
