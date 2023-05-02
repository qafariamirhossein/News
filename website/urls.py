from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='index'),
    path('contact',contact_view,name='contact'),
    path('category',category_view,name='category'),
]
