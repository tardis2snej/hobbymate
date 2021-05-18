import instascan


def compare_users(user1, user2):
    user1_keywords = instascan.get_user_keywords(user1)
    user2_keywords = instascan.get_user_keywords(user2)
    get_similarities(user1_keywords, user2_keywords)
    # TODO
    pass


def get_similarities(keywords, keywords2):
    # TODO
    pass
