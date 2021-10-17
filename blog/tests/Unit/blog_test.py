from unittest import TestCase
from blog import Blog

b = Blog('Test', 'Test Author')
b2 = Blog('My Day', 'Rolf')


# test driven development, dank aan wat je gaat implementeren voor je het implementeert
class BlogTest(TestCase):
    def test_create_blog(self):
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        b.posts = ['test']

        b2.posts = ['test', 'another']
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (2 posts)')
