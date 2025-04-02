import json

# 定义输入文件路径
input_file_path = r'C:\Users\Administrator\Desktop\后端数据库\所有音标过滤后的音标.json'
# 定义输出文件路径
output_file_path = r'C:\Users\Administrator\Desktop\后端数据库\######所有音标过滤后的音标oul.json'

try:
    # 打开输入文件并加载 JSON 数据
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 创建新字典存储符合条件的键值对
    filtered_data = {}

    # 遍历数据中的键值对
    for key, value in data.items():
        # 检查值中是否包含"oʊl"或"əʊl"
        if "oʊl" in value or "əʊl" in value:
            filtered_data[key] = value

    # 将筛选后的数据保存到输出文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(filtered_data, output_file, ensure_ascii=False, indent=4)

    print(f"处理完成，包含'oʊl'或'əʊl'的键值对已保存到 {output_file_path}")
    print(f"共找到 {len(filtered_data)} 个符合条件的键值对")

except FileNotFoundError:
    print(f"错误：指定的文件未找到，请检查文件路径。 文件路径: {input_file_path}")
except json.JSONDecodeError as json_error:
    print(f"错误：文件不是有效的 JSON 格式。 错误详情: {json_error}")
except Exception as e:
    print(f"发生未知错误：{e}")