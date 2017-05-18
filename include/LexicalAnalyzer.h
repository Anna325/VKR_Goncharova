#ifndef __LEXICALANALYZER_H__
#define __LEXICALANALYZER_H__

#include <regex>
#include <string>

class LexicalAnalyzer {
	std::string str;
	std::sregex_token_iterator it;
	std::sregex_token_iterator last;
	std::sregex_token_iterator _pred_it;
	static std::regex regex;

	bool first;

	std::string _to_lower(const std::string &str) const;
public:
	LexicalAnalyzer(const std::string &s);

	std::string cur_lex() const;

	bool move_to_next();
};

#endif
// do not add anything here