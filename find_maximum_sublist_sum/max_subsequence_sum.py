def max_subsequence_sum(value):
    '''this function is return maxsimum sum of sub [list/tuple]'''
    
    # we use start_max to look for the maximum sum
    # of elements among all positive segments
    start_max = value[0]
    
    # we use max_ending to look for all positive numbers in list or tuple
    max_ending = 0
    
    for n in range(len(value)):
        max_ending += value[n]

        if max_ending < 0:
            max_ending = 0

        elif start_max < max_ending:
            start_max = max_ending

    return start_max


if __name__ == '__main__':
    test_tuple = (3, -3, 4, -1, -2, 5, -2)
    print("Maximum sub sequence sum -->", max_subsequence_sum(test_tuple))
