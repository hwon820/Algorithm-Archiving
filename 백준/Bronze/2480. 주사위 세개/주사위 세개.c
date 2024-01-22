#include <stdio.h>

int main(void)
{
    int a, b, c, price;
    int max = 0;

    scanf("%d %d %d", &a, &b, &c);

    if (a == b && b == c)
    {
        price = 10000 + a * 1000;
    }
    else if (a == b && b != c)
    {
        price = 1000 + a * 100;
    }
    else if (b == c && c != a)
    {
        price = 1000 + b * 100;
    }
    else if (a == c && c != b)
    {
        price = 1000 + c * 100;
    }
    else
    {
        if (a > max)
            max = a;
        if (b > max)
            max = b;
        if (c > max)
            max = c;

        price = max * 100;
    }

    printf("%d", price);

    return 0;

}