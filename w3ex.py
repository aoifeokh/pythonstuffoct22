#ex1 string length
#shorthand is len()

#manual:
def str_len(string):
    cnt = 0
    for char in string:
        cnt += 1
    return cnt

print(str_len('committee'))

#ex2 - count characters
def char_freq(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_freq('astrophysics'))

#ex 3 
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#ex4
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))