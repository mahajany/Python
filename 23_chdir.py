import os
def chfunction():
    dir_name=os.getcwd()
    print(dir_name)
    os.chdir("../bingo")
    print(os.getcwd())

if __name__ == '__main__':
    chfunction()
