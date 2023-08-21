# def strcounter(s):
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym , 0) + 1
#     print(syms_counter) O(N) = N
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

# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym,counter)
# s = ("vkdvkxlxlvvvvc") O(N) = M * N  - M уникальные символы   N все символы
# strcounter(s)
# N * N - худший случай когда все символы уникальны


def function(x):
    if x == x[::-1]:
        return True
    else:
        return False
print(function("урок"))
