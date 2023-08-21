# def strcounter(s):
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym , 0) + 1
#     print(syms_counter)
# strcounter("gkbvckk")

# def strcounter(s):
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym,counter)
# s = ("bkvjcxvv")    N ** 2
# strcounter(s)

def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym,counter)
s = ("vkdvkxlxlvvvvc")
strcounter(s)