from django import forms
from .models import HomoBudget

class CreateForm(forms.ModelForm):
    
    class Meta :
        model = HomoBudget
        fields = ["category", "price", "content", "created_at"]
        #widgets(読み：ウィジェット) imputタグの表示様式を指定する(https://docs.djangoproject.com/ja/5.2/ref/forms/widgets/)
        widgets = {
            #日付(時間なし)をカレンダーから選択できるようにしたい場合、DateInput,attrsはdateを使う(https://docs.djangoproject.com/ja/5.2/ref/forms/widgets/#dateinput )
            "created_at": forms.DateInput(
                attrs={"type": "date"}
            )
        }