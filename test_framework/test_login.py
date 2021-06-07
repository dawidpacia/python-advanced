import requests

LOGIN_URL = "https://reqres.in/api"
LOGIN_LOGIN_URL = f"{LOGIN_URL}/login/"
STATUS_CODE_OK, STATUS_CODE_NOT_FOUND = 200, 400


def test_login_valid():
    json_body = {"email": "test@test.com", "password": "something"}
    resp = requests.post(LOGIN_URL, data=json_body)
    assert resp.status_code == STATUS_CODE_OK
    assert resp.json()["token"] == "QpwL5tke4Pnpja7X"


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
