import string, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_words(filename):
    translator = str.maketrans('', '', string.punctuation)
    words = list()
    file_path = os.path.join(SCRIPT_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            temp = line.translate(translator)
            words.extend(temp.split())
    return words

def get_words_dict(words):
    words_dict = dict()
    for word in words:
        words_dict[word.lower()] = words_dict.get(word.lower(), 0) + 1
    return words_dict

file_name = input("Введите название файла(нажмите Enter для значения по умолчанию): ")
if not file_name:
    file_name = "some_text.txt"
words_list = get_words(file_name)
words_dict = get_words_dict(words_list)
unique_words = sum([v for v in words_dict.values() if v == 1])
print(f"Кол-во слов: {len(words_list)}\nКол-во уникальных слов: {unique_words}\nВсе использованные слова:")
print(*[f"{key} {value}" for key, value in words_dict.items()], sep="\n")