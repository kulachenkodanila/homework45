from django.urls import path

from webapp.views import index_view, work_view, create_work

urlpatterns = [
    path('', index_view, name="index"),
    path('work/<int:pk>/', work_view, name="work_view"),
    path('works/add/', create_work, name="create_work")


]