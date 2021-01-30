"""В произвольном тексте найти и отпечатать слова, содержащие букву Е."""
import re
"Свинья под Дубом вековым Наелась желудей досыта, до отвала; Наевшись, выспалась под ним; Потом, глаза продравши, встала И рылом подрывать у Дуба корни стала. Есссссы"



def search_word_by_constant(text, constant):
    """Функция поиск слова содержащее constant без учета регистра"""
    result = re.findall(rf'\w+{constant.lower()}\w+|\w+{constant.upper()}\w+'
                        rf'|{constant.lower()}\w+|{constant.upper()}\w+'
                        rf'|\w+{constant.lower()}|\w+{constant.upper()}', text)
    return result


def information_output(text, constant, result):
    text_result = f"Из введенного текста:\n{text}\n" \
                  f"Найдены следующие слова содержащие букву {constant.upper()}:\n" \
                  f"{','.join(result)}"
    print(text_result)


if __name__ == '__main__':
    text = str(input('Введите текст для поиска: '))
    constant = str(input('Введите букву которую будет содержать слово: '))
    result = search_word_by_constant(text, constant)
    information_output(text, constant, result)
