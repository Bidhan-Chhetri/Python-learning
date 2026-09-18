import emoji

emoji_input = input("Input: ")
converted = emoji.emojize(emoji_input, language="alias")
print(converted)