
def simple_hash(key, size):
            return key % size

key_num = int(input("Enter a Key Value : "))
size_num = int(input("Enter a Size Value : "))

print(f"The key {key_num} and size {size_num} hash of {simple_hash(key=key_num, size=size_num)}")