from django.conf.urls import url
from django.contrib import admin

from .views import CategoryArticleView

urlpatterns = [
    url(r'^category/(?P<slug>\w+)', CategoryArticleView.as_view(), name='category_article',),
]
