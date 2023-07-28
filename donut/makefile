OBJS	= main.o donut.o
ASM	= yasm -g dwarf2 -f elf64
CC	= g++ -g -std=c++11 

all: main

main.o: main.cpp
	$(CC) -c main.cpp

donut.o: donut.asm 
	$(ASM) donut.asm -l donut.lst

main: $(OBJS)
	$(CC) -no-pie -o main $(OBJS)

# -----
# clean by removing object files.

clean:
	rm  $(OBJS)
	rm  donut.lst
