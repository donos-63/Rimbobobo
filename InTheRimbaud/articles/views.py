import datetime
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http import HttpResponse
import logging
import pytz
from django.views.decorators.csrf import csrf_protect

from articles.models import Article

logger = logging.getLogger(__name__)


def index(request) -> HttpResponse:
    """default page

    Args:
        request ([HttpRequest]): -

    Returns:
        [HttpResponse]: default message
    """
    return HttpResponse("Hello, you are at the article welcome page")


@csrf_protect
def details(request, id: str) -> HttpResponse:
    """Detail page

    Args:
        request ([HttpRequest]): -
        id (str): id searched for the article

    Returns:
        [HttpResponse]: article content
    """

    if id.isnumeric():
        article = (
            __default_articles_query(request.user.is_superuser).filter(id=id).first()
        )
    else:
        article = None

    if article is None:
        return render(request, "not_exists.html")

    context = {"article": article}
    return render(request, "detail.html", context)


@csrf_protect
def all(request) -> HttpResponse:
    """Main page. Display all articles

    Args:
        request ([HttpRequest]): -

    Returns:
        [HttpResponse]: list of articles
    """
    articles = __default_articles_query(request.user.is_superuser)

    context = {"articles_view_title": "Welcome on my page", "articles": articles}
    return render(request, "view_all.html", context)


@csrf_protect
def filter_id(request, id: str = None) -> HttpResponse:
    """Sub request to filter articles by id

    Args:
        request ([HttpRequest]): -
        id (str, optional): searched id(s). Defaults to None.

    Returns:
        [HttpResponse]: list of articles (all, none, or filtered)
    """
    if id is None:
        articles = __default_articles_query(request.user.is_superuser)

        logger.debug("No filter given")
    elif not id.isnumeric():
        articles = []

        logger.error("Filter is not a numeric")
    else:
        articles = __default_articles_query(request.user.is_superuser).filter(
            id__contains=id
        )

    context = {"articles": articles}
    return render(request, "view_all_content.html", context)


@csrf_protect
def filter_title(request, text: str = None) -> HttpResponse:
    """Sub request to filter articles by title

    Args:
        request ([HttpRequest]): -
        text (str, optional): searched title(s). Defaults to None.

    Returns:
        [HttpResponse]: list of articles (all, none, or filtered
    """
    if text is None:
        articles = __default_articles_query(request.user.is_superuser)
        logger.debug("No filter given")
    else:
        articles = __default_articles_query(request.user.is_superuser).filter(
            title__icontains=text
        )

    context = {"articles": articles}
    return render(request, "view_all_content.html", context)


def __default_articles_query(is_admin: bool = False) -> QuerySet:
    """[summary]

    Args:
        is_admin (bool, optional): [description]. Defaults to False.

    Returns:
        [type]: [description]
    """
    articles = Article.objects.exclude(
        # filter articles with validity date > today (arrange server date to utc)
        end_date__lt=datetime.datetime.now(pytz.utc),
    ).order_by("id")

    if not is_admin:
        articles = articles.exclude(
            is_adm_only=True,
        )

    return articles
