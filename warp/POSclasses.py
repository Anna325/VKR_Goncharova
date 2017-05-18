import NKRYAtags
import NKRYAtoPymorphyTags as NtoP


class PosS:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.other = []
        self.special = []
        self.gender = None
        self.case = None
        self.anim = None
        self.number = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.other:
                self.other.append(t)
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "NOUN"
        result["gender"] = NtoP.gender.get(self.gender)
        result["case"] = NtoP.case.get(self.case)
        result["anim"] = NtoP.anim.get(self.anim)
        result["number"] = NtoP.number.get(self.number)
#        if self.other or self.special:
#            result["other"] = []
#            for tag in self.other:
#                result["other"].append(NtoP.other.get(tag))
#            for tag in self.special:
#                if tag == "abbr":
#                    result["other"].append(NtoP.other.get(tag))
        return result


class PosA:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.other = []
        self.special = []
        self.gender = None
        self.anim = None
        self.number = None
        self.case = None
        self.brevity = None
        self.comp = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.brevity:
                self.brevity = t
            elif t in NKRYAtags.comp:
                self.comp = t
            elif t in NKRYAtags.other:
                self.other.append(t)
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex

        if self.comp == "comp" or self.comp == "comp2":
            result["pos"] = "COMP"
        elif self.brevity == "brev":
            result["pos"] = "ADJS"
        elif self.brevity == "plen":
            result["pos"] = "ADJF"
        else:
            result["pos"] = "ADJF"

        if result["pos"] == "ADJF":
            result["case"] = NtoP.case.get(self.case)
            result["gender"] = NtoP.gender.get(self.gender)
            result["number"] = NtoP.number.get(self.number)
            if self.comp == "supr":
                result["comp"] = NtoP.comp.get(self.comp)

        if result["pos"] == "ADJS":
            result["gender"] = NtoP.gender.get(self.gender)
            result["number"] = NtoP.number.get(self.number)

        return result


class PosNUM:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.gender = None
        self.anim = None
        self.case = None
        self.comp = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.comp:
                self.comp = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "NUMR"
        result["case"] = NtoP.case.get(self.case)
        return result


class PosANUM:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.gender = None
        self.anim = None
        self.number = None
        self.case = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "ADJF"
        result["case"] = NtoP.case.get(self.case)
        result["gender"] = NtoP.gender.get(self.gender)
        result["number"] = NtoP.number.get(self.number)
        result["other"] = "Anum"
        return result


class PosV:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.gender = None
        self.anim = None
        self.number = None
        self.case = None
        self.brevity = None
        self.aspect = None
        self.transitive = None
        self.voice = None
        self.form = None
        self.mood = None
        self.tense = None
        self.person = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.brevity:
                self.brevity = t
            elif t in NKRYAtags.aspect:
                self.aspect = t
            elif t in NKRYAtags.transitive:
                self.transitive = t
            elif t in NKRYAtags.voice:
                self.voice = t
            elif t in NKRYAtags.form:
                self.form = t
            elif t in NKRYAtags.mood:
                self.mood = t
            elif t in NKRYAtags.tense:
                self.tense = t
            elif t in NKRYAtags.person:
                self.person = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["aspect"] = NtoP.aspect.get(self.aspect)

        if self.form == "partcp":
            if self.brevity == "plen":
                result["pos"] = "PRTF"
            else:
                result["pos"] = "PRTS"
        elif self.form == "ger":
            result["pos"] = "GRND"
        elif self.form == "inf":
            result["pos"] = "INFN"
        else:
            result["pos"] = "VERB"

        if result["pos"] == "INFN":
            result["transitive"] = NtoP.transitive.get(self.transitive)

        if result["pos"] == "PRTS":
            result["tense"] = NtoP.tense.get(self.tense)
            result["gender"] = NtoP.gender.get(self.gender)
            result["number"] = NtoP.number.get(self.number)

        if result["pos"] == "GRND":
            result["transitive"] = NtoP.transitive.get(self.transitive)
            result["tense"] = NtoP.tense.get(self.tense)

        if result["pos"] == "PRTF":
            result["transitive"] = NtoP.transitive.get(self.transitive)
            result["tense"] = NtoP.tense.get(self.tense)
            result["gender"] = NtoP.gender.get(self.gender)
            result["number"] = NtoP.number.get(self.number)
            result["case"] = NtoP.case.get(self.case)

        if result["pos"] == "VERB":
            result["transitive"] = NtoP.transitive.get(self.transitive)
            result["tense"] = NtoP.tense.get(self.tense)
            result["gender"] = NtoP.gender.get(self.gender)
            result["person"] = NtoP.person.get(self.person)
            result["number"] = NtoP.number.get(self.number)
            result["mood"] = NtoP.mood.get(self.mood)

        return result


