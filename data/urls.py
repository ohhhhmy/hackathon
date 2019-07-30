from django.urls import path
from . import views

urlpatterns = [
    path('show', views.show, name="show"),
    path('search', views.search, name="search"),
    path('<int:data_id>', views.detail, name="detail"),
    path('show/sortName', views.sortName, name="sortName"),
    path('show/sortPrice', views.sortPrice, name="sortPrice"),
    path('pricefilter', views.pricefilter, name="pricefilter"),
]