import json
import pandas as pd

from flask import Flask, request

app = Flask(__name__)
global cnt
cnt = 0
@app.route("/", methods = ["POST"])
def index():
    # contentとして受け取ったPOSTメッセージを文字列として受け取る
    global cnt

    try:
        content = request.form["content"]
        dict = json.loads(content)
        ser = pd.Series(dict)
        df = pd.DataFrame([ser], index = [0])
        # print(df)
        with open("data.csv", "a") as f:
            df.to_csv(f, header = (cnt == 0))
            cnt += 1
        return "succeed!"
    except:
        return "fail!"

if __name__ == '__main__':
    app.run(debug =True)
