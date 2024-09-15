import random
from deep_translator import GoogleTranslator
from langdetect import detect_langs, DetectorFactory
DetectorFactory.seed = 0


def translate(text: str, src: str, dest: str) -> str:
    """Переклад тексту за допомогою deep_translator."""
    try:
        translator = GoogleTranslator(source=src, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f'Помилка перекладу: {str(e)}'


def langdetect(text: str, flag: str = "all") -> str:
    """Визначення мови та коефіцієнта довіри за допомогою langdetect."""
    try:
        result = detect_langs(text)
        language = result[0]

        if flag == 'lang':
            return f'Мова: {language.lang}'
        if flag == 'confidence':
            return f'Коефіцієнт довіри: {language.prob}'
        return f'Мова: {code_lang(language.lang)}, Коефіцієнт довіри: {language.prob}'
    except Exception as e:
        return f"Помилка визначення мови: {str(e)}"


def code_lang(lang: str) -> str:
    """Функція для переведення коду мови в назву або навпаки."""
    try:
        translator = GoogleTranslator()
        languages = translator.get_supported_languages(as_dict=True)

        if lang in languages:
            return languages[lang]
        if lang in languages.values():
            for code, name in languages.items():
                if name == lang:
                    return code
        return 'Помилка: некоректна мова або код.'
    except Exception as e:
        return f'Помилка: {str(e)}'


def language_list(out: str = 'screen', text: str = '') -> str:
    """Виводить таблицю всіх підтримуваних мов та перекладає текст."""
    try:
        translator = GoogleTranslator()
        languages = dict(random.sample(list(translator.get_supported_languages(as_dict=True).items()), 5))
        output = []
        for i, (code, language) in enumerate(languages.items(), start=1):
            translated_text = translate(text, 'auto', code) if text else ''
            output.append(f'{i:<5} {language:<15} {code:<5} {translated_text}')

        if out == 'screen':
            print(f"{'N':<5} {'Language':<15} {'ISO-639 code':<5} {'Text'}")
            print('-' * 50)
            for line in output:
                print(line)
        if out == 'file':
            with open('languages_list_deep.txt', 'w', encoding='utf-8') as f:
                f.write(f"{'N':<5} {'Language':<15} {'ISO-639 code':<5} {'Text'}\n")
                f.write('-' * 50 + "\n")
                for line in output:
                    f.write(line + "\n")

        return 'Oк'
    except Exception as e:
        return f'Помилка: {str(e)}'
