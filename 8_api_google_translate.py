from googletrans import Translator

translator = Translator()
result = translator.translate("ERROR: pip's dependency resolver does not currently take into account all the packages"
                              "that are installed. This behaviour is the source of the following dependency conflicts",
                              src='en', dest='ru')

print(result.src)
print(result.dest)
print(result.text)
#print(googletrans.LANGUAGES)

with open("english_text.txt", "r") as file:
    content = file.read()
res = translator.translate(content, dest='ru')

with open("russian_text.txt", "w") as file:
    file.write(res.text)




