# filetr.py
import os
from text_translator.google_module import translate


def load_config():
    config = {}
    with open("config.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(':')
            config[key.strip()] = value.strip()
    return config


def read_file(file_name, max_chars, max_words, max_sentences):
    text = ""
    char_count, word_count, sentence_count = 0, 0, 0

    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            char_count += len(line)
            word_count += len(line.split())
            sentence_count += line.count('.') + line.count('!') + line.count('?')
            text += line

            if char_count > max_chars or word_count > max_words or sentence_count > max_sentences:
                break

    return text


if __name__ == "__main__":
    config = load_config()
    file_name = config["File Name"]

    if not os.path.exists(file_name):
        print("Файл не знайдено.")
    else:
        text = read_file(file_name, int(config["Characters"]), int(config["Words"]), int(config["Sentences"]))
        translated_text = translate(text, 'uk', config["Language"])

        if config["Output"] == "screen":
            print(f"Переклад на {config['Language']}: {translated_text}")
        if config["Output"] == "file":
            base_name, ext = os.path.splitext(file_name)
            output_file_name = f"{base_name}_{config['Language']}.txt"
            with open(output_file_name, "w", encoding='utf-8') as out_file:
                out_file.write(translated_text)
            print("Ok")
