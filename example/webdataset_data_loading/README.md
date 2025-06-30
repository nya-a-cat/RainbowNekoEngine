# WebDataset 数据加载示例

本示例展示如何使用 RainbowNeko Engine 结合 WebDataset 进行高效的数据加载和训练。WebDataset 是一种用于大规模数据集的 I/O 格式，它将多个数据样本（例如图像和标签）打包成单个 `.tar` 文件，从而减少文件系统开销并提高数据吞吐量。

## 1. 准备 WebDataset 文件

首先，您需要创建一个 WebDataset 文件。运行 `create_webdataset.py` 脚本来生成一个模拟的 WebDataset 文件。

```bash
python create_webdataset.py
```

该脚本将在当前目录下创建一个 `data.tar` 文件。

## 2. 训练配置 (`webdataset_train_config.py`)

`webdataset_train_config.py` 文件将配置 RainbowNeko Engine 使用 WebDataset 作为数据源。

## 3. 运行训练

使用 `neko_train` 命令启动训练：

```bash
neko_train --cfg webdataset_train_config.py
```

## 4. 预期结果

训练过程将从 `data.tar` 文件中加载数据。您将体验到 WebDataset 在数据加载方面的效率。