from django.contrib.auth.models import User
from django.db import models


major_lst = (('major_1', '간호'), ('major_2', '건축'), ('major_3', '경영'), ('major_4', '공예'), ('major_5', '관광'),
('major_6', '광고'), ('major_7', '교육'), ('major_8', '교통&운송'), ('major_9', '기계&금속'), ('major_10', '농림&수산'),
 ('major_11', '도시&토목'), ('major_12', '디자인'), ('major_13', '미술'), ('major_14', '법'), ('major_15', '뷰티아트'),
 ('major_16', '사진&만화'), ('major_17', '사회과학'), ('major_18', '산업공학'),('major_19', '생명과학'), ('major_20', '서비스'),
 ('major_21', '소재&재료'), ('major_22', '수의학'), ('major_23', '식품'), ('major_24', '약학'), ('major_25', '언론'),
 ('major_26', '언어&문학'), ('major_27', '에너지'), ('major_28', '연극&영화'), ('major_29', '영상&예술'),
 ('major_30', '유아교육'), ('major_31', '음악'), ('major_32', '응용소프트웨어'),('major_33', '의류'),
 ('major_34', '인문과학'), ('major_35', '자연과학'), ('major_36', '전기&전자'),('major_37', '전산학&컴퓨터공학'),
 ('major_38', '정보&통신'), ('major_39', '조선'), ('major_40', '체육'), ('major_41', '초등교육'),
 ('major_42', '치료&보건'), ('major_43', '특수교육'), ('major_44', '화공'))

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.TextField(max_length=10)
    user_phone_num = models.CharField(max_length=20)
    user_major = models.CharField(choices=major_lst, max_length=20, null=True)


# class User__click_news(models.Model):
#     user_info = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='user')
#     last_user_news_title = models.TextField(max_length=200)
#     last_user_news_raw_stream = models.TextField(max_length=5000)
    

class User_scrap(models.Model):
    summary = models.TextField()
    writer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='scrap') 
    
    






