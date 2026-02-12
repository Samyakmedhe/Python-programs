#include<stdio.h>
#include<string.h>

void Reverse(char str[])
{
    int i =0, j = strlen(str)-1;
    char temp ;

    while(i < j)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
        i++;
        j--;
    }

}
int main()
{

    char str [100];
    printf("Enter String : ");
    scanf("%s", str);

    Reverse(str);
    printf("Reverse String is : %s \n", str);

    return 0;
}