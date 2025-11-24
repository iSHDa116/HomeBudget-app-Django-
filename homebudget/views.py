from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Sum , Avg # .models とは違う
from .models import HomoBudget
from .forms import CreateForm

def index(request):
    object_list = HomoBudget.objects.all()
    
    aggregate_values = HomoBudget.objects.aggregate(total = Sum("price"), avg = Avg("price"))
    # {}は辞書型
    return render(request, 
                "homebudget/index.html",
                {
                    "object_list":object_list,
                    "total":aggregate_values["total"],
                    "avg":aggregate_values["avg"]    
                }
                )

# 削除機能。jsのconfirm()を使うため関数を使用
def DeleteDate(request, pk):
    # 引数に入れた情報を元にオブジェクトを探す
    obj = get_object_or_404(HomoBudget, pk=pk)
    # 削除
    obj.delete()
    return redirect("index")

class ListHomeView(ListView):
    model = HomoBudget
    template_name = "homebudget/list.html"
    
class CreateDataView(CreateView):
    model = HomoBudget
    form_class = CreateForm
    #fields = ["category", "price", "content", "created_at"] forms.pyを作ったため不使用
    template_name = "homebudget/create.html"
    success_url = reverse_lazy("index")
    
class UpdateDataView(UpdateView):
    model = HomoBudget
    form_class = CreateForm
    template_name = "homebudget/update.html"
    success_url = reverse_lazy("index")