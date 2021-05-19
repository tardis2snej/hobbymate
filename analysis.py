import instascan
from decision_tree import *


def compare_users(user1, user2):
    user1_keywords = instascan.get_user_keywords(user1)
    user2_keywords = instascan.get_user_keywords(user2)

    keywords1 = get_sorted(user1_keywords)
    keywords2 = get_sorted(user2_keywords)
    print(keywords1)
    print(keywords2)

    similarities = get_similarities(keywords1, keywords2)
    prediction = calculate_prediction(keywords1, keywords2)
    return prediction, similarities


def calculate_prediction(keywords1, keywords2):
    tree = DecisionTree((keywords1, keywords2))
    return tree.get_end_point()


def get_sorted(dictionary):
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1])
    sorted_list.reverse()
    return {k: v for k, v in sorted_list}


