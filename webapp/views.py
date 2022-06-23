from django.shortcuts import render

# Create your views here.
from webapp.models import Work


def index_view(request):
    works = Work.objects.order_by("-d_date")
    context = {"works": works}
    return render(request, "index.html", context)


def work_view(request):
    pk = request.GET.get("pk")
    work = Work.objects.get(pk=pk)
    return render(request, "work_view.html", {"work": work})
