#Lambda Excercise 1

#Consider the List

from functools import reduce
from os import sep



prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]


#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]
sorted_by_version = sorted(prog_lang, key=lambda x:x[1])
print('Sorted by version' + str(sorted_by_version))
#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]
sort_length = sorted(prog_lang, key = lambda x: (len(x[0]),x[0]), reverse=True)
print( 'Sorted List: ' + str(sort_length))
#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
filter_with_a = list(filter(lambda x:  'a' in x[0], prog_lang)) 
print("Contains a:" + str(filter_with_a))
#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]
int_form_version = list(filter(lambda x : type(x[1])==int,prog_lang))
print('Filtered by version in integer form' + str(int_form_version))
#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]
lower_case_language = list(map(lambda x: ((x[0].lower()),x[1]), prog_lang))
print("Transformed into lowercase"+str(lower_case_language))
#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')

separated_list = list(map(lambda x,y : reduce((x[0]+y[0]),(x[1]+y[1])), prog_lang))
print("This list has been separated:" + str(separated_list))
