# BOJ 20006 S1 랭킹전 대기열

p, m = map(int, input().split())


def matching(level, name):
    for room in rooms:
        if len(room) < m:
            if room[0][1] - 10 <= level <= room[0][1] + 10:
                room.append((name, level))
                return

    rooms.append([(name, level)])


rooms = []
for _ in range(p):
    level, name = input().split()
    level = int(level)

    matching(level, name)


for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")

    room.sort(key=lambda x: x[0])
    for name, level in room:
        print(level, name)
