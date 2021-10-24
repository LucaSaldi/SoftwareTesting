# test_is de default naam voor een test
from base_test import BaseTest
import json


# een assert statement kijkt of een bepaalde conditie True is , als het True is blijft het runnen, als het false is
# geeft het een AssertionError. get is een request om iets te gaan halen We maken een test_client aan, zodat app.py
# niet echt moet runnen
# door het maken van een test_client, gaat het programma snel kunnen runner
class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')
            # 200 is de standaard status_code van een get request als deze ok is
            self.assertEqual(resp.status_code, 200)
            # Kijkt of het eerste gelijk is aan het tweede, kijkt dus of response dezelfde data teruggeeft,
            # we moeten wel json.loads gebruiken zodat deze een dictionary teruggeeft om de teste te laten slagen
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, world!'})
