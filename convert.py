import urllib.parse
from datetime import datetime, timedelta, timezone

# 转换到北京时间
tz_beijing = timezone(timedelta(hours=8))
today = datetime.now(tz=tz_beijing).strftime("%Y·%m.%d").lstrip("0").replace(".0", ".")

# 读取模板文件
with open("nodes_template.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    if "#" in line:
        base, _ = line.split("#", 1)
    else:
        base = line
    remark = urllib.parse.quote(f"⏰更新：{today}")
    new_lines.append(f"{base}#{remark}")

# 输出新节点文件
with open("nodes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))
