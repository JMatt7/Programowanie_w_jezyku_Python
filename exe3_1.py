#!/usr/bin/env python
import re
words_to_remove = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']

def remove_words(text: str) -> str:
    splited_text = text.split()
    regex = re.compile('[^a-zA-Z]')

    for word in splited_text:
        if regex.sub('', word.lower()) in words_to_remove:
            splited_text.remove(word)

    return ' '.join(splited_text)




if __name__ == "__main__":
    print(remove_words("Dzisiaj się zawachałem i zająkałem. Nie zrobilem tego nigdy oraz nigdy sie to nie wydarzyło w mojej rodzinie. Dlaczego, akurat w tym momencie."))
        