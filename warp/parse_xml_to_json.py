import xml.etree.cElementTree as cET
import os
import json
import POSclasses
# import PM


def parse_file_to_tags(source, result_list):
    tree = cET.parse(source)
    root = tree.getroot()

    for sentence in root.iter('se'):
        sentence_parses = []

        for word in sentence.findall('w'):
            word_parses = []
            text = word[-1].tail.replace('`', '')

            for analysis in word.findall('ana'):
                lex = analysis.get('lex')
                gr = analysis.get('gr').replace('=', ',').split(',')
                gr[0] = gr[0].replace('-', '')
                gr = POSclasses.to_pymorphy(text, gr, lex)
                word_parses.append(gr)

            sentence_parses.append(word_parses)

            punc = word.tail
            if punc is not None:
                punc = punc.replace(' ', '')
                punc = punc.replace('\n', '')
                punc = punc.replace('--', '-')
                if punc != "":
                    sentence_parses.append([{"text": punc, "lex": punc, "pos": "PNCT"}])

        result_list.append(sentence_parses)


def parse_directory_to_tags(source, destination):
    for filename in os.listdir(source):
        if filename.endswith(".xhtml"):
            sentences = []
            print(source, filename)
            tags_filename = os.path.join(destination, filename[:-6]+'_tags.txt')
            parse_file_to_tags(os.path.join(source, filename), sentences)
            with open(tags_filename, "w", encoding="utf-8") as outfile:
                outfile.write(json.dumps(sentences, indent=4, ensure_ascii=False))


def parse_directory_to_tags_all(source, destination):
    sentences = []
    for filename in os.listdir(source):
        if filename.endswith(".xhtml"):
            print(source, filename)
            parse_file_to_tags(os.path.join(source, filename), sentences)

    with open(destination, "w", encoding="utf-8") as outfile:
        outfile.write(json.dumps(sentences, indent=4, ensure_ascii=False))

result = []

from sys import argv, stderr, exit

if len(argv) != 3:
    stderr.write('Usage: {} <input_filename> <output_filename>\n'.format(argv[0]))
    exit(1)

input_filename = argv[1]
output_filename = argv[2]

parse_file_to_tags(argv[1], result)

with open(output_filename, 'w', encoding='utf8') as t:
    json.dump(result, t, ensure_ascii=False)