class PosADV:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.comp = None
        for t in tags:
            if t in NKRYAtags.comp:
                self.comp = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        if self.comp == "comp" or self.comp == "comp2":
            result["pos"] = "COMP"
        else:
            result["pos"] = "ADVB"
        return result


class PosPRAEDIC:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.comp = None
        for t in tags:
            if t in NKRYAtags.comp:
                self.comp = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "PRED"
        return result


class PosPARENTH:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "CONJ"
        result["other"] = "Prnt"
        return result


class PosSPRO:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.gender = None
        self.anim = None
        self.number = None
        self.case = None
        self.person = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.person:
                self.person = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "NPRO"
        result["gender"] = NtoP.gender.get(self.gender)
        result["case"] = NtoP.case.get(self.case)
        result["number"] = NtoP.number.get(self.number)
        result["person"] = NtoP.person.get(self.person)
        return result


class PosAPRO:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.gender = None
        self.anim = None
        self.number = None
        self.case = None
        self.brevity = None
        self.person = None
        for t in tags:
            if t in NKRYAtags.gender:
                self.gender = t
            elif t in NKRYAtags.anim:
                self.anim = t
            elif t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t
            elif t in NKRYAtags.brevity:
                self.brevity = t
            elif t in NKRYAtags.person:
                self.person = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "ADJF"
        result["other"] = "Apro"
        result["case"] = NtoP.case.get(self.case)
        result["gender"] = NtoP.gender.get(self.gender)
        result["number"] = NtoP.number.get(self.number)
        return result


class PosADVPRO:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        self.comp = None
        for t in tags:
            if t in NKRYAtags.comp:
                self.comp = t
            elif t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "ADVB"
        return result


class PosPRAEDICPRO:

    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.number = None
        self.case = None
        for t in tags:
            if t in NKRYAtags.number:
                self.number = t
            elif t in NKRYAtags.case:
                self.case = t

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "XXXX"
        return result


class PosPR:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "PREP"
        return result


class PosCONJ:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "CONJ"
        return result


class PosPART:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "PRCL"
        return result


class PosINTJ:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "INTJ"
        return result


class PosINIT:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "INIT"
        return result


class PosNONLEX:
    def __init__(self, text, tags, lex):
        self.text = text
        self.lex = lex
        self.special = []
        for t in tags:
            if t in NKRYAtags.special:
                self.special.append(t)

    def to_pymorphy(self):
        result = dict()
        result["text"] = self.text
        result["lex"] = self.lex
        result["pos"] = "LATN"
        return result


def to_pymorphy(text, tags, lex):
    pos = tags[0]
    gr = tags[1:]
    if pos == "S":
        return PosS(text, gr, lex).to_pymorphy()
    elif pos == "A":
        return PosA(text, gr, lex).to_pymorphy()
    elif pos == "NUM":
        return PosNUM(text, gr, lex).to_pymorphy()
    elif pos == "ANUM":
        return PosANUM(text, gr, lex).to_pymorphy()
    elif pos == "V":
        return PosV(text, gr, lex).to_pymorphy()
    elif pos == "ADV":
        return PosADV(text, gr, lex).to_pymorphy()
    elif pos == "PRAEDIC":
        return PosPRAEDIC(text, gr, lex).to_pymorphy()
    elif pos == "PARENTH":
        return PosPARENTH(text, gr, lex).to_pymorphy()
    elif pos == "SPRO":
        return PosSPRO(text, gr, lex).to_pymorphy()
    elif pos == "APRO":
        return PosAPRO(text, gr, lex).to_pymorphy()
    elif pos == "ADVPRO":
        return PosADVPRO(text, gr, lex).to_pymorphy()
    elif pos == "PRAEDICPRO":
        return PosPRAEDICPRO(text, gr, lex).to_pymorphy()
    elif pos == "PR":
        return PosPR(text, gr, lex).to_pymorphy()
    elif pos == "CONJ":
        return PosCONJ(text, gr, lex).to_pymorphy()
    elif pos == "PART":
        return PosPART(text, gr, lex).to_pymorphy()
    elif pos == "INTJ":
        return PosINTJ(text, gr, lex).to_pymorphy()
    elif pos == "INIT":
        return PosINIT(text, gr, lex).to_pymorphy()
    elif pos == "NONLEX":
        return PosNONLEX(text, gr, lex).to_pymorphy()
    else:
        return {"text": text, "lex": lex, "pos": "XXXX"}