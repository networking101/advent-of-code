aoc: aoc.asm
	yasm -g dwarf2 -f elf64 aoc.asm -l aoc.lst
	yasm -g dwarf2 -f elf64 solve1.asm -l solve1.lst
	yasm -g dwarf2 -f elf64 solve2.asm -l solve2.lst
	ld -dynamic-linker /lib64/ld-linux-x86-64.so.2 -g -o aoc aoc.o solve1.o solve2.o -lc
clean:
	rm -f aoc aoc.lst aoc.o solve1.lst solve1.o solve2.lst solve2.o
