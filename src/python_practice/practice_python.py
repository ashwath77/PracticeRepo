#Each word in sentence should be reversed input="This is good day"
def reverse_word(Input):
    reverse_str = []
    Input1 = Input.split()
    for word in Input1:
        output = word[::-1]
        reverse_str.append(output)
    return reverse_str

input = "This is good day"
reverse_word(input)


#sum of elemets in nested list
a=[[1,2],[3,4]]
list=[]
for i in a:
    sum = 0
    for j in i:
        sum=sum+j
    list.append(sum)

#Write a Python program to sum all the items
def sum_of_items(numbers):
    sum = 0
    for i in range(1, numbers + 1):
        sum += i
    return sum

#Write a Python program to multiply all the items in a list
def mutiplication_of_items(numbers):
    mul = 1
    for i in range(1, numbers + 1):
        mul*= i
    return mul

# Write a Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings
def words_sentance(sentence):
    words = sentence.split()
    selected_words = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            selected_words.append(word)
    return selected_words

sentence = "My mom and dad are leaving to party, Neen and nan preparing for there examse"
selected_words = words_sentance(sentence)
selected_words


#Write a Python program to find the list of words that are longer than n from a given list of words
def words_longer_than_n(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

l = ['ashwath', 'runner', 'takeaway', 'gowda']
n = int(input("Enter the length of n: "))
words_longer_than_n(l, n)


# Write a Python program to shuffle and print a specified list (shuffle)
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

list_1 = [1, 255, 35, 4, 15, 8]
shuffled_list = shuffle_list(list_1)
shuffled_list

#Find if the element is anagram, if it is print True, and if false print False and
# append the output to a list => Input1= "nami" Input2= ["mani", "anim", "nnaa", "iam"]
# Output: [True, True, False, False]

Input1= "nami"
Input2= ["mani", "anim", "nnaa", "iam"]
def anagram(Ip1,Ip2):
    str1=" ".join(sorted(Input1))
    str2=[" ".join(sorted(word)) for word in Input2]
    output=[str1==word for word in str2]
    return output

anagram(Input1,Input2)


def sum_of_largest_number(Ip1):
    sum=0
    for i in Ip1:
        sum1=max(i)
        sum = sum+sum1
    return sum

sum_of_largest_number(Input)
Input = [[1, 2, 3], [3, 5, 4], [8, 4, 0, -1]]