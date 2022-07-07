from django.shortcuts import render, get_object_or_404, redirect


status_choices = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')]


# Create your views here.
from webapp.models import Work
from webapp.forms import To_DoForm


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
        form = To_DoForm()
        return render(request, "create.html", {"form": form})
    else:
        form = To_DoForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            d_date = form.cleaned_data.get("d_date")
            title = form.cleaned_data.get("title")
            new_work = Work.objects.create(description=description, status=status, d_date=d_date, title=title)
            return redirect("work_view", pk=new_work.pk)
        return render(request, "create.html", {"form": form})


def delete_work(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == "GET":
        pass
    else:
        work.delete()
        return redirect("index")


def update_work(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == "GET":
        form = To_DoForm(initial={
            "description": work.description,
            "status": work.status,
            "d_date": work.d_date,
            "title": work.title
        })
        return render(request, "update.html", {"form": form})
    else:
        form = To_DoForm(data=request.POST)
        if form.is_valid():
            work.description = form.cleaned_data.get("description")
            work.status = form.cleaned_data.get("status")
            work.d_date = form.cleaned_data.get("d_date")
            work.title = form.cleaned_data.get("title")
            work.save()
            return redirect("article_view", pk=work.pk)
        return render(request, "update.html", {"form": form})

