# Diffie Hillman Key Exchange
# q > 29
q = 41

# is q prime?
print("q: ", q)
print("Is q prime?: ", 2**(q-1) % q == 1)

p = 2*q + 1
print("p: ", p)
print("Is p prime?: ", 2**(p-1) % p == 1)

g = 2
print("g: ", g)
print("Is a generator of p?: ", g ** ((p-1)/2) % p != 1)
print(g ** ((p - 1) / 2) % p)

# Alice sends a = 5 and Bob sends b = 7
a = 13
b = 21

A_to_Bob = g**a % p
B_to_Alice = g**b % p

print("A_to_Bob: ", A_to_Bob)
print("B_to_Alice: ", B_to_Alice)


key_Alice = B_to_Alice**a % p
key_Bob = A_to_Bob**b % p
shared = g**(a*b) % p
print("key_Alice: ", key_Alice)
print("key_Bob: ", key_Bob)
print("shared: ", shared)
# Shared in binary
print("shared in binary: ", bin(shared))

# Send a message
message = 10
print("message: ", message)
print("message in binary: ", bin(message))

# Encrypt the message
encrypted = message ^ key_Alice
print("encrypted: ", encrypted)
print("encrypted in binary: ", bin(encrypted))

# Decrypt the message
decrypted = encrypted ^ key_Bob
print("decrypted: ", decrypted)
print("decrypted in binary: ", bin(decrypted))

print("message == decrypted: ", message == decrypted)