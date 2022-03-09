
def get_probabilities(text):
    dict = {}
    count = 0
    for ch in text:
        count += 1
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    for key, value in dict.items():
        dict[key] = value / count
    return dict

