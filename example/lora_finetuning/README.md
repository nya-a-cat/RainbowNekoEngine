# LoRA 微调示例

本示例展示如何使用 RainbowNeko Engine 对一个预训练模型进行 LoRA (Low-Rank Adaptation) 微调，以高效地适应新任务。LoRA 是一种参数高效的微调方法，它在原始模型旁边添加小的可训练矩阵，而不是微调所有模型参数。

## 1. 准备预训练模型

为了简化示例，我们将使用一个简单的 ResNet18 模型作为预训练模型。在实际应用中，您会加载一个在大型数据集上预训练的模型。

## 2. 配置 LoRA

`lora_train_config.py` 文件将定义 LoRA 相关的配置。这包括指定需要应用 LoRA 的模块、LoRA 的秩 (rank) 和 alpha 值。

## 3. 运行微调

使用 `neko_train` 命令启动 LoRA 微调：

```bash
neko_train --cfg lora_train_config.py
```

## 4. 预期结果

微调后的模型将保存在配置中指定的输出路径。您可以观察到模型在目标任务上的性能提升，同时训练参数量远小于全模型微调。