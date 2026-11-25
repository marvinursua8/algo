# def repeat(text,n):
#     if n == 0:
#         return ""


#     return text + repeat(text, n - 1)



# print(repeat("ha",3))



def backwards(text):
    if  text == "":
        return ""

    return text[0] + backwards(text[1:])


print(backwards("hello"))


def test(num_lst):
    if num_lst == []:
        return []
    counter = 0

    counter += num_lst[0]

    return test(num_lst[1:]) + counter



print(test([4,3,2,1]))