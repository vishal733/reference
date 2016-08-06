#include <iostream>
#include <cstdio>

int main()
{
    int num, fifo;
    if ((fifo = open("/tmp/fifo", O_WRONLY)) < 0) {
       printf("%s\n", strerror(errno));
       return;
    }
    
    while (true)
    {
        if ((num= write(fifo, phrase, strlen(phrase)+1)) < 0) {
            printf("ERROR: %s\n", strerror(errno));
        }
    }

    close (fifo)
    return 0;
}
