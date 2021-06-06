import instagramy
import instascan


class ActiveUser:
    def __init__(self, username, session_id):
        self.session_id = session_id
        self.username = username
        self.user = InstagramUserExtended(username=username, sessionid=session_id)

    def get_user_posts_descriptions(self):
        return self.user.posts_texts

    def get_posts_with_keywords(self, keywords):
        posts = []
        print("Get posts with keywords")
        # all_posts = []
        # for post in self.user.simplified_posts:
        #     curr_post = post
        #     curr_post['keywords'] = ''
        #     all_posts.append(curr_post)
        print("all posts filled")
        for post in self.user.simplified_posts:
            post['keywords'] = ''
            for keyword in keywords:
                if keyword in post['text']:
                    print("append")
                    post['keywords'] += ' ' + keyword
                else:
                    print("not append")
            if len(post['keywords']) is not 0:
                posts.append(post)
        print("collected posts")
        for post in posts:
            print(post)
        return posts


class InstagramUserExtended(instagramy.InstagramUser):
    @property
    def simplified_posts(self):
        print("Simple posts")
        posts_lists = []
        posts_details = self.user_data["edge_owner_to_timeline_media"]["edges"]
        for i in posts_details:
            data = {}

            try:
                data["shortcode"] = i["node"]["shortcode"]
            except (KeyError, TypeError):
                data["shortcode"] = None

            try:
                data["text"] = i['node']['edge_media_to_caption']['edges'][0]['node']['text']
            except (KeyError, TypeError):
                data["text"] = None

            try:
                data["post_url"] = f'https://www.instagram.com/p/{i["node"]["shortcode"]}/'
            except (KeyError, TypeError):
                data["post_url"] = None

            try:
                data["display_url"] = i["node"]["display_url"]
            except (KeyError, TypeError):
                data["display_url"] = None

            try:
                data["is_video"] = i["node"]["is_video"]
            except (KeyError, TypeError):
                data["is_video"] = None

            if i["node"]["is_video"]:
                data["video_url"] = i["node"]["video_url"]
            if i["node"]["is_video"]:
                data["post_source"] = i["node"]["video_url"]
            else:
                data["post_source"] = i["node"]["display_url"]

            posts_lists.append(data)

        return posts_lists

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
