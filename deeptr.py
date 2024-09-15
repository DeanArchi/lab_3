from text_translator.deep_module import translate, langdetect, code_lang, language_list

text = "Bonjour tout le monde"
print(translate(text, 'auto', 'uk'))
print(langdetect(text))
print(code_lang('fr'))
language_list('screen', text)
language_list('file', text)
