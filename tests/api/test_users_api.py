from utils.config import BASE_URL
from utils.logger import get_logger
import re
from api.users_api import UsersAPI

# import sys
# from pathlib import Path
# PROJECT_ROOT = Path(__file__).resolve().parents[2]
# sys.path.insert(0, str(PROJECT_ROOT))
# from utils.config import BASE_URL

logger = get_logger(__name__)

def test_get_allusers(api_request):

    response = api_request.get(f"{BASE_URL}/api/users")
    assert response.status == 200
    assert response.status_text == 'OK'
    data = response.json()
    assert len(data) > 0
    assert "username" in data[0]
    assert "email" in data[0]
    assert "id" in data[0]

def test_get_single_user(api_request):

    list_users = api_request.get(f"{BASE_URL}/api/users").json()
    logger.info(f"list_users = {list_users}")
    list_ids = [usr['id'] for usr in list_users]
    logger.info(f"list_ids = {list_ids}")
    assert len(list_ids) == len(set(list_ids))  # To validate that all IDs are unique
    for user in list_users:
        assert user['id'] in list_ids
        assert user["username"] in user["email"]
        assert re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", user["email"])
