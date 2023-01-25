from django_filters import FilterSet
from .models import ArticleModel

class ArticleFilter(FilterSet):
    class Meta:
        
        model = ArticleModel
        fields = {
            'title_at': ['icontains'],
        }