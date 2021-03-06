
gender = {
    "m": "masc",    # мужской род (работник, стол)
    "f": "femn",    # женский род (работница, табуретка)
    "m-f": "ms-f",  # «общий род» (задира, пьяница)
    "n": "neut"     # средний род (животное, озеро)
}

anim = {
    "anim": "anim",     # одушевленность (человек, ангел, утопленник)
    "inan": "inan"      # неодушевленность (рука, облако, культура)
}

number = {
    "sg": "sing",   # единственное число (яблоко, гордость)
    "pl": "plur"    # множественное число (яблоки, ножницы, детишки)
}

case = {
    "nom": "nomn",      # именительный падеж (голова, сын, степь, сани, который)
    "gen": "gent",      # родительный падеж (головы, сына, степи, саней, которого)
    "dat": "datv",      # дательный падеж (голове, сыну, степи, саням, которому)
    "dat2": "datv",     # дистрибутивный дательный ([по] многу, нескольку, стольку)
    "acc": "accs",      # винительный падеж (голову, сына, степь, сани, который/которого)
    "ins": "ablt",      # творительный падеж (головой, сыном, степью, санями, которым)
    "loc": "loct",      # предложный падеж ([о] голове, сыне, степи, санях, котором)
    "gen2": "gen2",     # второй родительный падеж (чашка чаю)
    "acc2": "acc2",     # второй винительный падеж (постричься в монахи; по два человека)
    "loc2": "loc2",     # второй предложный падеж (в лесу, на оси́)
    "voc": "voct",      # звательная форма (Господи, Серёж, ребят)
    "adnum": "accs"     # счётная форма (два часа́, три шара́)
}

comp = {
    "supr": "Supr"      # превосходная степень (глубочайший)
}

aspect = {
    "pf": "perf",   # cовершенный вид (пошёл, встречу) (perfect)
    "ipf": "impf"   # несовершенный вид (ходил, встречаю) (inperfect)
}

transitive = {
    "intr": "intr",     # непереходность (ходить, вариться)
    "tran": "tran"      # переходность (вести, варить)
}

voice = {
    "act": "actv",      # действительный залог (разрушил, разрушивший)
    "pass": "pssv",     # страдательный залог (только у причастий: разрушаемый, разрушенный)
    "med": ""       # медиальный, или средний залог (глагольные формы на -ся: разрушился и т.п.)
}

mood = {
    "indic": "indc",    # изъявительное наклонение (украшаю, украшал, украшу)
    "imper": "impr",    # повелительное наклонение (украшай)
    "imper2": "impr"    # форма повелительного наклонения 1 л. мн. ч. на -те (идемте)
}

tense = {
    "praet": "past",    # прошедшее время (украшали, украшавший, украсив)
    "praes": "pres",    # настоящее время (украшаем, украшающий, украшая)
    "fut": "futr",      # будущее время (украсим)
}

person = {
    "1p": "1per",   # первое лицо (украшаю)
    "2p": "2per",   # второе лицо (украшаешь)
    "3p": "3per"    # третье лицо (украшает)
}

other = {
    "persn": "Name",    # личное имя (Иван, Дарья, Леопольд, Эстер, Гомер, Маугли)
    "patrn": "Patr",    # отчество (Иванович, Павловна)
    "famn": "Surn",     # фамилия (Николаев, Волконская, Гумбольдт)
    "zoon": "Name",     # кличка животного (Шарик, Дочка)
    "0": "Fixd",        # несклоняемое (шоссе, Седых)
    "abbr": "Abbr"
}

special = {
    "abbr": "Abbr"      # («Сокращение»)  — сокращенная запись (тов., гг., ч.). В поле «Лексема» сокращение (кроме
                        # инициалов)
                        # раскрывается, указывается грамматическая форма, соответствующая контексту. Специально отметим,
                        # что акронимы вроде ООН, вуз и усеченные слова вроде зав, зам, записываемые без точки и не
                        # раскрываемые при чтении, не получают пометы abbr и трактуются как обычные слова
                        # (склоняемые или несклоняемые).
}
