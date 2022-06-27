from django.shortcuts import render

# Create your views here.
from webapp.models import Work, status_choices


def index_view(request):
    works = Work.objects.order_by("-d_date")
    context = {"works": works}
    return render(request, "index.html", context)


def work_view(request):
    pk = request.GET.get("pk")
    work = Work.objects.get(pk=pk)
    return render(request, "work_view.html", {"work": work})


def create_work(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": status_choices})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        d_date = request.POST.get("d_date")
        new_work = Work.objects.create(description=description, status=status, d_date=d_date)
        context = {"work": new_work}
        return render(request, "work_view.html", context)
