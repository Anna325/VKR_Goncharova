CC = g++
CFLAGS = -Wall

all: obj/main.o obj/LexicalAnalyzer.o obj/MorphAnalyzer.o
	$(CC) obj/main.o obj/LexicalAnalyzer.o obj/MorphAnalyzer.o -o bin/main

obj/main.o: src/main.cpp obj/LexicalAnalyzer.o obj/MorphAnalyzer.o
	$(CC) $(CFLAGS) -c src/main.cpp -o obj/main.o

obj/MorphAnalyzer.o: include/MorphAnalyzer.cpp include/MorphAnalyzer.h obj/LexicalAnalyzer.o
	$(CC) $(CFLAGS) -c include/MorphAnalyzer.cpp -o obj/MorphAnalyzer.o

obj/LexicalAnalyzer.o: include/LexicalAnalyzer.cpp include/LexicalAnalyzer.h
	$(CC) $(CFLAGS) -c include/LexicalAnalyzer.cpp -o obj/LexicalAnalyzer.o

clean:
	rm -rf obj/*.o main