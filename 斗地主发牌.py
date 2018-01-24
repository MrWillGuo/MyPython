# 调用随机模块
import random

# 给定两个列表，一个存储牌的花色，一个存放牌数字和字母
flower = ['♠', '♥', '♣', '♦']
letter = ['3', '4', '5', '6',
          '7', '8', '9', '10',
          'J', 'Q', 'K', 'A', '2']
# 大小王没有花色，先直接存放在列表里
cards = ['小王', '大王']

for i in range(0, 13):
    index = random.randint(0, len(letter)-1)

    for temp in flower:
        cards.append(temp+letter[index])
    del letter[index]


# 从三个玩家中随机出一个成为地主,打印出地主玩家的牌
players = [[], [], []]
a = int(random.randint(0, 2))
print("玩家1 玩家2 玩家2")
print("玩家%d成为地主" % (a+1))
print('')

# 成为地主玩家的牌，共有20张
j = 0
while j < 54:
    if j < 20:
        index1 = random.randint(0, len(cards) - 1)
        players[a].append(cards[index1])
        cards.remove(cards[index1])
    else:
        break
    j += 1
# 打印出地主玩家的牌
print("地主的牌为：")
print("%s" % players[a])

# 从全部牌中去掉地主玩家的20张牌
del players[a]

# 其他两个玩家成为农民，分别有17张，共34张牌
k = 0
while k < 34:
    if k < 17:
        index2 = random.randint(0, len(cards)-1)
        players[0].append(cards[index2])
        cards.remove(cards[index2])

    else:
        index3 = random.randint(0, len(cards) - 1)
        players[1].append(cards[index3])
        cards.remove(cards[index3])
    k += 1

# 打印出农民玩家的牌
print("农民1的牌为：")
print(players[0])
print("农民2的牌为：")
print(players[1])
