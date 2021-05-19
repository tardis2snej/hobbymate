from decision_tree_questions import *


class Node:
    def __init__(self, question=None, nodeTrue=None, nodeFalse=None, dead_end_index=0):
        self.question = question
        self.TRUE = nodeTrue
        self.FALSE = nodeFalse
        self.dead_end_index = dead_end_index

    def get_next_node(self, data):
        if self.question(data):
            return self.TRUE
        else:
            return self.FALSE


class DecisionTree:
    def __init__(self, input_data):
        self.head = None
        self.keywords1 = input_data[0]
        self.keywords2 = input_data[1]
        self.similarities = get_similarities(self.keywords1, self.keywords2)
        self.decision_tree_setup()

    def decision_tree_setup(self):
        average_frequency_consistent = Node(dead_end_index=1)
        average_frequency_not_consistent = Node(dead_end_index=2)
        high_frequency = Node(is_consistent_frequency, average_frequency_consistent, average_frequency_not_consistent)
        not_high_frequency = Node(dead_end_index=3)
        similarities_exist = Node(is_high_frequency, high_frequency, not_high_frequency)
        similarities_doesnt_exist = Node(dead_end_index=4)
        self.head = Node(has_similarities, similarities_exist, similarities_doesnt_exist)

    def get_end_point(self):
        pointer = self.head
        while pointer.dead_end_index == 0:
            pointer = pointer.get_next_node(self.similarities)
        return pointer.dead_end_index
