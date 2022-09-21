# test timber.py

from sre_compile import isstring
from timber import (
    DOMAIN_CLIENT_ID,
    DOMAIN_CLIENT_SECRET,
    get_token,
)


def test_client_id_env_variable_exists():
    assert not isinstance(DOMAIN_CLIENT_ID, type(None))


def test_client_secret_env_variable_is_string():
    assert not isinstance(DOMAIN_CLIENT_SECRET, type(None))


def test_access_token_retrievable():
    assert not isinstance(get_token(), type(None))

