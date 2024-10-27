import string
from collections import Counter


A = "01234567890-abcdefghijklmnopqrstuvwxyz "
message = "hello there"

def make_maps(A):
  # am associated letters with numbers
  # nm associates numbers with letters
  am, nm = {}, {}
  for i in range(len(A)):
    letter = A[i]
    # assocaites a letter with its position in the alhabet i
    am[letter] = i
    # associates letters position in the alphabet with the letter
    nm[i] = letter
  return am, nm

def encode(message, am):
  result = []
  for letter in message:
    result += [am[letter]]
  return  result

def decode(message, nm):
  result = ""
  for position in message:
    result += nm[position]
  return result

def add_mod(encoded_message, key, n):
  result = []
  for i in encoded_message:
    result += [ (i + key) % n]
  return result 

def rolling_add_mod(encoded_message, keys, n):
  which_key = 0
  assert len(keys) > 0
  result = []
  for i in encoded_message:
    # this is the key we use at this step
    key = keys[which_key]
    # we update the key we are going to use one position to the right wrpaing around to the front 
    which_key = (which_key + 1) % len(keys)
    result += [(i + key ) % n]
  return result

def encrypt(m, keys, A):
  am, nm = make_maps(A)
  encoded_message = encode(m, am)
  encoded_ciphertext = rolling_add_mod(encoded_message, keys, len(A))
  return decode(encoded_ciphertext, nm)

def decrypt(ct, key, A):
  return encrypt(ct, -key, A)

def RNG(s, n):
  while True:
    yield s
    s += 1  % n

ciphertext = "5o12060vbw908c82j3fgeke"
message =  "r0lling-r0lling-r0lling"
key = 15 
keys = [] 
rng = RNG(key, len(A))
for i in range(len(ciphertext)):
  keys += [next(rng)]

#Encryption
ct = encrypt(message, keys, A)
print("encryption: " + ct)
print(keys) 


#decryption (reverse of encryption keys)
keys2 = [ -x for x in keys]
msg = encrypt(ciphertext, keys2, A)
print("decryption: " + msg)
print(keys2)
  


