import os
print(os.path.isfile("data1.txt"))
print(os.path.abspath("data1.txt"))
# os.rename("data1.txt","d1.txt")
print(os.path.isfile("data1.txt"))
print(os.path.isfile("d1.txt"))
print(os.path.abspath("data1.txt"))
print(os.path.abspath("d1.txt"))
# os.remove("d1.txt")
print(os.path.abspath("d1.txt"))
