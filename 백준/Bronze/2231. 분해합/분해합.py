num = int(input()) #216
for i in range(0, num + 1): #198 -> '198' i[0] = 1, i[1] = 9, i[2] = 8
    _sum = 0  #[1, 9, 8] 자리에 있는 수를 한자리수로 취급! -> 수를 "분해"
    for j in list(str(i)): #str(i) -> '198' list(str(i)) -> ['1', '9', '8']
        _sum += int(j)
    _sum += int(i)
    if _sum == num:
        print(i)
        break

    if i == num:
        print(0)