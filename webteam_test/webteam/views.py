from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Articles


class CategoryArticleView(TemplateView):
    template_name = 'webteam/article_category_list.html'

    def get(self, request, *args, **kwargs):
        category = kwargs.get('slug', '')
        kwargs['category'] = category
        if category:
            articles = Articles.objects.filter(category__slug=category)
            kwargs['article_list'] = articles
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
