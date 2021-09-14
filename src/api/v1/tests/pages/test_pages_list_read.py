import pytest

from main.models import Page

pytestmark = [
    pytest.mark.django_db,
]
base_url = "/api/v1/pages/"


def test_pages_list_return_200(api):
    r = api.get(base_url, as_response=True)
    assert r.status_code == 200


def test_pages_list_pagination(api):
    r = api.get(base_url)
    count_pages = Page.objects.all().count()
    assert r["count"] == count_pages
    assert r["next"] is not None


def test_pages_list_results(api):
    r = api.get(base_url)
    page = Page.objects.all().first()
    result = r["results"][0]
    assert result["id"] == page.id
    assert result["title"] == page.title
    assert f"{base_url}{page.id}/" in result["absolute_url"]
