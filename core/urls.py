
from . import views
from django.urls import path, re_path
from core.views import *

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('<slug>/', post_detail_view, name='post_detail')
]