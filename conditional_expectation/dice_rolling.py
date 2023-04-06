from scipy.stats import randint
import numpy as np

low, high = 1, 7
size_sample = 100
number_samples = 10_000


def get_atleast_larger_than_first():
    num_rolls_array = []
    for i in range(number_samples):
        dice_rolling = randint.rvs(low, high, size=size_sample)
        num_rolls = np.where(dice_rolling >= dice_rolling[0])[0][1]
        num_rolls_array.append(num_rolls)

    expectation = np.mean(num_rolls_array)
    return expectation


def get_pattern_expectation(pattern):
    pattern_indexes = []
    for i in range(number_samples):
        dice_samples = randint.rvs(low, high, size=size_sample * 10*len(pattern))
        dice_rolls_as_string = "".join(str(roll) for roll in dice_samples)
        index = dice_rolls_as_string.index(pattern) + len(pattern)
        pattern_indexes.append(index)

    return np.mean(pattern_indexes)


if __name__ == "__main__":
    pattern = '111'
    expectation = get_pattern_expectation(pattern)
    print(f' expectation calculated from simulation get_pattern_expectation is {expectation}')

    theoretical_expectation = 0
    [theoretical_expectation := theoretical_expectation + 1 / (high - i) for i in range(low, high)]
    print(f'Theoretical expectation is {theoretical_expectation}')
    expectation = get_atleast_larger_than_first()
    print(f' expectation calculated from simulation get_atleast_larger_than_first is {expectation}')

