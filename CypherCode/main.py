
#Alphabet
def alphabet_to_maps(alphabet):
	return alphabet_to_maps_helper(alphabet, {}, {}, 0)


# helper function
def alphabet_to_maps_helper(alphabet, num_map, alpha_map, n):
	#base case
	if len(alphabet) == 0:
		return alpha_map, num_map
	else:
		# get the first character
		c = alphabet[0]
		# create the mapping
		# associate the character c to the current integer n
		alpha_map[c] = n
		# associate the current integer n to the character c
		num_map[n] = c
		# increment the number of characters
		n += 1
		# recursive call
		return alphabet_to_maps_helper(alphabet[1:], num_map, alpha_map, n)


#Encode
#What is the return type of this function?
#A = List
#What is the base case of this function? i.e., how do we know we are out of work to do?
#A = If the length of the message is 0 (empty)
#What is the recursive case?
#A = encode(message[1:])
a = {'a': 0, 'b': 1, 'c': 2, 'd': 3, ' ': 4}


def encode(message, alpha_map):
	if len(message) == 0:
		return []
	return [alpha_map[message[0]]] + encode(message[1:], alpha_map)


assert encode("dad", a) == [3, 0, 3]
assert encode("bad", a) == [1, 0, 3]
assert encode("cbd", a) == [2, 1, 3]
assert encode("bc ", a) == [1, 2, 4]


#Add Key
#What is the return type of this function?
#A-List
#What is the base case of this function? i.e., how do we know we are out of work to do?
#A- When the length of the list is 0 (empty) return the empty list
#What is the recursive case?
#A- add_mod(lst[1:], k, n)
def add_mod(lst, k, n):
	if len(lst) == 0:
		return []
	new = (lst[0] + k) % n
	return [new] + add_mod(lst[1:], k, n)


assert add_mod([3, 0, 3], 2, 5) == [0, 2, 0]
assert add_mod([3, 0, 3], 3, 5) == [1, 3, 1]
assert add_mod([3, 0, 3], 4, 5) == [2, 4, 2]
assert add_mod([3, 0, 3], 1, 5) == [4, 1, 4]

#Decode
#What is the return type of this function?
#A-String
#What is the base case of this function? i.e., how do we know we are out of work to do?
#A- When the length of the list is 0 (empty) return the empty string
#What is the recursive case?
#A- decode(lst[1:], num_map)
n = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: ' '}


def decode(lst, num_map):
	if len(lst) == 0:
		return ""
	return num_map[lst[0]] + decode(lst[1:], num_map)


assert decode([0, 2, 0], n) == "aca"
assert decode([3, 0, 3], n) == "dad"
assert decode([1, 2, 4], n) == "bc "
assert decode([2, 1, 3], n) == "cbd"


#encrypt
def encrypt(message, alphabet, key):
	maps = alphabet_to_maps(alphabet)
	encoder = encode(message, maps[0])
	lengtha = len(alphabet)
	keyadd = add_mod(encoder, key, lengtha)
	return decode(keyadd, maps[1])


assert encrypt("dad", "abcd ", 2) == "aca"
assert encrypt("bad", "abcd ", 3) == " db"
assert encrypt("bc ", "abcd ", 4) == "abd"
assert encrypt("adc", "abcd ", 1) == "b d"


#decrypt
def decrypt(message, alphabet, key):
	maps = alphabet_to_maps(alphabet)
	encoder = encode(message, maps[0])
	lengtha = len(alphabet)
	keyadd = add_mod(encoder, -key, lengtha)
	return decode(keyadd, maps[1])


assert decrypt("aca", "abcd ", 2) == "dad"
assert decrypt(" db", "abcd ", 3) == "bad"
assert decrypt("abd", "abcd ", 4) == "bc "
assert decrypt("b d", "abcd ", 1) == "adc"


#cp_attack
#Explain how you can use this known plaintext+ ciphertext pair to recover the key and decrypt the original message
#A = turn them into lists of numbers and then find the difference between them, and thats the key
def cp_attack(c, A, known_message, known_ciphertext):
	alpha_map = alphabet_to_maps(A)[0]
	km = encode(known_message, alpha_map)
	kc = encode(known_ciphertext, alpha_map)
	k = kc[0] - km[0]
	return {decrypt(c, A, k): k}


assert cp_attack("aca", "abcd ", "bad", "dca") == {"dad": 2}
assert cp_attack("aba", "abcd ", "bad", "dca") == {"d d": 2}
assert cp_attack("bab", "abcd ", "bcb", " a ") == {"dcd": 3}

#How many possible unique keys are there for the Caesar Cipher with an alphabet of length n
#Creating a Brute Forcer
#A- n keys
message = bytes.fromhex("5c446e356f63646e356f637e356d7e60673578607e6e606d6e356b6067607c7e3a5e").decode()

def bruteforce_attacl(c, alphabet, d={}, k=0):
	if k == len(alphabet):
		return d
	else:
		msg = decrypt(c, alphabet, k)
		d[msg] = k
		return bruteforce_attacl(c, alphabet, d, k + 1)
bruteforce_attacl(message, "caesr")

#Creating a smart Cracker: Using word frequencies idk what to do
def smart_cracker(msg):
	frequencies = {
	    'e': 0.127,
	    't': 0.0906,
	    'a': 0.0817,
	    'o': 0.0751,
	    'i': 0.0697,
	    'n': 0.0675,
	    's': 0.0633,
	    'h': 0.0609,
	    'r': 0.0599,
	    'd': 0.0425,
	    'l': 0.0403,
	    'c': 0.0278,
	    'u': 0.0276,
	    'm': 0.0241,
	    'w': 0.0236,
	    'f': 0.0223,
	    'g': 0.0202,
	    'y': 0.0197,
	    'p': 0.0193,
	    'b': 0.0129,
	    'v': 0.0098,
	    'k': 0.0077,
	    'j': 0.0015,
	    'x': 0.0015,
	    'q': 0.001,
	    'z': 0.0007
	}
