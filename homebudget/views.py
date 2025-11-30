from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Sum , Avg # .models とは違う
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HomoBudget
from .forms import CreateForm

def index(request):
    object_list = HomoBudget.objects.all()
    #incomes = HomoBudget.objects.filter(category = "income")
    aggregate_values = HomoBudget.objects.exclude(category='income').aggregate(payment = Sum("price"))
    income_values = HomoBudget.objects.filter(category='income').aggregate(incomes = Sum("price"))
    
    #支出の計算
    payment = aggregate_values["payment"] or 0
    income = income_values["incomes"] or 0
    total = income - payment
    
    if(payment > income * 0.5):
        isRed = True
    else:
        isRed = False
    
    # {}は辞書型
    return render(request, 
                "homebudget/index.html",
                {
                    "object_list":object_list,
                    "payment":aggregate_values["payment"],
                    "incomes":income_values["incomes"],
                    "total":total,
                    "isRed":isRed,
                }
                )

# 削除機能。jsのconfirm()を使うため関数を使用
def DeleteDate(request, pk):
    # 引数に入れた情報を元にオブジェクトを探す
    obj = get_object_or_404(HomoBudget, pk=pk)
    # 削除
    obj.delete()
    return redirect("homebudget:index")

class ListHomeView(LoginRequiredMixin,ListView):
    model = HomoBudget
    template_name = "homebudget/list.html"
    
    # def post(*):
        
    
class CreateDataView(LoginRequiredMixin,CreateView):
    model = HomoBudget
    form_class = CreateForm
    #fields = ["category", "price", "content", "created_at"] forms.pyを作ったため不使用
    template_name = "homebudget/create.html"
    success_url = reverse_lazy("homebudget:index")
    
class UpdateDataView(LoginRequiredMixin,UpdateView):
    model = HomoBudget
    form_class = CreateForm
    template_name = "homebudget/update.html"
    success_url = reverse_lazy("homebudget:index")