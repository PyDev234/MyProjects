#include <stdio.h>
#include <time.h>   // for nanosleep function
#include <wchar.h>
#include <locale.h>
// #include <unistd.h> // for sleep function
#include <windows.h>

// Left Half Block
wchar_t l = 0x258C;
// Right Half Block
wchar_t r = 0x2590;
// Geometric symbol similar to '-'
wchar_t t = 0x25AC;
// Full block character
wchar_t b = 0x2588;
// unsigned int b = 0x2588;
// wchar_t b = 9608;

// alt + 219 -> FUll Block character
// alt + 221 -> Left Half Block character
// alt + 222 -> Right Half Block character

// Prints the top or bottom bar of the box
void print_boxtb()
{
	int i;
    for(i = 1; i<53; i++) { printf("\u25AC"); }
}

// Prints the progress bar
void print_bar(int progress)
{
	int i;
    printf("\u258C",l);
    for(i=1;i<51;i++)
    {
        if(progress){ printf("\u2588"); progress--;}
        else{ printf(" "); }
    }
    printf("\u2590");
}

int main(int argc, char **argv)
{
    // struct timespec remaining, request;
    // request.tv_sec = 0;
    // request.tv_nsec = 5000000L;
    char buffer[8192];
    // char buffer[32768];
    int progress = 0, cycle[100], i=0;

	// SetConsoleOutputCP(20127);                                 // US-ASCII (7-bit)
	// SetConsoleOutputCP(850);                                 // OEM Multilingual Latin 1; Western European (DOS)
	SetConsoleOutputCP(65001);                               // UTF-8 Encoding
	// SetConsoleOutputCP(65000);                               // UTF-7 Encoding
	// SetConsoleOutputCP(12000);                               // UTF-32 Little Endian encoding
	// SetConsoleOutputCP(12001);                               // UTF-32 Big Endian encoding
    // SetConsoleOutputCP(1252);                                // ANSI Latin 1; Western European (Windows)
    // SetConsoleOutputCP(1200);                                // UTF-16 Little Endian encoding
	// SetConsoleOutputCP(1201);                                // UTF-16 Big Endian endcoding
    setvbuf(stdout, buffer, _IOFBF, sizeof(buffer));
    
    // Making an array for circular iterating similar to cycle from itertools in python
    for(;i<51;i++) { cycle[i] = i; }
    for(i=51;i<100;i++) { cycle[i] = 100-i; }
    // For debugging
    // for(i=0;i<100;i++) {  printf("%d ",cycle[i]); }
    // printf("\n");

    // setlocale(LC_CTYPE, "C.UTF-8");
    // setlocale(LC_CTYPE, "en_US.utf8");
    // setlocale(LC_CTYPE, "ACP");
    // setlocale(LC_CTYPE, "en-GB.utf8");
    // setlocale(LC_CTYPE, "en-us.utf8");
    // setlocale(LC_ALL, "C.UTF-8");

    printf("\033[?25l\033[0;36m");
    // printf("%u \u2593\n", GetConsoleOutputCP());
    // printf("%lc %lc\n",219, 221);
    print_boxtb();
    printf("\033[54D\033[8B");
    // for(int i = 0; i<3; i++) { printf("\n"); }
    print_boxtb();
    printf("\033[54D\033[7A");

    // Main Program Starts Here!
    i = 0;
    while(1)
    {
        print_bar(progress);
        printf("\033[54D\033[1B");

        print_bar(50-progress);
        printf("\033[54D\033[1B");

        print_bar(progress);
        printf("\033[54D\033[1B");

        print_bar(50-progress);
        printf("\033[54D\033[1B");

        print_bar(progress);
        printf("\033[54D\033[1B");

        print_bar(50-progress);
        printf("\033[54D\033[1B");

        print_bar(progress);
        printf("\033[54D\033[6A");
        // nanosleep(&request, &remaining);
        // For Debugging of Cycle 
        progress = cycle[i=((++i)%100)];
        // printf("%d",progress);
        // nanosleep(&request, &remaining);
        // printf("\033[10D");
        // fflush(stdout);
    }
    printf("\033[?25h\033[0;0m\033[8B");
    return 0;
}
