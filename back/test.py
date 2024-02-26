# import jieba
# from collections import Counter

# result = jieba.lcut("<p>Record Something about: Bagging ..Bagging算法，全称为Bootstrap Aggregating，是一种集成学习算法，旨在提高单个预测模型，如决策树，的稳定性和准确性。这种方法通过以下步骤实现：</p><p><br></p><p>1. **自助采样（Bootstrap Sampling）**：从原始数据集中随机选择N个样本，采用放回抽样的方式，这意味着同一个样本可以被多次选择。这样的一个样本集称为一个bootstrap样本。</p><p><br></p><p>2. **构建基学习器**：使用每个bootstrap样本独立训练一个基学习器。在bagging算法中，基学习器通常是决策树，但也可以是任何其他算法。</p><p><br></p><p>3. **聚合**：将所有基学习器的预测结果进行聚合。对于分类问题，通常采用多数投票法；对于回归问题，则通常采用平均法。</p><p><br></p><p>Bagging的关键优势在于它可以减少模型的方差，从而提高模型的稳定性。通过结合多个模型的预测，它可以降低过拟合的风险，并在面对不同的数据子集时表现出更好的泛化能力。Bagging是随机森林算法的基础，随机森林通过在构建决策树时引入更多的随机性来进一步提高模型的性能。.</p>")
# word_count = Counter(result)
# print(word_count)

import subprocess

# 构建命令字符串
# command = r'python E:/Vis24-TailorMind/sftmodel/LLaMA-Factory/src/cli_demo.py --model_name_or_path "E:/Vis24-TailorMind/sftmodel/Baichuan2-7B-Chat" --adapter_name_or_path "E:/Vis24-TailorMind/sftmodel/LLaMA-Factory/0204test" --template baichuan2 --finetuning_type lora'
command = 'git status'
# 使用subprocess.run执行命令
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 打印命令执行的输出和错误
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
