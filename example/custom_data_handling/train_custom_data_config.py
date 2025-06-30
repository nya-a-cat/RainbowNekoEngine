from omegaconf import OmegaConf
from rainbowneko.utils.cfg_tool import merge_cfg

# 定义基础配置
_base_ = ["../train_base.py"]

# 数据集配置
data = dict(
    train=dict(
        _target_="custom_dataset.MyCustomSource", # 使用自定义数据源
        data_file_path="./custom_data/dummy_data.txt",
        transform=None, # 自定义数据源中处理数据，这里可以不加 transform
    ),
    val=dict(
        _target_="custom_dataset.MyCustomSource", # 使用自定义数据源
        data_file_path="./custom_data/dummy_data.txt",
        transform=None,
    ),
    dataloader=dict(
        batch_size=16, # 调整 batch_size 适应小数据集
        num_workers=0, # 简单示例，不需要多进程加载
        shuffle=True,
        drop_last=True,
    ),
)

# 模型配置 (使用一个简单的全连接网络来处理数值特征)
model = dict(
    _target_="torch.nn.Sequential",
    _args_=[
        dict(_target_="torch.nn.Linear", in_features=2, out_features=16),
        dict(_target_="torch.nn.ReLU"),
        dict(_target_="torch.nn.Linear", in_features=16, out_features=2), # 2个类别
    ],
)

# 优化器配置
optimizer = dict(
    _target_="torch.optim.AdamW",
    lr=1e-3,
)

# 损失函数配置
loss = dict(
    _target_="torch.nn.CrossEntropyLoss",
)

# 训练器配置
trainer = dict(
    max_epochs=5, # 减少 epoch 数量
    log_every_n_steps=1,
    val_every_n_epochs=1,
)

# 评估器配置
evaluator = dict(
    metrics=[
        dict(_target_="torchmetrics.Accuracy", task="multiclass", num_classes=2), # 2个类别
    ],
)

# 合并基础配置和当前配置
cfg = OmegaConf.create()
cfg = merge_cfg(cfg, _base_)
cfg = merge_cfg(cfg, OmegaConf.create(data=data, model=model, optimizer=optimizer, loss=loss, trainer=trainer, evaluator=evaluator))