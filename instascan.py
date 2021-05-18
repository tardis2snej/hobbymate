from networking import Session
from instauser import ActiveUser


def get_user_keywords(username):
    session = Session()
    user = ActiveUser(username, session.get_session_id())
    user_posts = user.get_user_posts()
    session.end_session()

    return convert_to_keywords_dict(user_posts)


def convert_to_keywords_dict(user_posts):
    # TODO
    pass