from utils.config import BASE_URL
from utils.test_data import TEST_FIRSTNAME
from utils.logger import get_logger
from uuid import uuid4
# from api.users_api import UsersAPI

logger = get_logger(__name__)

def convert_user_id_to_name(users_api, user_id):
    users_all_json = users_api.get_allusers().json()
    return [user['username'] for user in users_all_json if user['id'] == user_id][0]

def list_user_todelete(users_api, firstname):
    users_all_json = users_api.get_allusers().json()
    return [user['id'] for user in users_all_json if firstname in user['username']]

def test_delete_user(users_api):

    users_todelete = list_user_todelete(users_api, TEST_FIRSTNAME)
    logger.info(f"List of users_todelete = {users_todelete} / {[convert_user_id_to_name(users_api, i) for i in users_todelete]}")

    if len(users_todelete) == 0:
        users_api.create_testuser(TEST_FIRSTNAME)
        users_todelete = list_user_todelete(users_api, TEST_FIRSTNAME)

    i = 1
    for user_id in users_todelete:
        logger.info(f"{i}) User{i} to DELETE : ID = {user_id} / username = {convert_user_id_to_name(users_api, user_id)}")
        response = users_api.delete_user(user_id)
        assert response.status == 200
        assert response.status_text == 'OK'
        assert response.url.split('/')[-1] == str(user_id)
        data = response.json()
        assert data["message"] == "User deleted"
        # logger.info(f"\tUser{i} data = {data}")
        i += 1

# def test_delete_allusers_except_five(users_api):
#     users_all_json = users_api.get_allusers().json()
#     all_users_except_five = [u['id'] for u in users_all_json if u['id'] >= 5]
#     i = 1
#     for user_id in all_users_except_five:
#         logger.info(f"{i}) User to DELETE : ID = {user_id} / username = {convert_user_id_to_name(users_api, user_id)}")
#         response = users_api.delete_user(user_id)
#         assert response.status == 200
#         assert response.status_text == 'OK'
#         assert response.url.split('/')[-1] == str(user_id)
#         data = response.json()
#         assert data["message"] == "User deleted"
#         i += 1

def test_user_can_be_deleted(users_api):
    list_user_ids = list()
    for i in range(6):
        create_response, username = users_api.create_testuser(TEST_FIRSTNAME)
        user_id = create_response.json()["user"]["id"]
        list_user_ids.append(user_id)

    for user_id in list_user_ids:
        delete_response = users_api.delete_user(user_id)
        assert delete_response.status == 200
        assert delete_response.status_text == 'OK'
        assert delete_response.url.split('/')[-1] == str(user_id)
        datajson = delete_response.json()
        assert datajson["message"] == "User deleted"
        # after user been deleted
        get_response = users_api.get_user(user_id)
        assert get_response.status == 404
