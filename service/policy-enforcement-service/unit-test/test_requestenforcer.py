import os
import unittest

import jwt
from starlette.requests import Request
from starlette.datastructures import Headers
from app.policies.requestenforcer import RequestEnforcer, Service, EnforceResult

TEST_POLICIES_CONFIG = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'test-policies.yaml'
)
TEST_JWT_SECRET = '4e7c09ff-f69e-45f0-8285-99f80a289320'

LIBRARY_SERVICE = Service(
    name='library-service', entrypoint='http://library-service:5000/', inject_token_in_swagger=True
)



def build_request(
    method: str = "GET",
    server: str = "www.example.com",
    path: str = "/",
    headers: dict = None,
    body: str = None,
) -> Request:
    '''
    Build mock-request based on Starlette Request
    '''
    if headers is None:
        headers = {}
    request = Request(
        {
            "type": "http",
            "path_params": {'path_name': path[1:]},
            "path": path,
            "headers": Headers(headers).raw,
            "http_version": "1.1",
            "method": method,
            "scheme": "https",
            "client": ("127.0.0.1", 8080),
            "server": (server, 443),
        }
    )
    if body:
        async def request_body():
            return body

        request.body = request_body
    return request

class RequestEnforceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.policy_checker: RequestEnforcer = RequestEnforcer(
            TEST_POLICIES_CONFIG, TEST_JWT_SECRET
        )

    def test_book_allow(self):
        request = self._prepare_request(0, 1, 'GET', '/books/UID/')
        result = self.policy_checker.enforce(request)
        self._assert_access_allow(result, LIBRARY_SERVICE.entrypoint.unicode_string())

    def test_books_allow(self):
        request = self._prepare_request(0, 1, 'GET', '/books/BID/')
        result = self.policy_checker.enforce(request)
        self._assert_access_allow(result, LIBRARY_SERVICE.entrypoint.unicode_string())

    
    
    def test_books_denied(self):
        request = self._prepare_request(0, 2, 'DELETE', '/books/BID/')
        result = self.policy_checker.enforce(request)
        self._assert_access_denied(result)

    def test_books_post(self):
        request = self._prepare_request(0, 1, 'POST', '/books')
        result = self.policy_checker.enforce(request)
        self._assert_access_allow(result)

    def _make_headers(self, ban: int, group: int) -> dict:
        token = jwt.encode({
            'ban': ban, 
            'group_id': group,
            'aud': ["fastapi-users:auth"]
        }, key=TEST_JWT_SECRET)
        return {
            "authorization": f'Bearer {token}'
        }
    def _prepare_request(
            self, ban: int, group: int, method: str, path: str, make_headers: bool = True
        ) -> Request:

        headers = self._make_headers(ban, group) if make_headers else {}
        return build_request(method=method, path=path, headers=headers)
    
    def _assert_access_allow(self, result: EnforceResult, entrypoint: str):
        self.assertTrue(result.access_allowed)
        self.assertEqual(result.redirect_service, entrypoint)

    def _assert_access_denied(self, result: EnforceResult):
        self.assertFalse(result.access_allowed)
        self.assertIsNone(result.redirect_service)
