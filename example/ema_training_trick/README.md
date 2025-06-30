# EMA (Exponential Moving Average) 训练技巧示例

本示例展示如何在 RainbowNeko Engine 中集成并使用 EMA (Exponential Moving Average) 训练技巧来提高模型性能。EMA 是一种在训练过程中维护模型参数的平滑版本的方法，通常可以带来更稳定的训练和更好的最终性能。

## 1. 配置 EMA

`ema_train_config.py` 文件将定义 EMA 相关的配置。在 RainbowNeko Engine 中，您可以通过在模型配置中添加 `ema` 字段来启用 EMA。

## 2. 运行训练

使用 `neko_train` 命令启动训练：

```bash
neko_train --cfg ema_train_config.py
```

## 3. 预期结果

训练过程中，EMA 模型会同步更新。在评估和推理时，通常会使用 EMA 模型的权重而不是原始训练模型的权重，以获得更好的泛化性能。