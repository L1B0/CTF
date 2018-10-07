#include<iostream>
#include <cstdlib>
#include<cstring>
#include<cmath>
using namespace std;



int func0(int *a1, int a2, int a3)
{
  int temp; // ST0C_4

  temp = *(int *)(4 * a2 + a1);
  *(int *)(a1 + 4 * a2) = *(int *)(4 * a3 + a1);
  *(int *)(a1 + 4 * a3) = temp;
  return 1;
}
int func1(int *a1, int a2, int a3)
{
  return abs(*(int *)(4 * a2 + a1) + *(int *)(4 * a3 + a1))
       - abs(*(int *)(4 * a3 + a1))
       - abs(*(int *)(4 * a2 + a1))
       + 2;
}
// return v11
int func2(int *a1, int a2, int a3)
{
  return abs(*(int *)(4 * a3 + a1))
       - abs(*(int *)(4 * a3 + a1) + *(int *)(4 * a2 + a1))
       + abs(*(int *)(4 * a2 + a1))
       + 2;
}
int get_key(int a1, int a2)
{
  long  v2; // fst7
  int v4; // [esp+70h] [ebp+8h]

  v4 = ( long )(pow((double)a1, 0.9));
  v2 = (long int )(pow((double )a2, 9.800000000000001));
  return printf(
           "flag: %x%x%x%x%x%x%x%x\n",
           v4,
           v4 >> 16,
           (v2),
           (v2) >> 16,
           (v2) >> 16,
           (v2),
           v4 >> 16,
           v4);
}
int main()
{
  int result; // eax
  int i;
  int v4; // ebx
  int v5; // eax
  int v6; // ebx
  char v7_20[20]; // [esp+1Ch] [ebp-48h]
  signed int ( *func_ptr)(int*, int, int);
  int ( *v15)(int*, int, int); // [esp+4Ch] [ebp-18h]
  int ( *v16)(int*, int, int); 
  int v8; // [esp+30h] [ebp-34h]
  int v9; // [esp+34h] [ebp-30h]
  int v10; // [esp+38h] [ebp-2Ch]
  int v11; // [esp+3Ch] [ebp-28h]
  int v12; // [esp+40h] [ebp-24h]
  int v13; // [esp+44h] [ebp-20h]
  int v17; // [esp+54h] [ebp-10h]
  int v18; // [esp+58h] [ebp-Ch]
  FILE *file_ptr; // [esp+5Ch] [ebp-8h]

  func_ptr = func0;
  v15 = func1;
  v16 = func2;
  v8 = 0;
  v9 = 1;
  v10 = 2;
  v11 = 3;
  v12 = 3;
  v13 = 4;
  file_ptr = fopen("data", "rb");
  printf("%d\n",file_ptr);
  if ( !file_ptr )
    return -1;
  fseek(file_ptr, 0, 2);
  v18 = ftell(file_ptr);
  fseek(file_ptr, 0, 0);
  v17 = ftell(file_ptr);
  if ( v17 )
  {
    puts("something wrong");
    result = 0;
  }
  else
  {
    for ( i = 0; i < v18; ++i )
    {
      v4 = i;
      v7_20[v4] = fgetc(file_ptr);
    }
    v5 = strlen(v7_20);
    if ( v5 <= v18 )
    {
      v18 = v11;
      i = 0;
      v17 = v13;

      if(i==0)
      {
        get_key(v18, v17);
        system("PAUSE");
        result = 0;
      }
    }
    else
    {
      result = -1;
    }
  }
  return result;
}
