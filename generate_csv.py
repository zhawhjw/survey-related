import pandas as pd
import os

if __name__ == "__main__":

    dataframe = pd.DataFrame()

    for root, dirs, files in os.walk("SearchSurvey/", topdown=True):

        if not dirs:
            continue

        if 'combined' in dirs:
            continue

        dataframe['name'] = dirs

    dataframe.to_csv("./search_pairs.csv", index=False)
