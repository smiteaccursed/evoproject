import unittest
import requests
import logging
import typing
import pydantic

ENTRYPOINT = "http://forum-service:5010"
ACCESS_DENIED_MESSAGE = {"detail":"Not Found"}


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-9s %(message)s"
)

class Topic(pydantic.BaseModel):
    creator_id: str
    name: str
    id: int
    messages: list[typing.Any]


class TestCommonFunctionality(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_service_availability(self):
        response = requests.get(ENTRYPOINT, timeout=10)
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertDictEqual(data, ACCESS_DENIED_MESSAGE)

class TestForum(unittest.TestCase):
    def _create_topic(self, id="3fa85f64-5717-4562-b3fc-2c963f66afa6", name="testetstttets"):
        data={
                "creator_id": id,
                "name": name}
        response = requests.post(f"{ENTRYPOINT}/topics", json=data,
            timeout=10)
        self.assertEqual(response.status_code, 200)
        return Topic(**response.json())
    
    def test_get_topics(self):
        response = requests.get(f"{ENTRYPOINT}/topics",
            timeout=10)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_post_topics(self):
        try:
            top=self._create_topic(name="smite")
            self.assertIsInstance(top, Topic)
            self.assertEqual(top.name, "smite")
        finally:
            response = requests.delete(f"{ENTRYPOINT}/topics/TID/{top.id}",
            timeout=10)
            self.assertEqual(response.status_code, 200)
    def test_get_topic_by_id(self):
        top=self._create_topic(name="smite")
        try:
            self.assertIsInstance(top, Topic)
            self.assertEqual(top.name, "smite")
            response = requests.get(f"{ENTRYPOINT}/topics/TID/{top.id}",
            timeout=10)
            self.assertEqual(response.status_code, 200)
        finally:
            response = requests.delete(f"{ENTRYPOINT}/topics/TID/{top.id}",
            timeout=10)
            self.assertEqual(response.status_code, 200)
    def test_update_topic(self):
        top=self._create_topic(name="smite")
        try:
            self.assertIsInstance(top, Topic)
            self.assertEqual(top.name, "smite")
            data={"name":"asdasd", 
                  "creator_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}
            response = requests.put(f"{ENTRYPOINT}/topics/TID/{top.id}", json=data,
            timeout=10)
            self.assertEqual(response.status_code, 200)
        finally:
            response = requests.delete(f"{ENTRYPOINT}/topics/TID/{top.id}",
            timeout=10)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()