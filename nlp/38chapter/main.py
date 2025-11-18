# list1 = [1,2,3,5]
# list2 = [2,3,4]
# list3 = [1,2,3,4,5,6]
#
# a = zip(list1,list2,list3)
# print(list(a))

ngram_range = 2


def create_ngram_set(input_list):
    return set(zip(*[input_list[i:] for i in range(ngram_range)]))


if __name__ == "__main__":
    input_list = [1,3,2,1,5,3]
    res = create_ngram_set(input_list)
    print(res)

