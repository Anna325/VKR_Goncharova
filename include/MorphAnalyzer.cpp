#include "MorphAnalyzer.h"
#include "LexicalAnalyzer.h"

#include <stdio.h>

bool MorphAnalyzer :: _vec_tag_intersection(const int &tag_num, const std::vector<std::string> &vec) const {
	bool res = false;

	for (int i = 0; i < vec.size(); ++i) {
		for (int j = 0; j < tags[tag_num].size(); ++j) {
			if (tags[tag_num][j] == vec[i]) {
				res = true;
				break;
			}
		}
		if (res)
			break;
	}

	return res;
}

bool MorphAnalyzer :: _vec_tag_include(const int &tag_num, const std::vector<std::string> &vec) const {
	bool res = false;
	int cnt;

	for (int i = 0; i < vec.size(); ++i) {
		cnt = 0;
		for (int j = 0; j < tags[tag_num].size(); ++j) {
			if (tags[tag_num][j] == vec[i]) {
				++cnt;
				break;
			}
		}
		if (cnt == vec.size()) {
			res = true;
			break;
		}
	}

	return res;
}

MorphAnalyzer :: MorphAnalyzer() {
	word = "";
	homonym_flag = false;
}


MorphAnalyzer :: MorphAnalyzer(const std::string &s): word(s) {
	FILE *fp = popen(("python src/parse.py " + s).c_str(), "r");
	char buf[1024];
	std::vector<std::string> str_vec;

	while(fgets(buf, 1024, fp)) {
		LexicalAnalyzer str(buf);

		do {
			str_vec.push_back(str.cur_lex());
		} while (str.move_to_next());

		tags.push_back(str_vec);
		str_vec.clear();
	}

	add_cases_to_PREP();

	if (tags.size() > 1)
		homonym_flag = true;
}

void MorphAnalyzer :: add_cases_to_PREP() {
	std::vector<std::string> PREP_case;
	bool is_PREP = false;
	int first_PREP = -1;

	for (int i = 0; i < tags.size(); ++i)
		if (tags[i][0] == "PREP") {
			is_PREP = true;
			first_PREP = i;
			break;
		}

	if (is_PREP) {
		if (word == "без" || word == "у" || word == "до" || word == "от"
		|| word == "с" || word == "около" || word == "из" || word == "возле"
		|| word == "после" || word == "для" || word == "вокруг")
			PREP_case.push_back("gent");

		if (word == "к" || word == "по")
			PREP_case.push_back("datv");

		if (word == "в" || word == "за" || word == "на" || word == "про" || word == "через")
			PREP_case.push_back("accs");

		if (word == "за" || word == "над" || word == "под" || word == "перед" || word == "с")
			PREP_case.push_back("ablt");

		if (word == "в" || word == "на" || word == "о" || word == "об"
		|| word == "обо" || word == "при")
			PREP_case.push_back("loct");

		if (PREP_case.size()) {
			tags[first_PREP].push_back(PREP_case[0]);
			for (int j = 1; j < PREP_case.size(); ++j) {
				std::vector<std::string> tmp;
				tmp.push_back("PREP");
				tmp.push_back(PREP_case[j]);
				tags.insert(tags.begin() + first_PREP, tmp);
			}
		}
		case_of_preps = PREP_case;
	}
}

std::vector< std::vector<std::string> > MorphAnalyzer :: get_tags_intersection(const std::vector< std::vector<std::string> > &tag2) const {
	std::vector< std::vector<std::string> > res;

	for (int i = 0; i < tags.size(); ++i)
		for (int j = 0; j < tag2.size(); ++j)
			if (tags[i] == tag2[j]) {
				res.push_back(tags[i]);
				break;
			}

	return res;
}

std::vector<std::string> MorphAnalyzer :: get_case_of_preps() const {
	return case_of_preps;
}

std::string MorphAnalyzer :: get_word() const {
	return word;
}

std::vector< std::vector<std::string> > MorphAnalyzer :: get_tags() const {
	return tags;
}

void MorphAnalyzer :: set_tags(const std::vector< std::vector<std::string> > new_tags) {
	tags = new_tags;
}


bool MorphAnalyzer :: is_homonym() const {
	bool res = false;
	if (tags.size() > 1)
		res = true;
	return res;
}


bool MorphAnalyzer :: is_feature(const std::string &feature) const {
	std::vector<std::string> vec_features;
	LexicalAnalyzer str(feature);

	do {
		vec_features.push_back(str.cur_lex());
	} while (str.move_to_next());

	bool res = false;

	for (int i = 0; i < tags.size(); ++i)
		if (_vec_tag_include(i, vec_features)) {
			res = true;
			break;
		}

	return res;
}

void MorphAnalyzer :: del_tags(const std::string &str_del_tags) {
	LexicalAnalyzer str(str_del_tags);
	std::vector<std::string> vec_del_tags;

	do {
		vec_del_tags.push_back(str.cur_lex());
	} while (str.move_to_next());

	for (int i = tags.size() - 1; i >= 0; --i)
		if (_vec_tag_intersection(i, vec_del_tags))
			tags.erase(tags.begin() + i);
}

void MorphAnalyzer :: del_bsds(const std::string &str_svd_tags) {
	LexicalAnalyzer str(str_svd_tags);
	std::vector<std::string> vec_svd_tags;

	do {
		vec_svd_tags.push_back(str.cur_lex());
	} while (str.move_to_next());

	for (int i = tags.size() - 1; i >= 0; --i)
		if (!_vec_tag_intersection(i, vec_svd_tags))
			tags.erase(tags.begin() + i);
}

void MorphAnalyzer :: del_bsds(const std::vector<std::string> &vec_svd_tags) {
	for (int i = tags.size() - 1; i >= 0; --i)
		if (!_vec_tag_intersection(i, vec_svd_tags))
			tags.erase(tags.begin() + i);
}


std::ostream& operator<<(std::ostream& os, const MorphAnalyzer& morph)
{
	os << morph.word << std::endl;
	for (int i = 0; i < morph.tags.size(); ++i) {
		for (int j = 0; j < morph.tags[i].size(); ++j) {
			os << morph.tags[i][j];
			if (j != morph.tags[i].size() - 1)
				os << ',';
			else
				os << std::endl;
		}
	}
	os << "~~~~" << std::endl;


	return os;
}