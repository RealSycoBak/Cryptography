def make_maps(a):
  am = {}
  nm = {}
  for i in range(len(a)):
    am[a[i]] = i
    nm[i] = a[i]
  return am,nm

def encoder(m,a):
  base = []
  am = make_maps(a)[0]
  for i in m:
    base = base + [am[i]]
  return base

def add_mod(lst, k, n):
  base = []
  for i in range(n):
    base = base + [(lst[i] + k) % n]
  return base

#def rolling_add_mod(encoded_message, keys,n):
  #keys = list of keys
  #result = []
  #assert len(keys) > 0
  #while_keys = 0
  #for i in encoded_message:
    #keys = keys[while_keys]
    #while_keys = (while_keys + 1) % len(keys)
    #result = result + [(i + keys) % n]
  #return result


#rolling_add_mod([1,0,3],[1,2],3)

def decoder(l,a):
  base = ""
  nm = make_maps(a)[1]
  for i in l:
    base = base + nm[i]
  return base

def encrypt(message, alphabet, key):
	encoder1 = encoder(message, alphabet)
	lengtha = len(alphabet)
	keyadd = add_mod(encoder1, key, lengtha)
	return decoder(keyadd, alphabet)

def decrypt(message, alphabet, key):
	encoder1 = encoder(message, alphabet)
	lengtha = len(alphabet)
	keyadd = add_mod(encoder1, -key, lengtha)
	return decoder(keyadd, alphabet)

def cp_attack(c, A, known_message, known_ciphertext):
	km = encoder(known_message, A)
	kc = encoder(known_ciphertext, A)
	k = kc[0] - km[0]
	return {decrypt(c, A, k): k}

def bruteforce_attacl(c, alphabet):
  d={}
  for i in range(len(alphabet)):
    msg = decrypt(c,alphabet,i)
    d[msg] = i
  return d


alphabet_len = 27

p0 = 61
p1 = 10

s0 = 16
s = s0
counter = {}
for i in range(100):
  s = (s * p0) + p1
  print(s % alphabet_len)

