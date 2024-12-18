import matplotlib.pyplot as plt

x = ['LSTM without embeddings', 'MLP Layers', 'Social LSTM', 'Transformer', "GPT-Prompt"] 
y = [0.66, 0.72, 0.72, 0.74, 0.55]  

x = ['Random Initialization', 'One-hot Initialization', 'Pre-trained Initialization'] 
y = [0.60, 0.64, 0.67]  

x = ['Positive-only Loss', 'Negative-only Loss', 'Negative Loss with sigmoid'] 
y = [0.60, 0.64, 0.67]


# 绘制直方图
plt.figure(figsize=(8, 6))  # 设置画布大小
plt.bar(x, y, color='#4A90E2', alpha=0.8, edgecolor='black')  # 使用柔和的蓝色

# 添加标题和标签
plt.title('Performance on downstream tasks', fontsize=16)
plt.xlabel('Methods', fontsize=14)
plt.ylabel('AUROC metrics value', fontsize=14)

plt.ylim(0.5, max(y) + 0.1)

# 显示网格
plt.grid(axis='y', linestyle='--', alpha=0.6)

# 显示直方图
plt.show()