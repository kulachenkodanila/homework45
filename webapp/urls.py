from django.urls import path

from webapp.views import index_view, work_view, create_work

urlpatterns = [
    path('', index_view),
    path('work/', work_view),
    path('works/add/', create_work)


]