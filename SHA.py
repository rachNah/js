import hashlib
print("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)

str = "RVCE"
result = hashlib.sha256(str.encode())
# printing the equivalent hexadecimal value.
print("\nThe hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

str = "RVCE COLLEGE OF ENGINEERING"
result = hashlib.sha384(str.encode())
print("\nThe hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

str = "RVCE"
result = hashlib.sha224(str.encode())
print("\nThe hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

str = "RVCE"
result = hashlib.sha512(str.encode())
print("\nThe hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())

str = "RVCE COLLEGE OF ENGINEERING"
result = hashlib.sha1(str.encode())
print("\nThe hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())


