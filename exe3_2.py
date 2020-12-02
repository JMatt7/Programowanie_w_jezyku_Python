#!/usr/bin/env python
import re 
words_to_replace = {'i': 'oraz',
                    'oraz': 'i',
                    'nigdy': 'prawie nigdy',
                    'dlaczego': 'czemu'
                    }

def replace(text: str) -> str:
    splited_text = text.split()
    regex = re.compile('[^a-zA-Z]')
    i = 0
    for word in splited_text:
        if regex.sub('', word.lower()) in words_to_replace:
            splited_text[i] = words_to_replace[regex.sub('', word.lower())]
        
        i += 1
    
    return ' '.join(splited_text)

if __name__ == "__main__":
    print(replace("Dzisiaj się zawachałem i zająkałem. Nie zrobilem tego nigdy oraz nigdy sie to nie wydarzyło w mojej rodzinie. Dlaczego, akurat w tym momencie."))
