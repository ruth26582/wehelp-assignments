import urllib.request as req
import json

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    data = json.load(response)
tlist = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for list in tlist:
        # 景點名稱,區域,經度,緯度,第一張圖檔網址
        file.write(
            list["stitle"]
            + ","
            + list["address"][5:8]
            + ","
            + list["longitude"]
            + ","
            + list["latitude"]
            + ","
            + "https"
            + (list["file"].split("https")[1])
            + "\n"
        )
