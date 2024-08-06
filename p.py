import json
import pandas as pd

# 读取 JSON 文件
with open("parsed_config.json", "r") as json_file:
    config_data = json.load(json_file)

# 提取数据并转换为 DataFrame
data = []

def extract_data(planet, fluids):
    for fluid, properties in fluids.items():
        if isinstance(properties, dict):
            data.append({
                "Planet": planet,
                "Fluid": fluid,
                "Chance": properties.get("I:Chance", None),
                "DecreasePerOperationAmount": properties.get("I:DecreasePerOperationAmount", None),
                "MaxAmount": properties.get("I:MaxAmount", None),
                "MinAmount": properties.get("I:MinAmount", None),
                "Registry": properties.get("S:Registry", None)
            })
        else:
            print(f"Unexpected data format for fluid '{fluid}' on planet '{planet}': {properties}")

# 提取每个星球的数据
for planet, fluids in config_data.get("undergroundfluid", {}).items():
    extract_data(planet, fluids)

# 转换为 DataFrame
df = pd.DataFrame(data)

# 将 DataFrame 保存为 CSV 文件
df.to_csv("fluid_data.csv", index=False)

print("数据已保存到 fluid_data.csv")
