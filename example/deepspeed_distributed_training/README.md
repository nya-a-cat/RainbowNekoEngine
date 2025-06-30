# DeepSpeed 分布式训练示例

本示例展示如何利用 RainbowNeko Engine 集成 DeepSpeed 进行大规模模型的分布式训练，以减少显存占用和加速训练。

## 1. 准备

确保您的环境中已安装 DeepSpeed：

```bash
pip install deepspeed
```

## 2. 配置 DeepSpeed

本示例使用 `train_deepspeed_config.py` 配置文件。该文件将继承 `../train_base.py` 并添加 DeepSpeed 相关的配置。

## 3. 运行训练

使用 `neko_train_ds` 命令启动 DeepSpeed 训练：

```bash
neko_train_ds --cfg train_deepspeed_config.py
```

您也可以使用 `deepspeed` 命令直接启动：

```bash
deepspeed --num_gpus=2 main_deepspeed.py --cfg train_deepspeed_config.py
```

其中 `--num_gpus` 指定使用的 GPU 数量。

## 4. 训练过程监控

训练过程中的日志和模型检查点将保存在配置文件中指定的输出路径。您可以通过 TensorBoard 或 WandB 进行监控（如果已在 `train_deepspeed_config.py` 中启用）。