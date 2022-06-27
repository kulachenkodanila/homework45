from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from webapp.models import Work, status_choices


def index_view(request):
    works = Work.objects.order_by("-d_date")
    context = {"works": works}
    return render(request, "index.html", context)


def work_view(request, **kwargs):
    pk = kwargs.get("pk")
    work = get_object_or_404(Work, pk=pk)
    return render(request, "work_view.html", {"work": work})


def create_work(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": status_choices})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        d_date = request.POST.get("d_date")
        title = request.POST.get("title")
        new_work = Work.objects.create(description=description, status=status,  d_date=d_date, title=title)
        return redirect("work_view.html", pk=new_work.pk)

