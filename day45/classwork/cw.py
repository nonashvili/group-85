#codewars 1
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positives = 0
    negatives_sum = 0

    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives_sum += i

    return [positives, negatives_sum]