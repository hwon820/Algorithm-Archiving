#include <stdio.h>

int main(void)
{
    int x, y, qq;

    scanf("%d\n%d", &x, &y);

    if (x > 0 && y > 0)
        qq = 1;
    else if (x > 0 && y < 0)
        qq = 4;
    else if (x < 0 && y > 0)
        qq = 2;
    else
        qq = 3;

    printf("%d", qq);

}