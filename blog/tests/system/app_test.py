# type test die door het hele systeem gaat
from unittest import TestCase

# Laat ons iets patchen, kan ons dingen laten veranderen van de methode, de methode iets anders laten doen Dit is een
# goede website over patching https://www.fugue.co/blog/2016-02-11-python-mocking-101#:~:text=Mocking%20in%20Python
# %20is%20done,want%20or%20raise%20an%20Exception%20. Want is toch niet het makkelijkste om te begrijpen

from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')
