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


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
