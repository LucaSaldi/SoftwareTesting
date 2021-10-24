# moet een ander patroon hebben dan andere test files, want deze gaat geen methodes bevatten om te testen
# Dit is een superclass van TestHome, zodat we niet steeds alles moeten veranderen
from unittest import TestCase
from app import app


class BaseTest(TestCase):
    # Deze methode gaat altijd voor alle andere testen worden gerunt en wordt voor iedere test methode gerunt
    def setUp(self):
        # Deze vertelt aan Flask dat we aan het testen zijn
        app.testing = True
        self.app = app.test_client()
