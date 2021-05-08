# インストールしたパッケージのインポート
from flask import Flask, render_template
import sqlite3

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

# どこのアドレスで実行するか指定
@app.route('/')
def hello_world():
    message = "Hello World"
    return message

# データベースの情報を member-list.html に表示
@app.route('/dbtest', methods=["GET"])
def debtest():
    # dbtest.dbに接続します
    conn = sqlite3.connect('9th.db')
    # DBの中身を操作できるようにします
    c = conn.cursor()
    # SQLを実行 テーブルとカラムを選択
    c.execute('SELECT name from profile')
    # SQLで取得したデータを変数に格納 fetch とって参る
    profile_info = c.fetchone()
    print(profile_info)
    # データベースとの接続を終了
    c.close()
    return render_template('member-list.html', tpl_name=profile_info[0])


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
