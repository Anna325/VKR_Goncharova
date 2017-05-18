#ifndef __MORPHANALYZER_H__
#define __MORPHANALYZER_H__

#include <string>
#include <vector>
#include <iostream>

class MorphAnalyzer {
	bool homonym_flag;
	std::string word;
	std::vector<std::vector <std::string> > tags;
	std::vector<std::string> case_of_preps;

	bool _vec_tag_intersection(const int &tag_num, const std::vector<std::string> &vec) const;
	bool _vec_tag_include(const int &tag_num, const std::vector<std::string> &vec) const;
public:
	MorphAnalyzer();
	MorphAnalyzer(const std::string &s);

	void add_cases_to_PREP();

	std::vector< std::vector<std::string> > get_tags_intersection(const std::vector< std::vector<std::string> > &tag2) const;
	std::vector<std::string> get_case_of_preps() const;
	std::string get_word() const;
	std::vector< std::vector<std::string> > get_tags() const;
	
	void set_tags(const std::vector< std::vector<std::string> > new_tags);

	bool is_homonym() const;

	bool is_feature(const std::string &feature) const;

	void del_tags(const std::string &str_del_tags);
	void del_bsds(const std::string &str_svd_tags);
	void del_bsds(const std::vector<std::string> &str_svd_tags);

	friend std::ostream& operator<<(std::ostream& os, const MorphAnalyzer& morph);
};

#endif
// do not add anything here