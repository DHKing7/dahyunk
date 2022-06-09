#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <limits.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>



int main(int argc, char *argv[])
{
	int fd, n;
	char req[PIPE_BUF];
        char str3[] = "quit";
	

	if (mkfifo("./tmp", 0600) < 0) {
		perror(argv[0]);
		exit(1);
	}
	fd = open("./tmp", O_RDONLY);
	if (fd < 0) {
		perror(argv[0]);
		exit(1);
	}

	while (1) {
		n = read(fd, req, PIPE_BUF);
		if (n > 0) {
			if (strcmp(req,str3)==0){
				exit(0);
			}
			else
			        write(STDOUT_FILENO, req, n);
			        printf("\n");
			
		}
	}

	return 0;
}

