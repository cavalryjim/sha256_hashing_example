import hashlib

input_string = 'hello world!'

# Generate SHA256 hash
sha256_hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()

# Print the hash
print(f"{input_string} {sha256_hash}")

with open("text_file.txt", "rb") as f:
    # Read the contents of the file
    data = f.read()

# Generate SHA256 hash
sha256_hash = hashlib.sha256(data).hexdigest()

# Print the hash
print(f"text_file.txt {sha256_hash}")

# Expected hash
confirmation_hash = "d16267b56ea53c1b340a3fd9ba7f70d8a6037abf350b492b60264ff32f19faf0"

# Open the file
with open("text_file.txt", "rb") as f:
    # Read the contents of the file
    data = f.read()

# Generate SHA256 hash
sha256_hash = hashlib.sha256(data).hexdigest()

# Compare hashes
if sha256_hash == confirmation_hash:
    print("Hashes match! The file is authentic.")
else:
    print("Hashes do not match! The file may have been tampered with.")


# hashing an image
# Open the file
with open("mike.png", "rb") as f:
    # Read the contents of the file
    data = f.read()
    
# Generate SHA256 hash
sha256_hash = hashlib.sha256(data).hexdigest()

# Print the hash
print(f"mike.png {sha256_hash}")
len(sha256_hash)


# hashing a video file
# Open the file
with open("Afghanistan_homecoming.mov", "rb") as f:
    # Read the contents of the file
    data = f.read()
    
# Generate SHA256 hash
sha256_hash = hashlib.sha256(data).hexdigest()

# Print the hash
print(f"Afghanistan_homecoming.mov {sha256_hash}")
len(sha256_hash)