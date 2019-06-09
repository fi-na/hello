import random
import pysnooper


# @pysnooper.snoop()
def main():
    # ランダムのインポート
    str = input("あなたは何麺？：")
    try:
        deme = int(str)
    except ValueError as e:
        print("エラーが発生しました")
        print("死ねカス")
        exit()
    else:
        print(f'1d{deme}の結果→', random.randint(1, deme))


if __name__ == "__main__":
    main()
