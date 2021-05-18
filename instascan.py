import networking
from instauser import ActiveUser


def get_user_keywords(username):
    session_id = networking.get_session_id()
    user = ActiveUser(username, session_id)
    user_posts = user.get_user_posts()
    return convert_to_keywords_dict(user_posts)


def convert_to_keywords_dict(user_posts):
    # TODO
    pass
