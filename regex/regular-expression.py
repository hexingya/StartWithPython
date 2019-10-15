# built-in module
import re

# Meta characters===================

# -- character set ---
# [aei]
# [a-z]
# [a-zA-Z]
# [01234]
# [^0-9]

# \d -- [0-9]

# res = re.search('th[Ee]', 'I know the application')
# res = re.search('x', 'I know the application')
# res = re.search('[0124]', 'djskfj98983412ksdjf')

# . any character except new line character

# ^ starts with
# $ ends with
# * zero or more occurrence {0,}
# + one or more occurrence {1,}
# ? zero or one occurrence {0,1}
# {6} exact no of foccurrence
# {5,} min 5 with no upper limit
# {5, 8} min 5 & max 8
# | either or
# () group

# Special sequences --------

# \A beginning
# \b at the beginning & end of a word r"\btion"
# \B not at beginning & end r"\Bt"
# \d digit '[0-9]'
# \D non-digit '[^0-9]'
# \s white space
# \S non white space
# \w word character [a-zA-Z0-9_]
# \W non word character [^a-zA-Z0-9_]

# \Z end of string r"toy\Z"

# res = re.search('[^\d]', '996956I have nothing 99')

# if res:
#     print(res.group())
#     print(res.start())
#     print(res.end())
#     print(res.span())

# string = "The quicks borwn fox jumps over the lazy jumps dog."
# pattern = r'q\B'

# result = re.search(pattern, string)

# print(result)


# string = "The quicks lazy jumps dog."

# # pat1 = r"\AT"
# pat1 = r"^T"
# # pat2 = r"\.\Z"
# pat2 = r"\.$"


# res = re.search(pat2, string)

# if res:
#     print(res.group())


# newstrring = "some Learn something someday"

# res = re.search('some', newstrring)

# if res:
#     print(res.group())
#     print(res.span())

# newstrring = "Learn something someday"

# res1 = re.match('some', newstrring)
# res2 = re.search('some', newstrring)

# if res1:
#     print(res1.group())
#     print(res1.span())

# if res2:
#     print(res2.group())
#     print(res2.span())


# newstrring1 = "Learn something someday"

# res1 = re.sub('some', "SOME", newstrring1)
# res2 = re.sub('some', "SOME", newstrring1, 1)

# print(res1)
# print(res2)

# string = "Just think or think"

# # patt1 = r"^[jJ].{0,}"
# patt2 = r"think"


# # res1 = re.findall(patt1, string)
# res2 = re.findall(patt2, string)

# # print(res1)
# print(res2)


# string = "Go and Watch everything to know everything"

# res1 = re.split('every', string)
# res2 = re.split('every', string, 1)

# print(res1)
# print(res2)

# print(re.split('t', 'toothpaste'))

# phone number

# string = "I am xyz. my phone 800903943478 place...kdjfk"

# phone = re.search('[0-9]{10}', string)
# pincode = re.search(r'\d{6}', string)

# if pincode:
#     print(pincode.group())

# urlstring = "http://www.example.com/"
# urlstring2 = "https://www.exam.com/"
# urlstring3 = "coolhttps://www.exam.com/"

# urlpatt = r'^https?://www\..{2,}\.\w{2,3}/.*$'

# result = re.search(urlpatt, urlstring)
# result2 = re.search(urlpatt, urlstring2)
# result3 = re.search(urlpatt, urlstring3)

# if result3:
#     print(result3.group())
#     print(result3.span())
# else:
#     print('Not a valid url')

# email

emailstring = "abc.some@example.com"

pat = r"^[0-9a-zA-Z_.]{3,}@\w{2,}\.\w{2,3}$"

res = re.search(pat, emailstring)

if res:
    print(res.group())
    print(res.span())
