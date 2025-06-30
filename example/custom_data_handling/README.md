# 自定义数据处理示例

本示例展示如何使用 RainbowNeko Engine 自定义数据源或数据处理器。通过实现 `rainbowneko.data.source.base.BaseSource` 或 `rainbowneko.data.handler.base.BaseHandler`，您可以灵活地处理各种数据格式和预处理逻辑。

## 1. 自定义数据源 (`custom_dataset.py`)

`custom_dataset.py` 中定义了一个简单的自定义数据源 `MyCustomSource`，它模拟从一个文本文件加载数据并进行简单的处理。

## 2. 训练配置 (`train_custom_data_config.py`)

`train_custom_data_config.py` 配置文件将使用我们自定义的数据源。

## 3. 运行训练

运行 `main_custom_data.py` 脚本来启动训练：

```bash
python main_custom_data.py --cfg train_custom_data_config.py
```

## 4. 预期结果

训练过程将使用自定义数据源提供的数据。您可以通过修改 `custom_dataset.py` 来体验不同的数据处理逻辑。