import pandas as pd
import sys


def headers_gengerator(df):                      #headersの作成
    headers = df.columns
    with open("headers.txt", mode="w") as f:
        f.write("HEADERS = [\n")
        for s in headers:
            f.write('   "' + s + '",\n')
        f.write("].freeze\n")
    return headers


def columns_gengerator(df, headers):                     #カラムの作成
    columns = []

    for i in range(65, 65+26):                  #AA~ZZまでのリストを作成
        for ii in range(65, 65+26):             #数字をchr()でasciiコードから文字へ変換している
            if i == 65:
                columns.append(chr(ii))
            else:
                columns.append(chr(i)+chr(ii))

    colmuns = columns[0:len(df.columns)]        #CSVのヘッダーの数だけのカラムを取り出している
    numbers = list(df.loc[2])                   #サンプル用の値
    numbers2 = list(df.loc[3])                   #サンプル用の値

    with open("colmuns.txt", mode="w") as f:
        f.write("csv << [\n")
        for colmun, header, number, number2 in zip(columns, headers, numbers, numbers2):
            if number == None and number2 == None:
                f.write("nil,       ")
            elif number == 0 and number2 == 0:
                f.write('"0",       ')
            else:
                f.write(",        ")
            f.write("#列" + colmun + " " + header + "\n")
        f.write("]\n")

    return  colmuns



args = sys.argv #コマンドライン引数　ファイル名を入れる
df = pd.read_csv(args[1], encoding="utf-8")

headers = headers_gengerator(df)
columns_gengerator(df, headers)









