import pytest
import variables


@pytest.fixture
def url():
    url_api = "https://gorest.co.in/public-api/users/"
    return url_api


@pytest.fixture
def token_auth():
    header_auth = {'Authorization': 'Bearer ' + variables.AUTH}
    return header_auth
