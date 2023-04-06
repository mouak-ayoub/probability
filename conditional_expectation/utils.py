from scipy.stats import bernoulli


def get_successive_occurence(str):
    if str is None or "".__eq__(str):
        raise ValueError(" String is None or empty")
    first_char_length = 1
    while first_char_length < len(str) and str[first_char_length] == str[0]:
        first_char_length += 1

    return first_char_length


def get_successive_occurence_array(str, runs):
    if str is None or "".__eq__(str):
        raise ValueError(" String is None or empty")
    if runs is None or runs == 0:
        raise ValueError(" runs is None or empty")
    occurences_array = []
    for i in range(runs):
        char_length = get_successive_occurence(str)
        occurences_array.append(char_length)
        str = str[char_length:]
        if str is None or "".__eq__(str):
            break
    return occurences_array


def generate_sample_head_tail(p,sample_length):
    samples = bernoulli(p).rvs(sample_length)
    ht_samples = ['H' if sample == 1 else 'T' for sample in samples]
    samples_as_string = "".join(ht_samples)
    return samples_as_string

