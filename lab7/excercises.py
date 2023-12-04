input_list = [1, 2, 4, -1, -4, 2]
input_list_of_tuples = [(1, 2), (3, 4)]


def replace_with_zeroes(input_list):
    new_list = []
    for number in input_list:
        if number < 0:
            input_list[input_list.index(number)] = 0
        else:
            new_list.append(number)
    return input_list


def join_tuples(list_of_tuples):
    number_list = []
    for one_tuple in list_of_tuples:
        number_list += one_tuple
    return number_list


def replace_below_average(input_list):
    sum = 0
    for number in input_list:
        sum += number
    average = sum/len(input_list)
    maximal = max(input_list)
    for number in input_list:
        if number < average:
            input_list[input_list.index(number)] = maximal
    return input_list


def one_before_last(word_list):
    count = 0
    for word in word_list:
        if word == word_list[-2]:
            count += 1
    return count


def count_even_lengths(word_list):
    even_length_count = 0
    for word in word_list:
        if len(word) % 2 == 0:
            even_length_count += 1
    return even_length_count


def count_same_letter_limbs(word_list):
    count = 0
    for word in word_list:
        if word[0] == word[-1]:
            count += 1
    return count


def multiply_in_string(number_list):
    final_string = ""
    for number in number_list:
        final_string += str(number)*number
    return final_string


def find_unique_letters(text1, text2):
    text1, text2 = text1.lower(), text2.lower()
    uniques = []
    for letter in text1:
        if letter not in text2:
            uniques.append(letter)
    for letter in text2:
        if letter not in text1:
            uniques.append(letter)
    return uniques


def translate_to_latin(polish_input):
    # # translation_dict = {"ą": "a",
    #                     "ć": "c",
    #                     "ę": "e",
    #                     "ł": "l",
    #                     "ń": "n",
    #                     "ó": "o",
    #                     "ś": "s",
    #                     "ź": "z",
    #                     "ż": "z"}
    translation_input = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
    translation_output = "acelnoszzACELNOSZZ"
    translation_table = str.maketrans(translation_input, translation_output)
    result = polish_input.translate(translation_table)
    return result


def is_more_even(number_list):
    count = 0
    for number in number_list:
        if number % 2 == 0:
            count += 1
        else:
            count -= 1
    if count > 0:
        result = True
    else:
        result = False
    return result


# replace_with_zeroes(input_list)
# join_tuples(input_list_of_tuples)
# replace_below_average([1, 3, 3, 3, 3, 72])
# one_before_last(["tak", "nie", "nie", "nie wiem"])
# count_even_lengths(["tak", "nie", "nie", "nie wiem"])
# multiply_in_string([4, 5, 9, 0])
# find_unique_letters("Abc", "abb")
# translate_to_latin("Król żółci")
is_more_even([1, 2, 3])
