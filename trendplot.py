import matplotlib.pyplot as plt

l = []
r = []
with open("./scoretrend.txt", "r") as f:
    lines = f.read().split("\n")

    for j, i in enumerate(lines):
        l.append(float(i))
        r.append(j + 1)

fig = plt.figure(figsize=(12, 8))
plt.plot(r, l)
plt.savefig("./trendplot.png")
