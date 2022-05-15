
tiangan = ['jia','yi','bing','ding','wu','ji','geng','xin','ren','gui']
dizhi = ['zi','chou','yin','mao','chen','si','wu','wei','shen','you','xu','hai']


year = int(input())

delta = year - 2020
a = 6
b = 0
if abs(delta)%60 == 0:
    print(tiangan[a]+dizhi[b])
else:
    delta = delta%60
    a = (a+delta)% 10
    b = (b+delta) % 12
    print(tiangan[a]+dizhi[b])
        