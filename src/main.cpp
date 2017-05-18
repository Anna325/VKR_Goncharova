#include "../include/LexicalAnalyzer.h"
#include "../include/MorphAnalyzer.h"

#include <iostream>
#include <fstream>

int main() {
	try {
		std::string input, line;
		std::ifstream input_file("data/input.txt");
		while (std::getline(input_file, line, '\n'))
			input += line + ' ';
		input = input.substr(0, input.size() - 1);
		input_file.close();

		std::ofstream output_file("data/output.txt");
		LexicalAnalyzer lex(input);
		std::vector<MorphAnalyzer> morphs;

		morphs.push_back(MorphAnalyzer());
		morphs.push_back(MorphAnalyzer());
		do {
			morphs.push_back(MorphAnalyzer(lex.cur_lex()));
		} while(lex.move_to_next());
		morphs.push_back(MorphAnalyzer());
		morphs.push_back(MorphAnalyzer());

		std::ofstream output_file_pym("data/pymorphy.txt");
		for (int i = 2; i < morphs.size() - 2; ++i) {
			output_file_pym << morphs[i];
		}
		output_file_pym.close();

		for (int i = 2; i < morphs.size() - 2; ++i) {
			if (morphs[i].is_homonym()) {
				if (!morphs[i + 1].is_feature("PNCT"))
					morphs[i].del_tags("INTJ");

				if (morphs[i].get_word().length() / 2 == 1 && morphs[i + 1].is_feature("PNCT"))
					morphs[i].del_tags("PREP CONJ PRCL");

				if ((morphs[i - 1].get_word() == ",") && (morphs[i].is_feature("GRND")))
					morphs[i].del_bsds("GRND");

				if (morphs[i].get_word() == "для" || morphs[i].get_word() == "благодаря" ||
					morphs[i].get_word() == "моя" || morphs[i].get_word() == "включая") {
					if (morphs[i + 1].is_feature("accs"))
						morphs[i].del_bsds("GRND");
					else
						morphs[i].del_tags("GRND");
				}

				if (morphs[i - 1].is_feature("PREP")) {
					morphs[i].del_tags("VERB INFN");
				}

				if (morphs[i - 1].is_feature("PREP")) {
					std::vector<std::string> PREP_case = morphs[i - 1].get_case_of_preps();
					if (PREP_case.size() != 0) {
						morphs[i].del_bsds(PREP_case);
					}
				}

				if (!(morphs[i + 1].is_feature("PNCT") || morphs[i + 1].is_feature("gent")))
					morphs[i].del_tags("COMP");

				if (morphs[i].get_word() == "три") {
					if (morphs[i + 1].is_feature("gent plur")) {
						morphs[i].del_bsds("NUMR");
						if (morphs[i + 1].is_homonym()) {
							morphs[i + 1].del_bsds("nomn");
							morphs[i + 1].del_bsds("plur");
						}
					}
					if (morphs[i + 1].is_feature("accs")) {
						morphs[i].del_bsds("VERB INFN");
						if (morphs[i + 1].is_homonym())
							morphs[i + 1].del_bsds("accs");
					}
				}	

				if (morphs[i].get_word() == "его" || morphs[i].get_word() == "её" || morphs[i].get_word() == "их") {
					if (morphs[i + 1].is_feature("NOUN") || (morphs[i + 1].is_feature("ADJF") && morphs[i + 2].is_feature("NOUN")))
						morphs[i].del_bsds("Apro");
					else
						morphs[i].del_tags("Apro");
				}

				if (morphs[i].get_word() == "мой" || morphs[i].get_word() == "моя" || morphs[i].get_word() == "мою")
					if (morphs[i - 1].is_feature("VERB") || morphs[i - 1].is_feature("INFN"))
						morphs[i].del_tags("INFN VERB GRND");


				if (morphs[i + 1].get_word() == "и" || morphs[i + 1].get_word() == "да" ||
				morphs[i + 1].get_word() == "или" || morphs[i + 1].get_word() == "либо") {
					std::vector< std::vector<std::string> > intersection;
					intersection = morphs[i].get_tags_intersection(morphs[i + 2].get_tags());
					if (intersection.size() != 0) {
						morphs[i].set_tags(intersection);
						morphs[i + 2].set_tags(intersection);
						morphs[i + 1].del_bsds("CONJ");
					}
				}

				if (morphs[i].get_word() == "в" && ((morphs[i + 1].is_feature("NOUN") || morphs[i + 1].is_feature("ADJF") ||
				morphs[i + 1].is_feature("ADJS") || morphs[i + 1].is_feature("NUMR"))))
					morphs[i].del_bsds("PREP");

				if (morphs[i].get_word() == "и" && !(morphs[i - 1].is_feature("PREP")))
					morphs[i].del_bsds("CONJ");

				if (morphs[i].is_feature("VERB") && morphs[i].is_feature("NPRO")) {
					if (morphs[i-1].is_feature("NOUN") || morphs[i-1].is_feature("ADJF") || morphs[i-1].is_feature("PREP") 
					|| morphs[i-1].is_feature("VERB") || morphs[i+1].is_feature("NOUN") || morphs[i+1].is_feature("ADJF"))
						morphs[i].del_bsds("NPRO");
					else
						morphs[i].del_bsds("VERB");
				}
				if (morphs[i].is_feature("NOUN") && morphs[i].is_feature("INFN"))
					if (morphs[i-1].is_feature("PREP") || morphs[i-1].is_feature("ADJF"))
						morphs[i].del_bsds("NOUN");
					else if (morphs[i-1].is_feature("VERB") || morphs[i-1].is_feature("NOUN") || morphs[i-1].is_feature("PRED")
						 || morphs[i-1].is_feature("INFN") || morphs[i+1].is_feature("PREP") || morphs[i+1].is_feature("NPRO")
						 || (morphs[i+1].is_feature("NOUN") && morphs[i+1].is_feature("accs")))
							morphs[i].del_bsds("INFN");

				if (morphs[i].is_feature("NOUN") && morphs[i].is_feature("ADJS"))
					if (morphs[i-1].is_feature("NUMR") || morphs[i-1].is_feature("PREP") || morphs[i-1].is_feature("ADJF") 
					|| morphs[i-1].is_feature("NPRO") || morphs[i-1].is_feature("VERB") || morphs[i-1].is_feature("Anph") 
					|| morphs[i-1].is_feature("ADJS") || morphs[i+1].is_feature("ADJS") || morphs[i-1].is_feature("INFN")
					|| morphs[i-1].is_feature("GRND") || morphs[i+1].is_feature("ADJF") || morphs[i+1].is_feature("VERB")
					|| morphs[i+1].is_feature("NOUN") && (morphs[i+1].is_feature("datv") || morphs[i+1].is_feature("gent"))
					|| morphs[i+1].is_feature("PRED") || morphs[i-1].is_feature("PRTF") || morphs[i-1].is_feature("PRTS")
					|| morphs[i+1].is_feature("PRTF") || morphs[i+1].is_feature("PRTS"))
						morphs[i].del_bsds("NOUN");
					else if (morphs[i-1].is_feature("ADVB") || morphs[i+1].is_feature("NOUN") || morphs[i-1].is_feature("NOUN"))
						morphs[i].del_bsds("ADJS");

				if (morphs[i].is_feature("NOUN") && morphs[i].is_feature("ADJF"))
					if (morphs[i-1].is_feature("ADJF") || morphs[i+1].is_feature("VERB") || morphs[i-1].is_feature("NPRO")
					|| morphs[i+1].is_feature("PREP") || morphs[i+1].is_feature("PRTF") || morphs[i+1].is_feature("PRTS"))
						morphs[i].del_bsds("NOUN");
					else if (morphs[i+1].is_feature("NOUN") || morphs[i-1].is_feature("ADVB"))
						morphs[i].del_bsds("ADJF");

				if (morphs[i].is_feature("NOUN") && morphs[i].is_feature("COMP"))
					if (morphs[i-1].is_feature("ADJF") || morphs[i-1].is_feature("PREP") || morphs[i-1].is_feature("NPRO"))
						morphs[i].del_bsds("NOUN");
					else if (morphs[i+1].is_feature("VERB") || morphs[i+1].is_feature("NOUN"))
						morphs[i].del_bsds("COMP");

				if (morphs[i].is_feature("GRND") && morphs[i].is_feature("ADJF"))
					if (morphs[i+1].is_feature("PREP") || morphs[i+1].is_feature("INFN") 
					|| morphs[i+1].is_feature("NOUN") && morphs[i+1].is_feature("accs"))
						morphs[i].del_bsds("GRND");
					else if (morphs[i-1].is_feature("NOUN") || morphs[i+1].is_feature("NOUN")
						 || morphs[i-1].is_feature("ADJF") || morphs[i+1].is_feature("ADJF"))
						morphs[i].del_bsds("ADJF"); 

				if (morphs[i].is_feature("VERB") && morphs[i].is_feature("ADJF"))
					if (morphs[i-1].get_word() == "я")
						morphs[i].del_bsds("VERB");
					else if (morphs[i-1].is_feature("PREP") || morphs[i-1].is_feature("NOUN") && morphs[i-1].is_feature("accs")
						 || morphs[i-1].is_feature("NPRO") || morphs[i-1].is_feature("VERB") || morphs[i-1].is_feature("INFN")
						 || morphs[i-1].is_feature("ADJF") || morphs[i+1].is_feature("NOUN") && morphs[i+1].is_feature("accs"))
							morphs[i].del_bsds("ADJF");

				if (morphs[i].is_feature("VERB") && morphs[i].is_feature("ADJS"))
					if (morphs[i+1].is_feature("ADVB") || morphs[i+1].is_feature("PREP"))
						morphs[i].del_bsds("VERB");
					else
						morphs[i].del_bsds("ADJS");

				if (morphs[i].is_feature("VERB") && morphs[i].is_feature("ADVB"))
					if (morphs[i-1].is_feature("NOUN") && morphs[i-1].is_feature("accs") 
					|| morphs[i+1].is_feature("NOUN") && morphs[i+1].is_feature("accs") || morphs[i+1].is_feature("PREP"))
						morphs[i].del_bsds("VERB");
					else if (morphs[i-1].is_feature("VERB") || morphs[i+1].is_feature("VERB") 
					|| morphs[i-1].is_feature("GRND") || morphs[i+1].is_feature("GRND"))
						morphs[i].del_bsds("ADVB");


				if (morphs[i].is_feature("VERB") && morphs[i].is_feature("CONJ"))
					if (morphs[i-1].is_feature("accs") && (morphs[i-1].is_feature("NOUN") || morphs[i-1].is_feature("NPRO"))
					|| morphs[i+1].is_feature("accs") && (morphs[i+1].is_feature("NOUN") || morphs[i+1].is_feature("NPRO")))
						morphs[i].del_bsds("VERB");
					else if (morphs[i+1].is_feature("NOUN") || morphs[i+1].is_feature("VERB") || morphs[i+1].get_word() == "уж")
						morphs[i].del_bsds("CONJ");

			}
			output_file << morphs[i];
		}
		output_file.close();
	}
	catch (const char* error) {
		std::cerr << "Error: " << error << '!' << std::endl;
	}
	catch (...) {
		std::cerr << "Unexpected error!" << std::endl;
	}

	return 0;
}