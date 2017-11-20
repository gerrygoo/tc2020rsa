from RSA import RSA
import random
primes = [541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659]
primes2 = [661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811]

rsa = RSA(random.choice(primes), random.choice(primes2))
print("P:", rsa.p, "Q:", rsa.q)
print("N:", rsa.N)
print("ϕ(N):", rsa.ϕ)
print("Public key:", rsa.public_key)
print("Private key:", rsa.private_key)

print()
print()

message = input("Message:")

print("Parsed:", [ord(i) for i in message])

print()
message_encrypted = [rsa.encrypt(ord(el)) for el in message]
print("Encrypted:", message_encrypted)

message_decrypted = [rsa.decrypt(el) for el in message_encrypted]
print("Decrypted:", message_decrypted)
print()

print("Parsed:", "".join([chr(el) for el in message_decrypted]))