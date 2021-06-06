import re
from gensim.parsing.preprocessing import remove_stopwords
from networking import Session
from instauser import ActiveUser


def get_user_keywords(username):
    session = Session()
    user = ActiveUser(username, session.get_session_id())
    user_posts = user.get_user_posts_descriptions()
    session.end_session()

    return convert_to_keywords_dict(user_posts)


def convert_to_keywords_dict(user_posts):
    keywords = {}
    for post in user_posts:
        words_list = split_to_keywords(post['text'])
        for word in words_list:
            if word in keywords:
                keywords[word] = keywords[word] + 1
            else:
                keywords[word] = 1

    return keywords


def split_to_keywords(message):
    message_without_punctuation = remove_punctuation(message)
    clean_message = remove_stopwords(message_without_punctuation)
    words = clean_message.split()
    keywords = filter_words(words)
    return keywords


def remove_punctuation(message):
    """ Cleans message so that only words left """
    cleaned_message = message.replace('\n', ' ').replace('\t', ' ').replace('#', ' ').lower()
    cleaned_message = re.sub("\.|,|—|\?|!|\(|\)|\"|\"|«|-|\|;|:|\|\\|", "", cleaned_message)
    cleaned_message = remove_stopwords(cleaned_message)
    return cleaned_message


def clean_stopwords(words):
    # try:
    #     stop_words = set(nltk.corpus.stopwords.words('english'))
    # except LookupError:
    #     nltk.download()
    #     return clean_stopwords(words)
    # clean_words = [w for w in words if not w in stop_words]
    clean_words = remove_stopwords(words)
    return clean_words


def filter_words(words):
    filtered = []
    for word in words:
        word = word.rstrip()
        if len(word) > 2 and re.search('^[a-z]', word):
            filtered.append(word)

    return filtered


def get_posts_with_keywords(keywords, user):
    session = Session()
    user = ActiveUser(user, session.get_session_id())

    user_posts = user.get_posts_with_keywords(keywords)
    session.end_session()

    return user_posts
