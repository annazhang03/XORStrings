import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()#[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()#[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False
if mode == "human":
    human = True
elif mode == "numOut":
    human = False
else:
    debug = True

if(debug):
    print("arguments were entered incorrectly")
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)
    sys.exit()


# wrap key
l = len(key)
if l < len(inp):
    i = l
    while i < len(inp):
        key += key[i % l]
        i += 1
ciph = ""
for j in range(len(key)):
    result = ord(key[j]) ^ ord(inp[j])
    if human:
        ciph += chr(result)
    else:
        ciph += str(hex(result))[2:] + " "
print(ciph)