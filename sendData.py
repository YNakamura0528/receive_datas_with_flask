import json
import requests

def main():
    data = {"data1":30, "data2":50}
    jsonString = json.dumps(data)
    res = requests.post("http://localhost:5000",
                        data={"content":jsonString})
    print(res)
    print(res.text)

if __name__ == '__main__':
    main()
