import random


def generate_random_matrix(n):
    return [generate_random_martix_row(n) for i in range(0, n)]


def generate_random_martix_row(n):
    return [random.random() for i in range(0, n)]
