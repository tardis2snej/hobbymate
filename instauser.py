import instagramy


class ActiveUser:
    def __init__(self, session_id, username):
        self.session_id = session_id
        self.username = username
        self.user = instagramy.InstagramUser(username, sessionid=session_id)

    def get_user_posts(self):
        # TODO
        # print(user.user_data['edge_owner_to_timeline_media']['edges'][0]['node']['edge_media_to_caption']['edges'][0]['node']['text'])

        #
        # for post in user.posts:
        #     print(post)
        #

        pass