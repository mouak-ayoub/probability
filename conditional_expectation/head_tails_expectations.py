import numpy as np
from utils import *

p = 0.7
sample_length = 200
number_samples = 10_000


def expectation_to_get_pattern(pattern):
    hh_indexes = []

    for i in range(number_samples):
        samples_as_string = generate_sample_head_tail(p, sample_length)
        hh_indexes.append(samples_as_string.index(pattern) + 2)

    return np.mean(hh_indexes)


def get_runs_length(nb_runs):
    length_array = []

    for i in range(number_samples):
        samples_as_string = generate_sample_head_tail(p, sample_length)
        occurences_array = get_successive_occurence_array(samples_as_string, nb_runs)
        length_array.append(occurences_array)

    matrix_length = np.array(length_array)
    mean_array = np.mean(matrix_length, axis=0)
    return mean_array


if __name__ == "__main__":
    test_pattern = 'HH'
    expectation = expectation_to_get_pattern(test_pattern)
    print(expectation)

    nb_runs = 5
    expectation_array = get_runs_length(nb_runs)
    print(expectation_array)

    theoretical_expectation_runs_length = (1 / (p * (1 - p))) - 2
    print(theoretical_expectation_runs_length)
