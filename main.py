class DefaultList(list):
  def __init__(self, default_param):
    self.default = default_param
  def __getitem__(self, y):
    try:
      return list(self)[y]
    except IndexError:
      return self.default

x = DefaultList(6)
x.append(1)
x.extend([4, 10])
#print(x[1], x[1488])

class PasswordError(Exception):
  def __init__(self, default_param):
    self.message = default_param

class LengthError(PasswordError):
  pass  #log in __init__

class LetterError(PasswordError):
  pass  

class DigitError(PasswordError):
  pass

class WordError(PasswordError):
  pass

class SequenceError(PasswordError):
  pass  

def digit_checker(pwd):
  for i in pwd:
    if i.isdigit():
      return True
  return False

def word_checker(pwd, file_words):
  file_words.seek(0)
  for i in file_words.readlines():  
    i = i.strip()     
    if i in pwd:      
      return True #WORD IN PASSWORD!
  return False

def sequence_checker(pwd):  
  for i in range(len(pwd)): 
    if i+3 > len(pwd):
      break
    if (pwd[i:i+3] in 'qwertyuiopasdfghjklzxcvbnm') or (
    pwd[i:i+3] in 'йцукенгшщзхъфывапролджэячсмитьбю'):
      return True
  return False

d = {'LengthError': [], 'LetterError': [], 'DigitError': [], 'WordError': [], 'SequenceError': []}

with open('top-9999-words.txt', 'r') as file_words:  
  with open('top 10000 passwd.txt', 'r') as f:    
    for i in f.readlines():
      i = i.strip()
      if word_checker(i, file_words):
        try:
         raise WordError('')
        except WordError:
          d['WordError'].append(i)
      if len(i)<9:
        try:
         raise LengthError('Password length is 8 or less')
        except LengthError:
          d['LengthError'].append(i)
      if i == i.lower() or i == i.upper():
        try:
         raise LetterError('')
        except LetterError:
          d['LetterError'].append(i)
      if not digit_checker(i):
        try:
          raise DigitError('Password must contain digit')
        except DigitError:
          d['DigitError'].append(i)      
      if sequence_checker(i):
        try:
          raise SequenceError('qwerty')
        except SequenceError:
          d['SequenceError'].append(i)

for i in sorted(list(d.keys())): 
 print(i, '-' , len(d[i]))





    