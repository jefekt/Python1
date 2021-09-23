company = {
    'gasprom': 2152,
    'lucoul': 1482,
    'rosneft': 602,
    'magnit': 1368,
    'tatneft': 932,
    'novatek': 862,
    'evraz': 770,
    'nlmk': 683,
    'mmk': 514,
    'mts': 476,
    'chtpz': 192,
}

def sorted_1(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]
    return random_list[0:3]


list_from_dictionary = list(company.items())
for i in sorted_1(list_from_dictionary):
    print(i[0], ':', i[1])

list_from_dictionary = list(company.items())
list_from_dictionary.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])


def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max
print(three_max(company))
