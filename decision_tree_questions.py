def has_similarities(similarities):
    if len(similarities) > 0:
        return True
    else:
        return False


def is_consistent_frequency(similarities):
    count = len(similarities)
    sum_percent = 0
    for key in similarities:
        difference_percent = min(similarities[key][0], similarities[key][1]) / max(similarities[key][0], similarities[key][1])
        sum_percent += difference_percent

    average_percent = sum_percent / count

    print("Average percent")
    print(average_percent)

    if average_percent > 0.7:
        return True
    else:
        return False


def is_high_frequency(similarities):
    count = len(similarities)
    user1_sum = 0
    user1_average = 0
    user1_high_count = 0
    user2_sum = 0
    user2_average = 0
    user2_high_count = 0

    for key in similarities.keys():
        user1_sum += similarities[key][0]
        user2_sum += similarities[key][1]

    user1_average = user1_sum / count
    user2_average = user2_sum / count

    print("Averages:")
    print(user1_average)
    print(user2_average)

    for key in similarities.keys():
        if similarities[key][0] > user1_average:
            user1_high_count += 1
        if similarities[key][1] > user2_average:
            user2_high_count += 1

    print("High counts:")
    print(user1_high_count)
    print(user2_high_count)

    user1_percent = user1_high_count / count
    user2_percent = user2_high_count / count

    print("Percent:")
    print(user1_percent)
    print(user2_percent)

    if user1_percent > 0.3 and user2_percent > 0.3:
        return True
    else:
        return False


def get_similarities(dict1, dict2):
    similarities = {}
    for key in dict1.keys():
        if key in dict2:
            if dict1[key] != 1 and dict2[key] != 1:
                similarities[key] = [dict1[key], dict2[key]]

    print(similarities)
    return similarities