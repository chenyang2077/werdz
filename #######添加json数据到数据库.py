import sqlite3  
import json  
  
# 数据库文件路径  
db_path = r'F:\MyApplication8\app\src\main\assets\WordTranslations11111 1030.db'  

  
# JSON 文件路径  
json_path = r'C:\Users\Administrator\Desktop\后端数据库\######所有ssssssouufs.json'  
  
# 连接到 SQLite 数据库  
conn = sqlite3.connect(db_path)  
cursor = conn.cursor()  
  
# 确保 Translations 表存在  
cursor.execute('''  
CREATE TABLE IF NOT EXISTS Translations (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    english_word TEXT NOT NULL UNIQUE,  
    chinese_translation TEXT NOT NULL  
)  
''')  

# 清空Translations表中的所有数据  
cursor = conn.cursor()  
cursor.execute("DELETE FROM Translations")  
  
# 读取 JSON 文件  
with open(json_path, 'r', encoding='utf-8') as file:  
    data = json.load(file)  
  
# 遍历数据并插入或更新数据库  
for english_word, chinese_translation in data.items():  
    cursor.execute("SELECT COUNT(*) FROM Translations WHERE english_word=?", (english_word,))  
    count = cursor.fetchone()[0]  
    if count > 0:  
        cursor.execute("UPDATE Translations SET chinese_translation=? WHERE english_word=?", (chinese_translation, english_word))  
    else:  
        cursor.execute("INSERT INTO Translations (english_word, chinese_translation) VALUES (?, ?)", (english_word, chinese_translation))  
  
# 提交事务  
conn.commit()  
  
# 关闭数据库连接  
conn.close()  
  
print("数据库数据已成功增加或覆盖。")