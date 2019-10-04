from translate import Translator

translator = Translator(to_lang='tl')

with open('test.txt') as my_file:
    text = my_file.read()
    translation = translator.translate(text)

    with open('result.txt', mode='a') as result:
        result.write(translation)
