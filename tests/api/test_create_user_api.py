import re
from time import sleep
from datetime import datetime
from api.users_api import UsersAPI
from utils.config import BASE_URL
from utils.test_data import TEST_FIRSTNAME
from utils.json_reader import get_user
from utils.logger import get_logger


logger = get_logger(__name__)

def test_create_user(users_api):

    for i in range(6):
        response, testuser = users_api.create_testuser(TEST_FIRSTNAME)
        sleep(1)        # to make the username diff name by 1 sec
        assert response.status == 201
        assert response.status_text == 'CREATED'
        data = response.json()
        logger.info(f"{i + 1}) User{i+1} to CREATE: username = {testuser} / email = {data["user"]["email"]}")
        assert data["message"] == "User created"
        assert data["user"]["username"] == f"{testuser}"
        assert re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", data["user"]["email"])


def test_create_many_users(users_api):

    for userx in [get_user('valid_user'), get_user('integers_user'), get_user('integers_pswd')]:
        tstamp = datetime.now().strftime("%H%M%S")
        usrname = userx.username + '_' + tstamp
        logger.info(f"--> USERNAME = {usrname} / PSWD = {userx.password} / EMAIL = {usrname}@rosli-laptop.com.my")
        response1 = users_api.create_user(data={"username": f"{usrname}", "password": f"{userx.password}", "email": f"{usrname}@rosli-laptop.com.my"})
        sleep(1)  # to make the username diff name by 1 sec
        assert response1.status == 201
        assert response1.status_text == 'CREATED'
        data1 = response1.json()
        assert data1["message"] == "User created"
        assert data1["user"]["username"] == usrname
        assert re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", data1["user"]["email"])
