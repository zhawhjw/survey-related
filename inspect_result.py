import math

import pandas as pd


d = {}

if __name__ == "__main__":

    result = pd.read_csv("result.csv")

    choices = result['Answer.userchoice'].values

    choices = [int(c) for c in choices if not math.isnan(c)]

    for c in choices:
        if c not in d:
            d[c] = 0

        d[c] += 1

    for n in d:
        print(n)
        print(d[n]/2000)
    # print(d)