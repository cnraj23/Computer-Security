

str = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"

List = list(str)
#print (List)
Unique = set(List)
print ("Unique Variables from Given String: \n")
print (Unique)
elements = {}
for key in Unique:
   elements[key] = str.count(key)

print("\nSorted Elements:\n")
elements = sorted(elements.items(), key=lambda x: x[1], reverse = True)
print(elements)
print("\n\nPrinting Decrypted String: \n")


new_str = str.replace("5", "a")
new_str = new_str.replace("3", "g")
new_str = new_str.replace("‡", "o")
new_str = new_str.replace("†", "d")
new_str = new_str.replace("0", "l")
new_str = new_str.replace(")", "s")
new_str = new_str.replace("6", "i")
new_str = new_str.replace("*", "n")
new_str = new_str.replace(";", "t")
new_str = new_str.replace("4", "h")
new_str = new_str.replace("8", "e")
new_str = new_str.replace("2", "b")
new_str = new_str.replace(".", "p")
new_str = new_str.replace("¶", "v")
new_str = new_str.replace("(", "r")
new_str = new_str.replace("9", "m")
new_str = new_str.replace("?", "u")
new_str = new_str.replace(":", "y")
new_str = new_str.replace("—", "c")
new_str = new_str.replace("1", "f")
new_str = new_str.replace("]", "w")



print (new_str);
