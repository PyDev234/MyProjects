#include <stdio.h>
#include <windows.h>                                                                // For setting code page in Windows 
#include <time.h>                                                                   // for using nanosleep function
// #include <unistd.h>                                                                 // For setting code page in Unix or Linux

void print_block(int n)
{
    int i = 0;
    for(;i<n;i++) { printf("\u2588"); }
}

void print_blank(int n)
{
    int i = 0;
    for(;i<n;i++) { printf(" "); }
}

int main(void)
{
    int total_width = 50;                                                           // Total length of progress Bar, taking for generalization
    int cycle_len = total_width*2;                                                  // progress array len
    int progress[cycle_len], i = 0, j = 0;
    int fgcolor[7] = { 31, 32, 33, 34, 35, 36, 37 } , color = 0; 
    int n = 1;                                                                   // No. of Progress Bar   
    struct timespec remaining, request;
    remaining.tv_nsec = 200000000;                                              // 0.5 sec or 5*10^8 nanosec
    remaining.tv_sec = 0;                                                       // Increase or decrease delay for nanosleep function

    SetConsoleOutputCP(65001);                                                   // Set code page to utf-8 i.e change ascii encoding to utf-8

    // \U0001FB96 for checker board unicodde character just for fun
    printf("\U0001FB96 \U0001F600\n");

    // Making progress array for circular looping.
    for(;i<=total_width;i++) { progress[i] = i; }
    for(i=(total_width-1);i>0;i--) { progress[cycle_len-i] = i; }

    // For Debugging the progress array
    // for(i=0;i<cycle_len;i++) { printf("%d ",progress[i]); }

    printf("\033[?25l\033[0;%dm", fgcolor);                                     // Setting the TextColor

    // Printing the Top and Bottom of progress Bar
    for(j = -2;j<total_width; j++) {  printf("\u25AC"); }
    printf("\033[%dD\033[%dB", total_width + 2, n + 1);
    for(j = -2;j<total_width; j++) {  printf("\u25AC"); }
    printf("\033[%dD\033[%dA", total_width + 2, n);

    j = 0;
    while(1)
    {
        printf("\033[0;%dm\u258C", fgcolor[color]);
        print_block(progress[j]);
        print_blank(total_width - progress[j]);
        printf("\u2590\033[%dD", total_width + 2);
        j = (++j)%cycle_len;
        color = (++color)%7;
        nanosleep(&remaining, &request);                                    // comment this line for full speed 
    }
    return 0;
}