#include <stdio.h>
#include <cwchar>

int main()
{
    int i;
    wchar_t chinese[] = L"我不是中国人。";
    for(i = 0; chinese[i]; ++i)
    {
        if(chinese[i] == L'不')
        	//printf("%lc\n", chinese[i]);
            printf("found\n");
        if(chinese[i] == L'\u4E0D')
        	printf("%lc\n", chinese[i]);
            printf("also found\n");
    }
    return 0;
}