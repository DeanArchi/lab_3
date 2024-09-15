from text_translator.google_module import translate, langdetect, code_lang, language_list

text = 'Привіт, як справи?'
print(translate(text, 'uk', 'en'))
print(langdetect(text))
print(code_lang('uk'))
language_list('screen', text)
language_list('file', text)
