# 图像分类基础训练与推理示例

本示例展示如何使用 RainbowNeko Engine 进行标准的图像分类任务，包括数据准备、模型训练和模型推理。

## 1. 数据准备

本示例使用一个模拟数据集。您可以通过运行 `data_prep.py` 脚本来生成数据。

```bash
python data_prep.py
```

该脚本将在当前目录下创建一个 `data` 文件夹，其中包含训练和验证所需的图像文件。

## 2. 模型训练

使用 `train_config.py` 配置文件进行模型训练。

```bash
neko_train --cfg train_config.py
```

训练过程中的日志和模型检查点将保存在默认的输出路径。

## 3. 模型推理

使用 `infer_config.py` 配置文件进行模型推理。

```bash
neko_run --cfg infer_config.py
```

推理结果将输出到控制台或指定的文件。