'''
author = Pavel Mikeska
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''',
         ]


separator = ('-' * 40)

print(separator)

# 1. Greet or welcome the user to the app
print('Welcome to the app. Please log in: ')

# 2. Ask the user for entering username and password
username = input('Username: ')
password = input('Password: ')

users = {
         'bob': '123',
         'ann': 'pass123',
         'mike': 'password123',
         'liz': 'pass123'
}

# 3. Check whether the password and username entered are among those registered.
if username in users and users[username] == password:
    print('You are verified!')
else:
    print('You do not have permission to continue!')
    quit()

print(separator)


# 4. Ask the user to select among the three texts stored in the variable TEXTS.
print('We have 3 texts to be analyzed.')
select_text = int(input('Enter a number btw. 1 and 3 to select: '))
selected_text = TEXTS[select_text - 1]
words_chosen_text = list(selected_text.split())


# 5. Calculate the following statistics for the selected text:
# 1) number of words in total;
# 2) number of words starting with capital letter;
# 3) number of uppercase words;
# 4) number of lowercase words;
# 5) number of numeric-only words (e.g. 100, not 100N)
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
for i in words_chosen_text:
    if i.istitle():
        titlecase += 1
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase += 1
    if i.isnumeric():
        numeric += 1

print('There are', len(words_chosen_text), 'words in selected text.')
print('There are', titlecase, 'titlecase words.')
print('There are', uppercase, 'uppercase words.')
print('There are', lowercase, 'lowercase words.')
print('There are', numeric, 'numeric words.')

print(separator)

# remove symbols '.' and ',' from the list
words_chosen_text = [i.strip('.,') for i in words_chosen_text]


# 6. Create a bar chart depicting the frequencies of word lengths in the text:
frequency_word = {}
for i in words_chosen_text:
    i = len(i)
    frequency_word[i] = frequency_word.get(i, 0) + 1

for i in sorted(frequency_word):
    value = frequency_word[i]
    print(i, '*' * value, value)

print(separator)

# 7. Calculate the sum of all the numeric "words" in the given text:
numeric_sum = 0
for i in words_chosen_text:
    if i.isdecimal():
        numeric_sum += float(i)

print('If we summed all the numbers in this text we would get: ', numeric_sum)

print(separator)
