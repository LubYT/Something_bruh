# def character_counter(s):
#     ops=0
#     for sym in set(s):
#         counter=0
#         for sub_sym in s:
#             ops+=1
#             if sym == sub_sym:
#                 counter+=1
#         print(f'количество "{sym}" = {counter}')
#     print(ops)
#
# character_counter('abssaksajaosfdskphgoiakrot')


def character_counter_v2(s):
    ops = 0
    syms_counter={}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
        ops += 1

    for sym, counter in syms_counter.items():
        print(f'количество "{sym}" = {counter}')
    print(f'{ops}')

character_counter_v2('abcc')