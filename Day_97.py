print('Day 97\n')

import base64

print("------Encoding------")

sample_string = input("Enter a string: ")
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Encoded string: {base64_string}\n")


print("\n------Decoding------")

base64_string = input('Enter a encode string: ')
base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = sample_string_bytes.decode("ascii")

print(f"Decoded string: {sample_string}")

