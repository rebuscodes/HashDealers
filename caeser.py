
listify = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
alphabet = list(str(listify))
pineapple=raw_input("enter string to encrypt/decrypt: ")
words = pineapple.split()
ED = raw_input("Encrypt (e) / Decrypt (d): ")
shift= input("enter the shfit amount: ")
output = []

if ED == "e":

    for p in range(0, len(words)):
        en = list(str(words[p]))
        for n in range(0, len(en)):
            for i in range(0, 63):
                if en[n] == alphabet[i]:
                    output.append(alphabet[i+shift])
                else:
                    continue
        output.append(" ")

    encryption="".join(output)
    print encryption

elif ED == "d":
    for p in range(0, len(words)):
        en = list(str(words[p]))
        for n in range(0, len(en)):
            for i in range(0, 63):
                if en[n] == alphabet[i]:
                    output.append(alphabet[i-shift])
                else:
                    continue
        output.append(" ")

    encryption="".join(output)
    print encryption

else:
    print "you fucking suck"
