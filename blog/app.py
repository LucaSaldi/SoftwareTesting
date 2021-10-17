# laat de user het aantal blogs zien
# laat de user kiezen
blogs = dict()


def menu():
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
