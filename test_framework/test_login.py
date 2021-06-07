import requests
from hamcrest import assert_that, contains_string, equal_to, has_key

URL = "https://reqres.in/api"
LOGIN_URL = f"{URL}/login/"
STATUS_CODE_OK, STATUS_CODE_NOT_FOUND = 200, 400


def test_login_valid():
    json_body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    resp = requests.post(LOGIN_URL, data=json_body)
    assert_that(resp.status_code, equal_to(STATUS_CODE_OK))
    assert_that(resp.json(), has_key("token"))


def test_login_no_password():
    json_body = {"email": "test@test.com"}
    resp = requests.post(LOGIN_URL, data=json_body)
    assert_that(resp.status_code, equal_to(STATUS_CODE_NOT_FOUND))
    assert_that(resp.json()["error"], contains_string("Missing password"))


def test_login_no_email():
    json_body = {}
    resp = requests.post(LOGIN_URL, data=json_body)
    assert_that(resp.status_code, equal_to(STATUS_CODE_NOT_FOUND))
    assert_that(resp.json()["error"], contains_string("email"))
    assert_that(resp.json()["error"], contains_string("username"))
