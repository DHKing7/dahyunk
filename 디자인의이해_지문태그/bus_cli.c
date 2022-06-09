#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

typedef struct Person {
	char name[20];
	int cash;
	char card[5];
	char finger_print[5];
} DataBase;

int main(int argc, char *argv[])
{
	int fd;
	int i;
        char str1[] = "Card_Tag";
	char str2[] = "Finger_Tag";

	DataBase db[] = {
		{"KDH", 3000, "001", "None"},
                {"CJH", 10000, "002", "002"},
		{"KTH", 10000, "003", "003"},
		{"YHY", 10000, "004", "004"},
		{"PSA", 10000, "005", "005"},
		{"JJM", 10000, "006", "006"}
	};

	DataBase *p = NULL;
        char message1[] = "하차처리 되었습니다.";
	char message2[] = "등록되지 않은 카드 입니다.";
	char message3[] = "등록되지 않은 지문 입니다.";
	int size = sizeof(db) /sizeof(db[0]);
	char check[5];

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
	                for(i=0; i<size; ++i){
				if (strcmp(argv[2], db[i].card)==0){
					p = &db[i];
					break;
				}
			}
			
			if(p == NULL)
				write(fd, message2, strlen(message2)+1);
			else
				write(fd, message1, strlen(message1)+1);
		        close(fd);
		}
	        else if (strcmp(argv[1],str2)==0){
			for(i=0; i<size; ++i){
				if(strcmp(argv[2], db[i].finger_print)==0){
					p = &db[i];
					break;
				}
			}

			if(p == NULL)
				write(fd, message3, strlen(message3)+1);
			else
				write(fd, message1, strlen(message1)+1);
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
