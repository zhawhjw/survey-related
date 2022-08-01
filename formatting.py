import os


if __name__ == "__main__":

    for root, dirs, files in os.walk("./", topdown=True):

        for f in files:

            if f.endswith(".py"):
                continue

            if f.endswith(".meta"):
                os.remove(root + "/" + f)