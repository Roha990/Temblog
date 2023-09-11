import random
from .models import Article


# Случайные статьи для специальной секции случайных статей
def get_random_article(request):
    articles = list(Article.objects.all())
    random_articles = random.sample(articles, 3)
    return {
        "random_articles": random_articles,
    }
