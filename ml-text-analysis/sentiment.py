from snownlp import SnowNLP

text = "这部电影真的太棒了！"
s = SnowNLP(text)
print(f"文本: {text}")
print(f"情感得分: {s.sentiments:.4f}")

texts = ["产品质量很差", "一般般", "超级喜欢！"]
print("\n批量结果:")
for t in texts:
    score = SnowNLP(t).sentiments
    sentiment = "正面" if score > 0.6 else "负面" if score < 0.4 else "中性"
    print(f"{sentiment} ({score:.2f}): {t}")