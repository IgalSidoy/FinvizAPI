import utility

filter_configuration = {
    'Price': {'condition': '<', 'condition_value': 40.0, 'condition_type': 'float'},
    'Rel_Volume': {'condition': '>', 'condition_value': 1.5, 'condition_type': 'float'},
    'Stocatics': {'condition': '>', 'condition_value': 70, 'condition_type': 'float'},
    'P/E': {'condition': '<', 'condition_value': 50, 'condition_type': 'float'},
    'Change': {'condition': '>', 'condition_value': 0, 'condition_type': 'float'}
}


def filter_by_type(value, condition_object):
    condition = condition_object['condition']
    condition_value = condition_object['condition_value']
    condition_type = condition_object['condition_type']
    if condition_type == 'float':
        value = float(value)

    if condition_type == 'int':
        value = int(value)

    if '<' == condition:
        if value < condition_value:
            return True
    if '=' == condition:
        if value == condition_value:
            return True
    if '>' == condition:
        if value > condition_value:
            return True
    return False


def filter(name, filter_configuration=filter_configuration):

    collection = utility.convert_csv_to_object(name)
    result_collection = []
    for stock in collection:

        # sort by conditions
        skip = False

        for sort_type in filter_configuration:
            condition = filter_configuration[sort_type]
            value = stock[sort_type]
            skip = not filter_by_type(value, condition)

            if skip:
                break

        if skip:
            continue
        result_collection.append(stock)

    result_file = name.split('.csv')[0]
    result_file = result_file+'-filtered.csv'

    utility.save_dic_csv(result_file, result_collection, True, 'w')
