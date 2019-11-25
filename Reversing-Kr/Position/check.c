signed int __stdcall sub_401740(int a1)
{
  int v1; // edi
  int v3; // esi
  int v4; // esi
  __int16 v5; // bx
  unsigned __int8 v6; // al
  unsigned __int8 name_first_1bit; // ST2C_1
  unsigned __int8 v8; // al
  unsigned __int8 name_second_3bit; // bl
  wchar_t *v10; // eax
  __int16 v11; // di
  wchar_t *v12; // eax
  __int16 v13; // di
  wchar_t *v14; // eax
  __int16 v15; // di
  wchar_t *v16; // eax
  __int16 v17; // di
  wchar_t *v18; // eax
  __int16 v19; // di
  unsigned __int8 v20; // al
  unsigned __int8 name_third_1bit; // ST2C_1
  unsigned __int8 v22; // al
  unsigned __int8 name_fourth_3bit; // bl
  wchar_t *v24; // eax
  __int16 v25; // di
  wchar_t *v26; // eax
  __int16 v27; // di
  wchar_t *v28; // eax
  __int16 v29; // di
  wchar_t *v30; // eax
  __int16 v31; // di
  wchar_t *v32; // eax
  __int16 v33; // si
  unsigned __int8 name_second_1bit; // [esp+10h] [ebp-28h]
  unsigned __int8 name_fourth_1bit; // [esp+10h] [ebp-28h]
  unsigned __int8 name_second_2bit; // [esp+11h] [ebp-27h]
  unsigned __int8 name_fourth_2bit; // [esp+11h] [ebp-27h]
  unsigned __int8 name_second_4bit; // [esp+13h] [ebp-25h]
  unsigned __int8 name_fourth_4bit; // [esp+13h] [ebp-25h]
  unsigned __int8 name_second_5bit; // [esp+14h] [ebp-24h]
  unsigned __int8 name_fourth_5bit; // [esp+14h] [ebp-24h]
  unsigned __int8 name_first_2bit; // [esp+19h] [ebp-1Fh]
  unsigned __int8 name_third_2bit; // [esp+19h] [ebp-1Fh]
  unsigned __int8 name_first_3bit; // [esp+1Ah] [ebp-1Eh]
  unsigned __int8 name_third_3bit; // [esp+1Ah] [ebp-1Eh]
  unsigned __int8 name_first_4bit; // [esp+1Bh] [ebp-1Dh]
  unsigned __int8 name_third_4bit; // [esp+1Bh] [ebp-1Dh]
  unsigned __int8 name_first_5bit; // [esp+1Ch] [ebp-1Ch]
  unsigned __int8 name_third_5bit; // [esp+1Ch] [ebp-1Ch]
  int name; // [esp+20h] [ebp-18h]
  int serial; // [esp+24h] [ebp-14h]
  char v52; // [esp+28h] [ebp-10h]
  int v53; // [esp+34h] [ebp-4h]

  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&name);
  v1 = 0;
  v53 = 0;
  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&serial);
  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&v52);
  LOBYTE(v53) = 2;
  CWnd::GetWindowTextW(a1 + 304, &name);
  if ( *(_DWORD *)(name - 12) == 4 )
  {
    v3 = 0;
    while ( (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, v3) >= 0x61u
         && (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, v3) <= 0x7Au )
    {
      if ( ++v3 >= 4 )
      {
LABEL_7:
        v4 = 0;
        while ( 1 )
        {
          if ( v1 != v4 )
          {
            v5 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, v4);
            if ( (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, v1) == v5 )
              goto LABEL_2;
          }
          if ( ++v4 >= 4 )
          {
            if ( ++v1 < 4 )
              goto LABEL_7;
            CWnd::GetWindowTextW(a1 + 420, &serial);
            if ( *(_DWORD *)(serial - 12) == 11
              && (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 5) == 0x2D )
            {
              v6 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, 0);
              name_first_1bit = (v6 & 1) + 5;
              name_first_5bit = ((v6 >> 4) & 1) + 5;
              name_first_2bit = ((v6 >> 1) & 1) + 5;
              name_first_3bit = ((v6 >> 2) & 1) + 5;
              name_first_4bit = ((v6 >> 3) & 1) + 5;
              v8 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, 1);
              name_second_1bit = (v8 & 1) + 1;
              name_second_5bit = ((v8 >> 4) & 1) + 1;
              name_second_2bit = ((v8 >> 1) & 1) + 1;
              name_second_3bit = ((v8 >> 2) & 1) + 1;
              name_second_4bit = ((v8 >> 3) & 1) + 1;
              v10 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
              itow_s(name_first_1bit + name_second_3bit, v10, 0xAu, 10);
              v11 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0);
              if ( (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 0) == v11 )
              {
                ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                v12 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                itow_s(name_first_4bit + name_second_4bit, v12, 0xAu, 10);
                v13 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 1);
                if ( v13 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                {
                  ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                  v14 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                  itow_s(name_first_2bit + name_second_5bit, v14, 0xAu, 10);
                  v15 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 2);
                  if ( v15 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                  {
                    ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                    v16 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                    itow_s(name_first_3bit + name_second_1bit, v16, 0xAu, 10);
                    v17 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 3);
                    if ( v17 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                    {
                      ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                      v18 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                      itow_s(name_first_5bit + name_second_2bit, v18, 0xAu, 10);
                      v19 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 4);
                      if ( v19 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                      {
                        ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                        v20 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, 2);
                        name_third_1bit = (v20 & 1) + 5;
                        name_third_5bit = ((v20 >> 4) & 1) + 5;
                        name_third_2bit = ((v20 >> 1) & 1) + 5;
                        name_third_3bit = ((v20 >> 2) & 1) + 5;
                        name_third_4bit = ((v20 >> 3) & 1) + 5;
                        v22 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&name, 3);
                        name_fourth_1bit = (v22 & 1) + 1;
                        name_fourth_5bit = ((v22 >> 4) & 1) + 1;
                        name_fourth_2bit = ((v22 >> 1) & 1) + 1;
                        name_fourth_3bit = ((v22 >> 2) & 1) + 1;
                        name_fourth_4bit = ((v22 >> 3) & 1) + 1;
                        v24 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                        itow_s(name_third_1bit + name_fourth_3bit, v24, 0xAu, 10);
                        v25 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 6);
                        if ( v25 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                        {
                          ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                          v26 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                          itow_s(name_third_4bit + name_fourth_4bit, v26, 0xAu, 10);
                          v27 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 7);
                          if ( v27 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                          {
                            ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                            v28 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                            itow_s(name_third_2bit + name_fourth_5bit, v28, 0xAu, 10);
                            v29 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 8);
                            if ( v29 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                            {
                              ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                              v30 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                              itow_s(name_third_3bit + name_fourth_1bit, v30, 0xAu, 10);
                              v31 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 9);
                              if ( v31 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                              {
                                ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                                v32 = (wchar_t *)ATL::CSimpleStringT<wchar_t,1>::GetBuffer(&v52);
                                itow_s(name_third_5bit + name_fourth_2bit, v32, 0xAu, 10);
                                v33 = ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 10);
                                if ( v33 == (unsigned __int16)ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )
                                {
                                  ATL::CSimpleStringT<wchar_t,1>::ReleaseBuffer(&v52, -1);
                                  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::~CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&v52);
                                  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::~CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&serial);
                                  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::~CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&name);
                                  return 1;
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
            goto LABEL_2;
          }
        }
      }
    }
  }
LABEL_2:
  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::~CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&v52);
  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::~CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&serial);
  ATL::CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>::~CStringT<wchar_t,StrTraitMFC_DLL<wchar_t,ATL::ChTraitsCRT<wchar_t>>>(&name);
  return 0;
}