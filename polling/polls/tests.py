from django.test import TestCase
from polling.polls.models import Poll


class PollTestCase(TestCase):

    fixtures = ["db.json"]

    def setUp(self) -> None:
        return super().setUp()

    def test_poll(self):
        poll = Poll.objects.get(id=10)
        self.assertEqual(poll.title, "Should FED print more money?")
