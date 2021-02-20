#4. You need to calculate the sum of a special sequence constructed like follows:
#The sequence starts with a number M (1 <= M <= 9). Each (i+1)-st element is formed by incrementing
#all digits of the previous i-th element and putting one additional digit of the same new value.
#If a certain element consists of nines, the next one will contain only ones.
#For example, if M = 4 the sequence goes like follows:
#4 55 666 7777 88888 999999 1111111 22222222 ...
#Apart from M (starting element), you are also given B > 0
#Calculate the sum of B first elements of the sequence starting with M
#Input:
#M
#B
#Output:
#Sum of the sequence described above
#Example 1
#Input:
#3
#4
#Output:
#7268
#Example 2
#Input:
#8
#3
#Output:
#218
def get_list(num1: int, num2: int):
    nums = []
    counter = 1
    temp_num = num1
    for i in range(num2):
        if temp_num > 9:
            temp_num = 1
        current_num = str(temp_num) * counter
        nums.append(current_num)
        counter += 1
        temp_num += 1
        
    return nums

TEST_CASES_1 = [
    (2, 1, ['2']),
    (3, 2, ['3', '44']),
    (4, 1, ['4']),
    (8, 3, ['8', '99', '111']),
    (3, 4, ['3', '44', '555', '6666']),
    (10, 5, ['1', '22', '333', '4444', '55555']),
    (1, 4, ['1', '22', '333', '4444']),
    (9, 3, ['9', '11', '222']),
]
for p, d, a in TEST_CASES_1:
    answer = get_list(p, d)
    if answer != a:
        print(p, d, a, answer)
        exit('Error')
print('ALL TESTS 1 PASSED')



def calculate_num(the_list: list):
    final_num = sum(int(num) for num in the_list)
    return final_num

TEST_CASES_2 = [
    (['2'], 2),
    (['3', '44'], 47),
    (['4'], 4),
    (['8', '99', '111'], 218),
    (['3', '44', '555', '6666'], 7268),
    (['1', '22', '333', '4444', '55555'], 60355),
    (['1', '22', '333', '4444'], 4800),
    (['9', '11', '222'], 242),
]
for p, a in TEST_CASES_2:
    answer = calculate_num(p)
    if answer != a:
        print(p, a, answer)
        exit('Error')
print('ALL TESTS 2 PASSED')





start = int(input())
amount = int(input())
list_ = get_list(start, amount)
print(calculate_num(list_))
