import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()#[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()#[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False
if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

# wrap key
if len(key) < len(inp):
    i = len(key)
    while i < len(inp):
        key += key[i % len(key)]
        i += 1
ciph = ""
for j in range(len(key)):
    ciph += chr(ord(key[j]) ^ ord(inp[j]))
print(ciph)