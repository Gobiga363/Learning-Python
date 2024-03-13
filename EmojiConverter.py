message = input(" >")
words = message.split(" ")
emojis = {
    ":)": "\U0001F603",
    ":(": "\U0001F622",
    "<3": "\U0001F49C"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


