from unittest import TestCase
from post import Post


# voor alle functies/klasses/.. die niet aafhankelijk zijn van andere, moet je in unit test zetten


# moet altijd afhankelijk zijn van een andere klasse, deze is TestCase van unittest eerste test is als je een post
# object aanmaakt, dat de correcte properties worden gezet, alle testen moeten beginnen met test_
class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
#gebruik assertDictEqual, anders kijkt hij of ze exact hetzelfde object zijn, dit is niet zo
        self.assertDictEqual(expected, p.json())
