class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # laat een dictionary zien
    def json(self):
        return {
            'title': self.title,
            'content': self.content,

        }