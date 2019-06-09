import random


def main():
    # {個数 d 面数} で入力
    s = input("フレフレサイコロ：")

    # 変数宣言
    deme_list = s.split("d")
    kosu = int(deme_list[0])
    deme = int(deme_list[1])
    kekka = []
    sum = 0

    # がんばれ
    print(f"{kosu}d{deme}の結果")
    for i in range(kosu):
        kekka.append(random.randint(1, deme))
        sum += kekka[i]
    print(kekka)
    print("(", end="", sep="")
    for i in range(len(kekka) - 1):
        print(f"{kekka[i]}+", end="", sep="")
    print(f"{kekka[-1]})={sum}")


if __name__ == "__main__":
    main()

