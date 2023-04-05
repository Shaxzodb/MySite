from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import ArticleModel

class LatestNewsFeed(Feed):
    title = "Latest News"
    link = "/news/"
    description = "The latest news articles on our site."

    def items(self):
        return ArticleModel.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title_at

    def item_description(self, item):
        return item.content_at

    def item_link(self, item):
        return reverse('article_delete', args=[item.slug])