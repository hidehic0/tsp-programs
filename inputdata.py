import random

# ネットで見たいいシード
random.seed(3014)

result = "150"
# [0]*150なのは競プロのクセ
for _ in [0] * 150:
    # -10^5から10^5に固定
    x = random.randint(-100000, 100000)
    y = random.randint(-100000, 100000)

    result += f"\n{x} {y}"

with open("./in.txt", "w") as f:
    f.write(result)
