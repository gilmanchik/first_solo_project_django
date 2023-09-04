from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='main_page'),
    path('about/', about, name='about'),
    path('create_info/', create_info, name='create_info'),
    path('<int:pk>', InfoDetail.as_view(), name='info-detail'),
    path('<int:pk>/update', InfoUpdate.as_view(), name='info-update'),
    path('<int:pk>/delete', InfoDelete.as_view(), name='info-delete')
]