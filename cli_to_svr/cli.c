#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>


int main(int argc, char *argv[])
{
	int fd;
	int i;
    char str1[] = "tolower";
	char str2[] = "toupper";
	fd = open("./tmp", O_RDWR);
	if (fd < 0) {
		perror(argv[0]);
		exit(1);
	}
        if (argc == 2) {
		write(fd, argv[1], strlen(argv[1]) + 1);
		close(fd);
	}
	if (argc == 3) {
		if (strcmp(argv[1],str1)==0){ 
	                for(i=0; i<strlen(argv[2]); i++)
		              if(argv[2][i] >= 'A' && argv[2][i] <= 'Z')
		                   argv[2][i] = argv[2][i] +32;
			write(fd, argv[2], strlen(argv[2])+1);
		        close(fd);
		}
	        else if (strcmp(argv[1],str2)==0){
			for(i=0; i<strlen(argv[2]); i++)
				if(argv[2][i] >= 'a' && argv[2][i] <= 'z')
					argv[2][i] = argv[2][i] -32;
			write(fd, argv[2], strlen(argv[2])+1);
			close(fd);
		}
		else{
			write(fd, argv[2], strlen(argv[2])+1);
		        close(fd);
		        printf("command is invailid, toupper or tolower is right command\n");
		}
			
	}
	return 0;

}
