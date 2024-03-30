from django.urls import path
from . import views


urlpatterns = [
    path('about/',views.about,name='about'),
    path('',views.home, name="home"),
    path('view-products/',views.view_products, name="view-products")
]