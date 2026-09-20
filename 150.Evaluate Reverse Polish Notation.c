#include <stdlib.h>

int evalRPN(char** tokens, int tokensSize)
{
    int* stack = (int*)malloc(tokensSize * sizeof(int));
    int top = -1;
    
    for (int i = 0; i < tokensSize; i++)
    {
        char* s = tokens[i];
        
        if ((s[0] == '+' || s[0] == '-' || s[0] == '*' || s[0] == '/') && s[1] == '\0')
        {
            int op2 = stack[top--];
            int op1 = stack[top--];
            
            if (s[0] == '+') stack[++top] = op1 + op2;
            else if (s[0] == '-') stack[++top] = op1 - op2;
            else if (s[0] == '*') stack[++top] = op1 * op2;
            else if (s[0] == '/') stack[++top] = op1 / op2;
        }
        else
        {
            stack[++top] = atoi(s);
        }
    }
    
    int result = stack[top];
    free(stack);
    return result;
}