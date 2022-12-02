mylist = ["hello", "world", "!"]

mylist.append("foo")
mylist[2] = 125
mylist.append(["foo", "bar"])
mylist[-1] = ("tuple", "there")
print(mylist[0])
mylist.pop(1)
print(mylist.count("foo"))

print("mylist: ", mylist)