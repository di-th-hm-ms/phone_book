import sqlite3
import sys

# お世話になっております。
# 1 の検索クエリだけうまく動きませんでした。原因を教えていただきたいです。
# 初のsqliteでしたが、便利ですね。切り分けができていませんが、ご理解よろしくお願い申し上げます。

# dbに接続
db_name = ('phone_book.db')
conn = sqlite3.connect(db_name)  # DB ? connect : create DB

# cursor オブジェクトの初期化 行の操作目的(excelはマウス)
cursor = conn.cursor()

sql_create_table = """CREATE TABLE IF NOT EXISTS phone(name, phone_number)"""
sql_get_table_name = """SELECT name FROM sqlite_master WHERE TYPE='table'"""
sql_insert = """INSERT INTO phone VALUES(?, ?)"""  # ?は後で値を受け取る
sql_get_all_data = """SELECT * FROM phone"""
sql_get_feature_data = """SELECT * FROM phone WHERE name = ?"""
sql_delete_datum = 'DELETE FROM phone WHERE name = ?'


# 基本 cursorオブジェクトのexecuteでデータを扱う
# cursor.execute(sql_create)


def main():

    cursor.execute(sql_create_table)
    conn.commit()

    while True:
        print('番号を入力してください。\n\
            1: 電話番号を検索\n\
            2: 電話番号を登録\n\
            3: 電話番号を削除\n\
            4: 電話番号を一覧\n\
            0: プログラムの終了\n->')

        try:
            n = int(input())
        except:
            print('適切な数字を入力してください。:')
            continue
        if n == 0:
            quit()
        # Query
        # 1 の検索クエリだけうまく動きませんでした。原因を教えていただきたいです。
        elif n == 1:
            name = input()
            try:
                cursor.execute(sql_get_feature_data)
                print(cursor.fetchone())

            except:
                print('指定された名前は見つかりませんでした。')

        elif n == 2:
            print('名前を入力してEnterを押してください:')
            name = input()
            number = None
            print('電話番号を入力してEnterを押してください:')
            # 番号判定
            while True:
                try:
                    number = int(input())
                    break
                except:
                    print('不正な値です。もう一度入力してください。(_cancel入力で最初から):')
                    continue
            # print(number)
            data = (name, number)
            cursor.execute(sql_insert, data)
            conn.commit()
        elif n == 3:
            print('削除する名前を入力してください:')
            name = None
            # if name == '_cancel':
            #     continue
            while name != '_cancel':
                try:
                    name = input()
                    cursor.execute(sql_delete_datum, (name,))
                except:
                    print('存在しない名前です。再度入力してください。(_cancel入力で最初から)')
                    continue
                else:
                    break
            conn.commit()
        elif n == 4:
            cursor.execute(sql_get_all_data)  # 取ってくるけど格納する必要はない。
            for d in cursor.fetchall():
                print(f'名前: {d[0]}  電話番号: {d[1]}')
        else:
            print('適切な数字を入力してください。:')
            continue


if __name__ == "__main__":
    main()
