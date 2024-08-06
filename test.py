import json

def parse_config(file_content):
    stack = []
    current_dict = {}
    root = current_dict

    for line in file_content:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        if line.endswith('{'):
            # Start a new dictionary level
            key = line[:-1].strip()
            new_dict = {}
            current_dict[key] = new_dict
            stack.append(current_dict)
            current_dict = new_dict
        elif line.endswith('}'):
            # End current dictionary level
            current_dict = stack.pop()
        else:
            # Handle key-value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                if value.isdigit():
                    value = int(value)
                current_dict[key] = value
    
    return root

# 读取文件内容并解析
with open("config.cfg", "r") as file:
    lines = file.readlines()

config_data = parse_config(lines)

# 将解析后的数据保存到 JSON 文件
with open("parsed_config.json", "w") as json_file:
    json.dump(config_data, json_file, indent=4)

print("配置数据已保存到 parsed_config.json")
