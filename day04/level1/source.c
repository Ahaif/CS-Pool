#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *pswd = "__stack_check";
    char *input = (char *)malloc(100); 

    if (input == NULL)
    {
        printf("Memory allocation failed.\n");
        exit(1);
    }

    printf("Please enter a key: ");
    scanf("%s", input);

    if (strcmp(pswd, input) == 0)
    {
        printf("Good job!\n");
        free(input); 
        exit(0);
    }
    else
    {
        printf("Nope\n");
        free(input); 
        exit(1);
    }
}
