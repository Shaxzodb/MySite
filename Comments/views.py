from django.shortcuts import get_object_or_404
# from django.http import Http404
from django.urls import reverse
from django.http import HttpResponseRedirect
from Articles.models import ArticleModel
from django.contrib.auth.decorators import login_required
from .models import ArticleComment
from django.contrib import messages
# Create your views here.


@login_required()
def created_comment(request, slug):
    if request.method == 'POST':
        article = get_object_or_404(ArticleModel, slug=slug)
        content = request.POST['comment']
        if content != '':
            ArticleComment.objects.create(
                author=request.user,
                article_cm=article,
                content_cm=content
            )
        else:
            messages.success(request, 'Comment bo\'sh bo\'lishi mumkun emas')
    return HttpResponseRedirect(reverse('article_detail', args=[str(slug)]))


@login_required()
def like_and_unlike_comment(request, pk, article):
    comment = get_object_or_404(ArticleComment, id=pk)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return HttpResponseRedirect(reverse('article_detail', args=[str(article)]))

