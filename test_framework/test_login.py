import requests

URL = "https://reqres.in/api"
LOGIN_URL = f"{URL}/login/"
STATUS_CODE_OK, STATUS_CODE_NOT_FOUND = 200, 400


def test_login_valid():
    json_body = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    resp = requests.post(LOGIN_URL, data=json_body)
    print(resp.text)
    assert resp.status_code == STATUS_CODE_OK
    assert "token" in resp.json()


def test_login_no_password():
    json_body = {"email": "test@test.com"}
    resp = requests.post(LOGIN_URL, data=json_body)
    assert resp.status_code == STATUS_CODE_NOT_FOUND
    assert resp.json()["error"] == "Missing password"


def test_login_no_email():
    json_body = {}
    resp = requests.post(LOGIN_URL, data=json_body)
    assert resp.status_code == STATUS_CODE_NOT_FOUND
    assert resp.json()["error"] == "Missing email or username"
