import unittest
import requests
import logging
import pydantic
from sqlalchemy import create_engine
from sqlalchemy.sql import text

ENTRYPOINT = 'http://policy-enforcement-service:5100/'
DATABASE_DSN = 'postgresql://book:book@26.255.132.24:5432/library'
ACCESS_DENIED_MESSAGE = {"message":"Content not found"}
BOOK_DELETE_MESSAGE = {"message":"Book deleted"}
ADMIN_GROUP_ID = 1
USER_GROUP_ID = 2
DATASCHEMA="users"

usermail="test-user20@example.com"
password="password"

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-9s %(message)s"
)

class Book(pydantic.BaseModel):
    id:int
    user_id=str
    name=str
    status=int
    rating=int
    generes=list[str]
    typ=str
    authors=list[str]
    series=str
    about=str

class User(pydantic.BaseModel):
    id: str 
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    nickname: str
    bio: str
    group_id: int
    ban: int

class TestCommonFunctionality(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_service_availability(self):
        response = requests.get(ENTRYPOINT)
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, ACCESS_DENIED_MESSAGE)

class BaseUserTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.test_user: User = None
        self.access_token: str = None

    def setUp(self, group_id: int, age: int) -> None:
        self._register_test_user(group_id, age)
        self._login()

    def tearDown(self) -> None:
        self._delete_test_user()

    def _register_test_user(self, group_id: int, ban: int) -> User:
        payload = {
            "email": usermail,
            "password": password,
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "nickname": "string",
            "bio": "string",
            "ban": ban,
            "group_id": group_id
        }   
        try:
            response = requests.post(f'{ENTRYPOINT}auth/register', json=payload) 
            response.raise_for_status()
            self.test_user = User(**response.json())
        except requests.exceptions.HTTPError as exc:
            logger.error(exc.response.text)
            logger.error(exc)

    def _raise_if_invalid_user(self):
        if self.test_user is None:
            raise Exception('Cannot continue test without valid user!')

    def _delete_test_user(self):
        if self.test_user is None:
            return
        engine = create_engine(DATABASE_DSN)
        with engine.connect() as connection:
            connection.execute(text(f"""DELETE FROM "{DATASCHEMA}"."user" WHERE id = '{self.test_user.id}';"""))
            connection.commit()

    def _login(self):
        self._raise_if_invalid_user()
        try:
            data = {
                'username': usermail,
                'password': password,
            }
            response = requests.post(
                f'{ENTRYPOINT}auth/jwt/login', data=data
            ) 
            response.raise_for_status()
            self.access_token = response.json()['access_token']
        except requests.exceptions.HTTPError as exc:
            logger.error(exc)

    @property
    def auth_headers(self):  
        return {
            'Authorization': f'Bearer {self.access_token}'
        }  
         
class TestAdminPolicies(BaseUserTestCase):
    def setUp(self) -> None:
        super().setUp(ADMIN_GROUP_ID, 0)
        self._login()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_complaints_list(self):
        self._raise_if_invalid_user()
        response = requests.get(
            f'{ENTRYPOINT}complaints/by_status/1', headers=self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

class TestUserPolicies(BaseUserTestCase):
    def setUp(self) -> None:
        super().setUp(USER_GROUP_ID, 0)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_complaints_list(self):
        self._raise_if_invalid_user()
        response = requests.get(
            f'{ENTRYPOINT}complaints/by_status/1', headers=self.auth_headers
        )
        
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, ACCESS_DENIED_MESSAGE)

    def test_get_topic_list(self):
        self._raise_if_invalid_user()
        response = requests.get(
            f'{ENTRYPOINT}/topics', headers=self.auth_headers
        )
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, ACCESS_DENIED_MESSAGE)

class TestBanPolicies(BaseUserTestCase):
    def setUp(self) -> None:
        super().setUp(USER_GROUP_ID, 0)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_topic_list(self):
        self._raise_if_invalid_user()
        response = requests.get(
            f'{ENTRYPOINT}/topics', headers=self.auth_headers
        )
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, ACCESS_DENIED_MESSAGE)

if __name__ == '__main__':
    unittest.main()