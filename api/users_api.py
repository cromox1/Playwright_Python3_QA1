# from datetime import datetime
from utils.config import BASE_URL
from uuid import uuid4
# from utils.test_data import TEST_FIRSTNAME


class UsersAPI:

    def __init__(self, request):
        self.request = request

    def get_user(self, user_id):
        return self.request.get(f"{BASE_URL}/api/users/{user_id}")

    def delete_user(self, user_id):
        return self.request.delete(f"{BASE_URL}/api/users/{user_id}")

    def get_allusers(self):
        return self.request.get(f"{BASE_URL}/api/users")

    def create_user(self, data):
        return self.request.post(f"{BASE_URL}/api/users", data=data)
    
    def login_user(self, username, password):
        return self.request.post(f"{BASE_URL}/api/login", data={"username": username, "password": password})

    def create_testuser(self, firstname):
        # timestamp = datetime.now().strftime("%H%M%S")
        testuser = f"{firstname}_{uuid4().hex[:8]}"

        return self.request.post(
            f"{BASE_URL}/api/users",
            data={"username": testuser, "password": "Password123",
                  "email": f"{testuser}@rosli-laptop.com.my"}
        ), testuser
