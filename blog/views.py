from blog.models import Maqola,Comment
from django.shortcuts import render

def index(request):
    maqolalar = Maqola.objects.all().order_by("created_at")
    return render(request, "index.html" ,{"maqolalar": maqolalar})

def detail(request ,id):
    maqola = Maqola.objects.get(id=id)
    comments= Comment.objects.filter(article=maqola , status=True)
    return render(request , "detail.html" , {"maqola":maqola , "comments":comments})