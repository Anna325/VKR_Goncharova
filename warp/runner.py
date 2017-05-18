import re
from sys import argv, stderr, exit
from os import system, path
import json
from tqdm import tqdm
from collections import OrderedDict

conformity = {
	'pos': ['NOUN', 'ADJF', 'ADJS', 'COMP', 'NUMR', 'INFN', 'PRTS', 'GRND', 'PRTF', 
			'VERB', 'ADVB', 'PRED', 'CONJ', 'NPRO', 'PNCT', 'PREP', 'PRCL', 'INTJ', 'INIT', 'LATN'],
	'gender': ['masc', 'femn', 'ms-f', 'neut'],
	'case': ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct', 'gen2', 'acc2', 'loc2', 'voct'],
	'number': ['sing', 'plur'],
	'anim': ['anim', 'inan'],
	'comp': ['sup2'],
	'aspect': ['perf', 'impf'],	
	'transitive': ['intr', 'tran'],
	'tense': ['past', 'pres', 'futr'],
	'person': ['1per', '2per', '3per'],
	'mood': ['indc', 'imp2'],
	'other': ['Anum', 'Apro', 'Prnt']
}

def check_key(word):
	for key, value in conformity.items():
		if word in value:
			return key
	return None


ROOT_DIR = '/Users/Anna/Desktop/VKR_Goncharova'
DATA_DIR = path.join(ROOT_DIR, 'data')
input_filename = path.join(DATA_DIR, 'input.txt')
output_filename = path.join(DATA_DIR, 'output.txt')
output_pymorphy = path.join(DATA_DIR, 'pymorphy.txt')

BIN_DIR = path.join(ROOT_DIR, 'bin')
script_filename = path.join(BIN_DIR, 'main')

if len(argv) != 3:
	stderr.write('Usage: {} <input_filename> <output_filename>\n'.format(argv[0]))
	exit(1)

filename = argv[1]
result_filename = argv[2]
result_pymorphy = path.join(DATA_DIR, 'pymorphy.json')

with open(filename, 'r') as f:
	text = f.read()

input_sentences = [sentence + '.' for sentence in re.split("[\n.!?]+", text) if sentence != '']

sentences = list()
psentences = list()

for input_sentence in tqdm(input_sentences):
	sentence = list()
	psentence = list()
	with open(input_filename, 'w') as t:
		t.write(input_sentence)

	system(script_filename)

	pword_all = list()
	pword_flag = False

	with open(output_pymorphy, 'r') as f:
		for line in f:
			line = line.rstrip()
			if line == '~~~~':
				psentence.append(pword_all)
				pword_all = list()
				pword_flag = False
				continue
			if not pword_flag:
				word_text = line
				pword_flag = True
				continue
			pword = OrderedDict()
			pword['text'] = word_text
			pword.update([(check_key(w), w) for w in line.split(',') if check_key(w) != None])
			pword_all.append(pword)

	psentences.append(psentence)

	word_all = list()
	word_flag = False

	with open(output_filename, 'r') as f:
		for line in f:
			line = line.rstrip()
			if line == '~~~~':
				sentence.append(word_all)
				word_all = list()
				word_flag = False
				continue
			if not word_flag:
				word_text = line
				word_flag = True
				continue
			word = OrderedDict()
			word['text'] = word_text
			word.update([(check_key(w), w) for w in line.split(',') if check_key(w) != None])
			word_all.append(word)

	sentences.append(sentence)

with open(result_filename, 'w', encoding='utf8') as t:
	json.dump(sentences, t, ensure_ascii=False)

with open(result_pymorphy, 'w', encoding='utf8') as t:
	json.dump(psentences, t, ensure_ascii=False)




