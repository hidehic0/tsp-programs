import random
import math

random.seed(3014)


def distance(x1, y1, x2, y2) -> float:
    # ユークリッド距離
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# ファイルから入力を受け取る
N = 0

X, Y = [], []

with open("./in.txt", "r") as f:
    lines = f.read().split("\n")
    N = int(lines[0])

    for l in lines[1:]:
        x, y = list(map(int, l.split()))

        X.append(x)
        Y.append(y)


def getscore(array: list[int]) -> float:
    """
    スコアを計算
    """
    array = [0] + array + [0]
    result = 0

    for i in range(1, len(array)):
        result += distance(X[array[i - 1]], Y[array[i - 1]], X[array[i]], Y[array[i]])

    return result


l = [i for i in range(1, N)]
current_score = getscore(l)

iter = 30000

scorelist = [current_score]
m = 10**10
for i in range(iter):
    tmp = l.copy()
    start = random.randint(0, N - 2)
    end = random.randint(start, N)

    tmp[start:end] = reversed(tmp[start:end])
    new_score = getscore(tmp)

    if new_score < current_score:
        current_score = new_score
        l = tmp.copy()

        scorelist.append(current_score)
        m = min(m, current_score)
    else:
        # 鉄則本焼きなまし
        T = 30 - 28 * (i / iter)
        probability = math.exp(min((current_score - new_score) / T, 0))

        if random.random() < probability:
            current_score = new_score
            l = tmp.copy()
    # else:
    #     probability = math.exp((current_score - new_score) / temp)

    #     if random.random() < probability:
    #         current_score = new_score
    #         l = tmp.copy()

    #     scorelist.append(current_score)


with open("scoretrend.txt", "w") as f:
    f.write("\n".join([str(i) for i in scorelist]))

print(m)
