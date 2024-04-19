# BOJ 16472 G4 고냥이

n = int(input())
string = input()
length = len(string)

end, answer = 0, 0
alphabet_dict = {}
for start in range(length):
    while end < length:
        if len(alphabet_dict.keys()) > n:
            break

        if string[end] not in alphabet_dict.keys():
            if len(alphabet_dict.keys()) == n:
                break
            else:
                alphabet_dict[string[end]] = 1
        else:
            alphabet_dict[string[end]] += 1
        end += 1
        answer = max(answer, end - start)

    alphabet_dict[string[start]] -= 1
    if not alphabet_dict[string[start]]:
        alphabet_dict.pop(string[start])

print(answer)
