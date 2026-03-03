import pandas as pd
import json
import requests
import time

# ================= 配置区域 =================
API_KEY = "sk-17485ba4895740478d3de30abb7f17bb"
API_URL = "https://api.deepseek.com/chat/completions"
MODEL_NAME = "deepseek-chat"

EXCEL_FILE = "architecture_data.xlsx"

# 调试时改成 5，正式跑改成 None
TEST_LIMIT = None
# ===========================================


def ask_deepseek(prompt):
    """调用 DeepSeek，强制 UTF-8，安全解析"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "你是一位建筑史专家。请输出JSON格式，包含ai_tags(3个专业术语)和ai_insight(50字内分析)。"
            },
            {"role": "user", "content": prompt}
        ],
        "response_format": {"type": "json_object"}
    }

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {API_KEY.strip()}"
    }

    try:
        data_body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        response = requests.post(API_URL, headers=headers, data=data_body, timeout=60)

        if response.status_code != 200:
            print(f"❌ HTTP错误: {response.status_code}")
            print(response.text)
            return None

        response.encoding = "utf-8"
        res_json = response.json()

        if "choices" not in res_json:
            print("❌ API 返回异常：", res_json)
            return None

        content = res_json["choices"][0]["message"]["content"]

        try:
            return json.loads(content)
        except:
            print("⚠️ AI返回格式异常，已跳过")
            return None

    except Exception as e:
        print("⚠️ 请求失败:", e)
        return None


def process_data():
    print("🚀 DeepSeek 数据工厂启动...")

    try:
        df_basic = pd.read_excel(EXCEL_FILE, sheet_name="Sheet1")
        df_viz = pd.read_excel(EXCEL_FILE, sheet_name="Sheet3")

        for df in [df_basic, df_viz]:
            df.columns = (
                df.columns.astype(str)
                .str.replace("\ufeff", "")
                .str.strip()
            )

        merged = pd.merge(
            df_basic,
            df_viz,
            on="ID",
            how="left",
            suffixes=("", "_viz")
        )

        print("✅ Excel 读取成功")

    except Exception as e:
        print("❌ 读取 Excel 失败:", e)
        return

    run_df = merged.head(TEST_LIMIT) if TEST_LIMIT else merged

    building_list = []

    print(f"🧠 开始分析 {len(run_df)} 条建筑数据...\n")

    for _, row in run_df.iterrows():

        name = row.get("名称", "未知")
        print(f" -> 正在分析: {name}")

        prompt = f"""
名称：{row.get('名称')}
朝代：{row.get('朝代')}
类型：{row.get('类型')}
核心材质：{row.get('核心材质')}
简介：{row.get('简介文本')}
"""

        ai_res = ask_deepseek(prompt)

        if ai_res:
            tags = ai_res.get("ai_tags", ["传统工艺"])
            insight = ai_res.get("ai_insight", row.get("简介文本"))
        else:
            tags = ["传统工艺"]
            insight = row.get("简介文本")

        try:
            lng = float(row.get("经度"))
            lat = float(row.get("纬度"))
            tech = float(row.get("技术评分"))
            art = float(row.get("艺术评分"))
            integrity = float(row.get("完好度"))
        except:
            print("⚠️ 数值转换失败，跳过")
            continue

        building_list.append({
            "id": str(row.get("ID")),
            "name": row.get("名称"),
            "dynasty": row.get("朝代"),
            "type": row.get("类型"),
            "location": row.get("地点"),
            "coord": [lng, lat],
            "scores": {
                "tech": tech,
                "art": art,
                "integrity": integrity
            },
            "material": row.get("核心材质"),
            "ai_tags": tags,
            "ai_insight": insight,
            "desc": row.get("简介文本")
        })

        time.sleep(1.2)

    # 保存单体分析
    with open("ai_building_map.json", "w", encoding="utf-8") as f:
        json.dump(building_list, f, ensure_ascii=False, indent=4)

    print("✅ 单体建筑分析完成")

    # ==========================
    # 🔥 朝代级 AI 聚合分析（必须在函数内）
    # ==========================

    print("\n📊 开始生成朝代级 AI 总结...")

    dynasty_groups = merged.groupby("朝代")
    dynasty_stats = []

    for dynasty, group in dynasty_groups:

        count = len(group)
        avg_tech = round(group["技术评分"].mean(), 2)
        avg_art = round(group["艺术评分"].mean(), 2)
        avg_integrity = round(group["完好度"].mean(), 2)

        prompt = f"""
朝代：{dynasty}
建筑数量：{count}
平均技术评分：{avg_tech}
平均艺术评分：{avg_art}
平均完好度：{avg_integrity}

请总结该朝代建筑特征。
输出JSON格式：
ai_tags(3个风格关键词)
ai_insight(80字内学术总结)
"""

        ai_res = ask_deepseek(prompt)

        if ai_res:
            tags = ai_res.get("ai_tags", ["结构演变"])
            insight = ai_res.get("ai_insight", f"{dynasty}时期建筑风格鲜明。")
        else:
            tags = ["结构演变"]
            insight = f"{dynasty}时期建筑风格鲜明。"

        dynasty_stats.append({
            "dynasty": dynasty,
            "count": count,
            "avg_tech": avg_tech,
            "avg_art": avg_art,
            "avg_integrity": avg_integrity,
            "ai_tags": tags,
            "ai_insight": insight
        })

        time.sleep(1.2)

    with open("ai_dynasty_stats.json", "w", encoding="utf-8") as f:
        json.dump(dynasty_stats, f, ensure_ascii=False, indent=4)

    print("✅ 朝代级 AI 总结完成")
    print("\n🎉 所有任务完成！")


if __name__ == "__main__":
    process_data()
