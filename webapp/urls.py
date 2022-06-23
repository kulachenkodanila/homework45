from django.urls import path

from webapp.views import index_view, work_view

urlpatterns = [
    path('', index_view),
    path('work/', work_view)


]