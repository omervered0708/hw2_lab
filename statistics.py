def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2)
    # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """
    find covariance between two features
    :param first_list_of_values: list of values of the first feature
    :param second_list_of_values: list of values of the second feature
    :return: returns covariance
    """
    average1 = mean(first_list_of_values)
    average2 = mean(second_list_of_values)
    length = len(first_list_of_values)
    co_sum = sum([(first_list_of_values[i]-average1)*(second_list_of_values[i]-average2) for i in range(length)])
    result = co_sum/(len(first_list_of_values)-1)
    return result


def correlation(first_list_of_values, second_list_of_values):
    """
    find correlation between two features
    :param first_list_of_values: list of values of the first feature
    :param second_list_of_values: list of values of the second feature
    :return: returns correlation
    """
    first_list_std = variance(first_list_of_values)**0.5
    second_list_std = variance(second_list_of_values)**0.5
    result = covariance(first_list_of_values, second_list_of_values)/(first_list_std*second_list_std)
    return result


def find_strongest_pair(data):
    """
    find pair with strongest correlation
    :param data: a dictionary whose keys are features and values are lists of feature's values
    :return: tuple of the alphabetically sorted pair in places 0 and 1 and the value of their correlation in 2
    """
    strongest_pair = ([], [], 0)
    sorted_keys = sorted(data.keys())
    for out_key in sorted_keys:
        for in_key in sorted_keys:
            # compare features in order to not check same pair twice
            if in_key > out_key:
                curr_corr = correlation(data[out_key], data[in_key])
                if abs(curr_corr) > abs(strongest_pair[2]):
                    strongest_pair = (out_key, in_key, curr_corr)
                # if the current correlation is 0 and 'strongest_pair' is still empty set it to the current pair
                # if the current correlation is 0 but there is a previous pair with correlation 0 don't make a change
                elif curr_corr == 0 and strongest_pair == ([], [], 0):
                    strongest_pair = (out_key, in_key, curr_corr)

    return strongest_pair


def find_weakest_pair(data):
    """
    find pair with weakest correlation
    :param data: a dictionary whose keys are features and values are lists of feature's values
    :return: tuple of the alphabetically sorted pair in places 0 and 1 and the value of their correlation in 2
    """
    weakest_pair = ([], [], 2.0)
    sorted_keys = sorted(data.keys())
    for out_key in sorted_keys:
        for in_key in sorted_keys:
            # compare features in order to not check same pair twice
            if in_key > out_key:
                curr_corr = correlation(data[out_key], data[in_key])
                if abs(curr_corr) < abs(weakest_pair[2]):
                    weakest_pair = (out_key, in_key, curr_corr)

    return weakest_pair
