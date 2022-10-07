from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('birds/', views.BirdList.as_view(), name="bird_list"),
    path('birds/new/', views.BirdCreate.as_view(), name="bird_create"),
    path('birds/<int:pk>/', views.BirdDetail.as_view(), name="bird_detail"),
    path('birds/<int:pk>/update',views.BirdUpdate.as_view(), name="bird_update"),
    path('birds/<int:pk>/delete',views.BirdDelete.as_view(), name="bird_delete"),
]