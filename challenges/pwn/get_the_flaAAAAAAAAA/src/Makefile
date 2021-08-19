all: clean
	gcc main.c -o program -fno-stack-protector -no-pie -D_FORTIFY_SOURCE=0

clean:
	@rm program