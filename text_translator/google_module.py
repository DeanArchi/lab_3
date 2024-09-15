import random
from googletrans import Translator
from googletrans.constants import LANGUAGES

translator = Translator()


def translate(text: str, scr: str, dest: str) -> str:
    """Перекладає текст на задану мову або повідомляє про помилку."""
    try:
        translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return f'Помилка перекладу: {e}'


def langdetect(text: str, flag: str = 'all') -> str:
    """Визначає мову тексту та повертає її код або коефіцієнт довіри."""
    try:
        detection = translator.detect(text)
        if flag == 'lang':
            return f'Мова: {detection.lang}'
        if flag == 'confidence':
            return f'Коефіцієнт довіри: {detection.confidence}'
        return f'Мова: {detection.lang}, Коефіцієнт довіри: {detection.confidence}'
    except Exception as e:
        return f'Помилка визначення мови: {e}'


def code_lang(lang: str) -> str:
    """Перетворює назву мови в код або код мови в назву."""
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    if lang in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
    return 'Помилка: некоректна мова або код.'


def language_list(out: str = 'screen', text: str = '') -> str:
    """Виводить таблицю мов і тексту на екран або у файл."""
    try:
        languages = dict(random.sample(list(LANGUAGES.items()), 5))
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
            with open('languages_list_google.txt', 'w', encoding='utf-8') as f:
                f.write(f"{'N':<5} {'Language':<15} {'ISO-639 code':<5} {'Text'}\n")
                f.write('-' * 50 + "\n")
                for line in output:
                    f.write(line + "\n")

        return 'Oк'
    except Exception as e:
        return f'Помилка: {str(e)}'
