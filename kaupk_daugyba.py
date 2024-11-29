# užduotis kaupia daugyba
def kaupk_daugyba(*args):
    if len(args) == 0:
        return 0
    kaupiklis = args[0]
    for elem in args[1:]:
        kaupiklis *= elem
    return kaupiklis


res = kaupk_daugyba(1)  # 1
print(res)
res = kaupk_daugyba(2, 2)  # 4
print(res)
res = kaupk_daugyba(2, 2, 2)  # 8
print(res)
res = kaupk_daugyba(0, 2, 2)  # 0
print(res)

