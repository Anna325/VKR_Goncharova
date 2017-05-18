import json
from collections import OrderedDict

to_nkrya = {
'gender': {
    "masc": "m",
    "femn": "f",
    "ms-f": "b",
    "neut": "n",
    None: "-"
},

'anim': {
    "anim": "a",
    "inan": "i",
    None: "-"
},

'number': {
    "sing": "s",
    "plur": "p",
    None: "-"
},

'comp': {
    "Supr": "s",
    None: "-"
},

'case': {
    "nomn": "n-",
    "gent": "g-",
    "datv": "d-",
    "accs": "a-",
    "ablt": "i-",
    "loct": "l-",
    "gen2": "-g",
    "acc2": "-a",
    "loc2": "-l",
    "voct": "v-",
    None: "--"
},

'aspect': {
    "perf": "p",
    "impf": "i",
    None: "-"
},

'transitive': {
    "tran": "t",
    "intr": "i",
    None: "-"
},

'mood': {
    "indc": "n",
    "impr": "m",
    None: "-"
},

'tense': {
    "past": "p",
    "pres": "n",
    "futr": "f",
    None: "-"
},

'person': {
    "1per": "1",
    "2per": "2",
    "3per": "3",
    None: "-"
},

'other': {
    "Anum": "n",
    "Apro": "p",
    "Prnt": "r",
    None: "-"
}

}

def to_short_tag(tags):

    result = tags["pos"]
    result += gender[tags.get("gender")]
    result += case[tags.get("case")]
    result += number[tags.get("number")]
    result += anim[tags.get("anim")]
    result += comp[tags.get("comp")]
    result += aspect[tags.get("aspect")]
    result += transitive[tags.get("transitive")]
    result += tense[tags.get("tense")]
    result += person[tags.get("person")]
    result += mood[tags.get("mood")]
    result += other[tags.get("other")]

    return result

def compare_all_tags(tags1_all, tags2):
    tags11_good = 0
    for tags1 in tags1_all:
        if tags1['text'].lower() != tags2['text'].lower():
            return -1
        is_good = True
        for k in tags2.keys():
            if not k in tags1.keys():
                continue
            if k == 'text':
                continue
            if tags1[k] != tags2[k]:
                is_good = False
        same_lex = True
        if is_good:
            tags11_good = 1
    return tags11_good

def compare_first_tag(tags1, tags2):
    tags1 = tags1[0]
    if tags1['text'].lower() != tags2['text'].lower():
        return -1
    is_good = True
    for k in tags2.keys():
        if not k in tags1.keys():
            continue
        if k == 'text':
            continue
        if tags1[k] != tags2[k]:
            is_good = False
    same_lex = True
    if is_good:
        return 1
    else:
        return 0


def compare_tags(correct, tag):
    for cor in correct:
        answer = compare_first_tag(tag, cor)
        if answer == 1:
            return 1
        elif answer == -1:
            return -1
    return 0


def compare_files(correct_file, file):
    with open(correct_file, "r", encoding="utf-8") as infile:
        correct_sentences = json.loads(infile.read(), encoding="utf-8", object_pairs_hook=OrderedDict)

    with open(file, "r", encoding="utf-8") as infile:
        sentences = json.loads(infile.read(), encoding="utf-8", object_pairs_hook=OrderedDict)

    word_count = 0
    correct_tag_count = 0

    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            print('{}: '.format(sentences[i][j][0]['text']), end = '')
            answer = compare_tags(correct_sentences[i][j], sentences[i][j])
            if answer == 1:
                word_count += 1
                correct_tag_count += 1
                print('ВЕРНО!')
                for k, v in sentences[i][j][0].items():
                    print('\t{}: {}'.format(k, v))
            elif answer == 0:
                word_count += 1
                print('НЕВЕРНО!')
                for variant in sentences[i][j]:
                    for k, v in variant.items():
                        print('\t{}: {}'.format(k, v))
                    print('\t--------')
                print('ВЕРНЫЙ ВАРИАНТ:')
                for variant in correct_sentences[i][j]:
                    for k, v in variant.items():
                        print('\t{}: {}'.format(k, v))
                    print('\t--------')
            else:
                print(correct_sentences[i][j][0]['text'], end='')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    return 100 * correct_tag_count / word_count

if __name__ == "__main__":
    from sys import argv, stderr, exit

    if len(argv) != 3:
        stderr.write('Usage: {} <gt_filename> <result_filename>\n'.format(argv[0]))
        exit(1)

    gt_filename = argv[1]
    result_filename = argv[2]

    print(compare_files(argv[1], argv[2]))
