import pytest

pytestmark = [
    pytest.mark.django_db,
]
base_url = "/api/v1/pages/"


@pytest.fixture
def content_video(factory):
    return factory.video_content()


@pytest.fixture
def content_audio(factory):
    return factory.audio_content()


@pytest.fixture
def content_text(factory):
    return factory.text_content()


@pytest.fixture
def page(factory, content_video, content_audio, content_text):
    page = factory.page()
    factory.page_block(page=page, content_video=content_video)
    factory.page_block(page=page, content_audio=content_audio)
    factory.page_block(page=page, content_text=content_text)
    return page


def test_page_detail_return_200(api, page):
    r = api.get(f"{base_url}{page.id}/", as_response=True)
    assert r.status_code == 200


def test_page_detail_return_404(api):
    r = api.get(f"{base_url}9999/", as_response=True)
    assert r.status_code == 404


def test_page_detail_page_data(api, page):
    r = api.get(f"{base_url}{page.id}/")

    assert r["id"] == page.id
    assert r["title"] == page.title


def test_page_detail_video_data(api, page, content_video):
    r = api.get(f"{base_url}{page.id}/")

    video = r["blocks"][0]["content_video"]
    assert video["id"] == content_video.id
    assert video["title"] == content_video.title
    assert content_video.video.url in video["video"]
    assert content_video.subtitle.url in video["subtitle"]


def test_page_detail_audio_data(api, page, content_audio):
    r = api.get(f"{base_url}{page.id}/")

    audio = r["blocks"][1]["content_audio"]
    assert audio["id"] == content_audio.id
    assert audio["title"] == content_audio.title
    assert content_audio.audio.url in audio["audio"]
    assert audio["bitrate"] == content_audio.bitrate


def test_page_detail_text_data(api, page, content_text):
    r = api.get(f"{base_url}{page.id}/")

    text = r["blocks"][2]["content_text"]
    assert text["id"] == content_text.id
    assert text["title"] == content_text.title
    assert text["text"] == content_text.text


def test_page_detail_inc_content_counter(
    api, page, content_video, content_audio, content_text
):
    assert content_video.counter == 0
    assert content_audio.counter == 0
    assert content_text.counter == 0

    api.get(f"{base_url}{page.id}/")

    content_video.refresh_from_db()
    assert content_video.counter == 1

    content_audio.refresh_from_db()
    assert content_audio.counter == 1

    content_text.refresh_from_db()
    assert content_text.counter == 1
