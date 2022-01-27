from random import randrange, choice


def get_jokes(numb, not_rep=True):
    """
    Generate jokes from inner lists of words

    :param numb: number of jokes
    :param not_rep: False-words in jokes can repit, True -words in jokes don't repit
    :return: list of random jokes

    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if not_rep and len(min(nouns, adverbs, adjectives)) < numb:
        numb = len(min(nouns, adverbs, adjectives))
    for i in range(numb):
        if not_rep:
            print(f'{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))} {adjectives.pop(randrange(len(adjectives)))}')
        else:
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')


get_jokes(10)
