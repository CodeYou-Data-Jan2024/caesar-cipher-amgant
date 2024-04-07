#Aliyah Gant's Caesar Cipher
sentence = input("Please enter a sentence: ")
sentence = sentence.lower()
new_sent = ""
alpha = "abcdefghijklmnopqrstuvwxyzabcde"


for s in sentence:
    for a in alpha:
        letter = a
        if a == s:
            switch = alpha.index(a) + 5
            new_sent += alpha[switch]
            break
    if letter != s:
        new_sent += s
print("The encrypted sentence is: " + new_sent)# add your code here
