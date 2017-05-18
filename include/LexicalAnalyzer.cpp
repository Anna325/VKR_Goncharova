#include "LexicalAnalyzer.h"

std::regex LexicalAnalyzer :: regex = std::regex("([a-zA-Z]+|[А-пр-ё]+|[,:;.!?-])");


LexicalAnalyzer :: LexicalAnalyzer(const std::string &s): str(s), first(true) {
	it = std::sregex_token_iterator(begin(str), end(str), regex);
	last = std::sregex_token_iterator();
}

std::string LexicalAnalyzer :: cur_lex() const {
	return _to_lower(it->str());
}

bool LexicalAnalyzer :: move_to_next() {
	if (first)
		first = false;

	_pred_it = it;
	++it;
	if (it == last)
		return false;
	else
		return true;
}

std::string LexicalAnalyzer :: _to_lower(const std::string &str) const {

	std::string res = "";

	int i = 0;
	while (i < str.length()) {
		if (str.substr(i, 2) == "А" || str.substr(i, 2) == "а") {
			res += "а";
			i += 2;
		}
		else if (str.substr(i, 2) == "Б" || str.substr(i, 2) == "б") {
			res += "б";
			i += 2;
		}
		else if (str.substr(i, 2) == "В" || str.substr(i, 2) == "в") {
			res += "в";
			i += 2;
		}
		else if (str.substr(i, 2) == "Г" || str.substr(i, 2) == "г") {
			res += "г";
			i += 2;
		}
		else if (str.substr(i, 2) == "Д" || str.substr(i, 2) == "д") {
			res += "д";
			i += 2;
		}
		else if (str.substr(i, 2) == "Е" || str.substr(i, 2) == "е") {
			res += "е";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ж" || str.substr(i, 2) == "ж") {
			res += "ж";
			i += 2;
		}
		else if (str.substr(i, 2) == "З" || str.substr(i, 2) == "з") {
			res += "з";
			i += 2;
		}
		else if (str.substr(i, 2) == "И" || str.substr(i, 2) == "и") {
			res += "и";
			i += 2;
		}
		else if (str.substr(i, 2) == "Й" || str.substr(i, 2) == "й") {
			res += "й";
			i += 2;
		}
		else if (str.substr(i, 2) == "К" || str.substr(i, 2) == "к") {
			res += "к";
			i += 2;
		}
		else if (str.substr(i, 2) == "Л" || str.substr(i, 2) == "л") {
			res += "л";
			i += 2;
		}
		else if (str.substr(i, 2) == "М" || str.substr(i, 2) == "м") {
			res += "м";
			i += 2;
		}
		else if (str.substr(i, 2) == "Н" || str.substr(i, 2) == "н") {
			res += "н";
			i += 2;
		}
		else if (str.substr(i, 2) == "О" || str.substr(i, 2) == "о") {
			res += "о";
			i += 2;
		}
		else if (str.substr(i, 2) == "П" || str.substr(i, 2) == "п") {
			res += "п";
			i += 2;
		}
		else if (str.substr(i, 2) == "Р" || str.substr(i, 2) == "р") {
			res += "р";
			i += 2;
		}
		else if (str.substr(i, 2) == "С" || str.substr(i, 2) == "с") {
			res += "с";
			i += 2;
		}
		else if (str.substr(i, 2) == "Т" || str.substr(i, 2) == "т") {
			res += "т";
			i += 2;
		}
		else if (str.substr(i, 2) == "У" || str.substr(i, 2) == "у") {
			res += "у";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ф" || str.substr(i, 2) == "ф") {
			res += "ф";
			i += 2;
		}
		else if (str.substr(i, 2) == "Х" || str.substr(i, 2) == "х") {
			res += "х";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ц" || str.substr(i, 2) == "ц") {
			res += "ц";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ч" || str.substr(i, 2) == "ч") {
			res += "ч";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ш" || str.substr(i, 2) == "ш") {
			res += "ш";
			i += 2;
		}
		else if (str.substr(i, 2) == "Щ" || str.substr(i, 2) == "щ") {
			res += "щ";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ъ" || str.substr(i, 2) == "ъ") {
			res += "ъ";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ы" || str.substr(i, 2) == "ы") {
			res += "ы";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ь" || str.substr(i, 2) == "ь") {
			res += "ь";
			i += 2;
		}
		else if (str.substr(i, 2) == "Э" || str.substr(i, 2) == "э") {
			res += "э";
			i += 2;
		}
		else if (str.substr(i, 2) == "Ю" || str.substr(i, 2) == "ю") {
			res += "ю";
			i += 2;
		}
		else if (str.substr(i, 2) == "Я" || str.substr(i, 2) == "я") {
			res += "я";
			i += 2;
		}
		else {
			res += str[i];
			++i;
		}
	}

	return res;
}
