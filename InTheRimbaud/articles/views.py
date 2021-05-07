import datetime
from articles.models import Article
from django.shortcuts import render
from django.http import HttpResponse
import logging
import pytz
from django.views.decorators.csrf import csrf_protect

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, you are at the article welcome page")


@csrf_protect
def details(request, id: str):

    if id.isnumeric():
        article = (
            default_articles_query(request.user.is_superuser).filter(id=id).first()
        )
    else:
        article = None

    if article is None:
        return render(request, "not_exists.html")

    context = {"article": article}
    return render(request, "detail.html", context)


@csrf_protect
def all(request):
    articles = default_articles_query(request.user.is_superuser)

    context = {"articles_view_title": "Welcome on my page", "articles": articles}
    return render(request, "view_all.html", context)


@csrf_protect
def filter_id(request, id: str = None):
    if id is None:
        articles = default_articles_query(request.user.is_superuser)

        logger.debug("No filter given")
    elif not id.isnumeric():
        articles = []

        logger.error("Filter is not a numeric")
    else:
        articles = default_articles_query(request.user.is_superuser).filter(
            id__contains=id
        )

    context = {"articles": articles}
    return render(request, "view_all_content.html", context)


@csrf_protect
def filter_title(request, text: str = None):
    if text is None:
        articles = default_articles_query(request.user.is_superuser)
        logger.debug("No filter given")
    else:
        articles = default_articles_query(request.user.is_superuser).filter(
            title__icontains=text
        )

    context = {"articles": articles}
    return render(request, "view_all_content.html", context)


def default_articles_query(is_admin: bool = False):
    articles = Article.objects.exclude(
        end_date__lt=datetime.datetime.now(pytz.utc),
    ).order_by("id")

    if not is_admin:
        articles = articles.exclude(
            is_adm_only=True,
        )

    return articles
