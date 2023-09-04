from django.urls import path
from .views import *

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create_news/', create_news, name='create_news'),
    path('<int:pk>', NewsDetail.as_view(), name='news-detail'),
    path('<int:pk>/update', NewsUpdate.as_view(), name='news-update'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='news-delete')
]