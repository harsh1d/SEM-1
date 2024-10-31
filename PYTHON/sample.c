#include<stdio.h>
void main()
{
    int sal;
    float tax;
    if (sal == 10000)
    {
        printf("NO TAX");
    }
    else if (sal > 10000 && sal < 20000)
    {
        tax = (0.10 * sal);
        printf("tax : %f ",tax);
    }
    else if (sal > 20000 && sal < 30000)
    {
        tax = (0.20 * sal);
        printf("tax : %f ",tax);
    }
    else
    {
        tax = (0.25 * sal);
        printf("tax : %f ",tax);
    }
}