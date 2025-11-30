from django.db import models
from django.utils import timezone

CATEGORY =( ("Food","食費"),("book","書籍"),("Favorite","趣味"),("subscribe","サブスク"),("Entertainment", "娯楽費"),("Work","経費") , ("income","収入"), ("other","その他"))

class HomoBudget(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY)
    price = models.IntegerField()
    content = models.CharField(max_length=100, default="")
    #日付の指定(https://docs.djangoproject.com/ja/5.2/ref/models/fields/#datefield )
    created_at = models.DateField()
    
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    #名前から中身を推測できるようにするため
    def __str__(self):
        return self.content
