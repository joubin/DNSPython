from unittest import TestCase

from dnslookup import dns


class TestLookup(TestCase):
    def test_lookup(self):
        result = dns.nslookup("google.com", "8.8.8.8")
        print(result)
        self.fail()
