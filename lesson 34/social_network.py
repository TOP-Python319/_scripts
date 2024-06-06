
# Классы:
#     SocialNetwork
#     User
#     Post
#     Group


class LikeMixin:
    def __init__(self):
        self.likes = 0

    def like(self):
        self.likes += 1


class CommentMixin:
    pass


class JoinMixin:
    def __init__(self):
        self.users = []

    def join(self, user):
        self.users.append(user)


class Post(LikeMixin, CommentMixin):
    def __init__(self, text, author):
        LikeMixin.__init__(self)
        self.text = text
        self.author = author

    def __str__(self):
        pass


class Group(JoinMixin):
    def __init__(self, name):
        JoinMixin.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name}, population: {len(self.users)}'


class User:
    def __init__(self, name, birthday, city):
        self.name = name
        self.birthday = birthday
        self.city = city
        self.posts = []
        self.groups = []

    def create_post(self, text) -> Post:
        post = Post(text, self)  # self, чтобы у поста был автор
        self.posts.append(post)
        return post

    def remove_post(self, post: Post):
        self.posts.remove(post)

    def like_post(self, post: Post):
        post.like()

    def join_group(self, group: Group):
        group.join(self)
        self.groups.append(group)


class SocialNetwork:
    def __init__(self):
        self.users = []
        self.posts = []
        self.groups = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_most_liked_posts(self):
        pass

    def get_most_populat_groups(self):
        pass

    def __str__(self):
        pass
