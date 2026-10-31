#include <stdbool.h>
#include <string.h>

bool isSubsequence(char *s, char *t)
{
    int s_len = strlen(s);
    int t_len = strlen(t);

    int i = 0;
    int j = 0;

    while (i < s_len && j < t_len)
    {
        if (s[i] == t[j])
            i++;
        j++;
    }
    return (i == s_len);
}