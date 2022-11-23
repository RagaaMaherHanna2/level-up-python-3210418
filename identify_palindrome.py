import re
def is_palindrome(phrase):
    phrase = re.sub("[^A-Z]", "", phrase, 0, re.IGNORECASE)

    phrase_len = len(phrase)
    is_palindrome_phrase = True
    if phrase_len % 2 == 0:
        left_side = phrase[:phrase_len//2].lower()
        right_side = phrase[(phrase_len//2):].lower()
    else:
        left_side = phrase[:phrase_len//2].lower()
        right_side = phrase[(phrase_len//2) + 1:].lower()
    for i in range(phrase_len//2):
        if left_side[i] != right_side[-1 - i]:
            is_palindrome_phrase = False
            break
    return is_palindrome_phrase



if __name__ == '__main__':

    print(is_palindrome("go hang a salami - I'm a lasagna hog"))
