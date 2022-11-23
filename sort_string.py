def sort_string(phrase):
    phrase = [word.lower() for word in phrase.split()]
    phrase.sort()
    return ' '.join(phrase)
     


if __name__ == '__main__':
    print(sort_string('banana ORANGE apple'))
