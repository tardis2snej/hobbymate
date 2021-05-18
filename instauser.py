import instagramy


class ActiveUser:
    def __init__(self, username, session_id):
        self.session_id = session_id
        self.username = username
        self.user = InstagramUserExtended(username=username, sessionid=session_id)

    def get_user_posts(self):
        return self.get_user_posts()


class InstagramUserExtended(instagramy.InstagramUser):
    @instagramy.InstagramUser.posts.getter
    def posts(self) -> list:
        # TODO override this to unite with get_posts_texts property
        return super().posts
        # print("Hello from overrided property!")
        # posts_tuple_lists = super().posts
        # posts_details = self.user_data["edge_owner_to_timeline_media"]["edges"]
        #
        # for post, i in zip(posts_lists, posts_details):
        #     post['description'] = i['node']['edge_media_to_caption']['edges'][0]['node']['text']
        #
        # return posts_lists

    @property
    def posts_texts(self) -> list:
        texts_list = []
        posts_list = self.user_data["edge_owner_to_timeline_media"]["edges"]
        for post in posts_list:
            data = {}
            try:
                data["display_url"] = post["node"]["display_url"]
            except (KeyError, TypeError):
                data["display_url"] = None
            try:
                data["text"] = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
            except (KeyError, TypeError):
                data["text"] = None
            texts_list.append(data)

        return texts_list
