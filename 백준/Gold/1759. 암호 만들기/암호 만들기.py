# BOJ 1759 G5 암호 만들기

l, c = map(int, input().split())
letters = list(input().split(" "))

vowels = ['a', 'e', 'i', 'o', 'u']


def check_letter(letter_list):
    vowel, consonant = 0, 0
    for letter in letter_list:
        if letter in vowels:
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        return True
    return False


def make_password(alphabets):
    global results
    if sorted(alphabets) != alphabets:
        return

    if len(alphabets) == l:
        if check_letter(alphabets):
            password = ''.join(alphabets)
            if password not in results:
                results.append(password)
        return

    for j in range(c):
        if not visited[j]:
            visited[j] = 1
            make_password(alphabets + [letters[j]])
            visited[j] = 0


results = []
visited = [0] * c
for i in range(c):
    visited[i] = 1
    make_password([letters[i]])
    visited[i] = 0

print(*sorted(results), sep='\n')
