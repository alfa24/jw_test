from test.api_client import DRFClient
from test.factory import Factory

import pytest
from mixer.backend.django import mixer as _mixer


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def api() -> DRFClient:
    return DRFClient()


@pytest.fixture
def factory() -> Factory:
    return Factory()
