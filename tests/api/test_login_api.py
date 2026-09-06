# from sqlalchemy.testing.provision import drop_db
from api.users_api import UsersAPI
from utils.config import BASE_URL
from utils.json_reader import get_user


def notlogin_api_page_then_validate(users_api, username, password):

    response = users_api.login_user(username, password)
    assert response.status == 401
    assert response.status_text == 'UNAUTHORIZED'
    data = response.json()
    assert data["success"] is False
    assert data["message"] == 'Invalid username or password'
    assert "user" not in data  # assert key "user" does not exist in data

def valid_login_then_validate(users_api, username, password):

    list_usernames = users_api.get_allusers().json()
    if username not in [user['username'] for user in list_usernames]:
        users_api.create_user(data={"username": username, "password": password})
    response = users_api.login_user(username, password)
    assert response.status == 200
    assert response.status_text == 'OK'
    data = response.json()
    assert data["success"] is True
    assert data["message"] == 'Login successful'
    assert data["user"]["username"] == username
    assert username in data["user"]["email"]

def test_valid_login_validuser(users_api):
    user = get_user('valid_user')
    valid_login_then_validate(users_api, user.username, user.password)

# def test_valid_login_intgr_user(users_api):
#     user = get_user('integers_user')
#     valid_login_then_validate(users_api, user.username, user.password)

# def test_valid_login_intgr_pswd(users_api):
#     user = get_user('integers_pswd')
#     valid_login_then_validate(users_api, user.username, user.password)

def test_invalid_login_wrongpswd(users_api):
    notlogin_api_page_then_validate(users_api, 'cromox1', 'WrongPassword')

def test_invalid_login_wronguser(users_api):
    notlogin_api_page_then_validate(users_api, 'notexist1', 'Password123')

def test_invalid_login_blankpswd(users_api):
    notlogin_api_page_then_validate(users_api, 'cromox1', ' ')

def test_invalid_login_blankuser(users_api):
    notlogin_api_page_then_validate(users_api, ' ', 'Password123')
