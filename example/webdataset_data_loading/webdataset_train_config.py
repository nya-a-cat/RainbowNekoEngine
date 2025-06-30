from omegaconf import OmegaConf
from rainbowneko.utils.cfg_tool import merge_cfg

# 定义基础配置
_base_ = ["../train_base.py"]

# 数据集配置
data = dict(
    train=dict(
        _target_="rainbowneko.data.source.webds.WebDataSource",
        urls=["./data.tar"], # WebDataset 文件路径
        handler=dict(
            _target_="rainbowneko.data.handler.image.ImageHandler",
            image_key="png",
            label_key="cls",
            transform=dict(
                _target_="torchvision.transforms.Compose",
                transforms=[
                    dict(_target_="torchvision.transforms.Resize", size=(64, 64)),
                    dict(_target_="torchvision.transforms.ToTensor"),
                    dict(_target_="torchvision.transforms.Normalize", mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ],
            ),
        ),
    ),
    dataloader=dict(
        batch_size=32,
        num_workers=4,
        shuffle=True,
        drop_last=True,
    ),
)

# 模型配置 (使用 ResNet18)
model = dict(
    _target_="torchvision.models.resnet18",
    pretrained=False,
    num_classes=3,  # 模拟数据集有3个类别
)

# 优化器配置
optimizer = dict(
    _target_="torch.optim.AdamW",
    lr=1e-3,
    weight_decay=1e-2,
)

# 学习率调度器配置
scheduler = dict(
    _target_="torch.optim.lr_scheduler.CosineAnnealingLR",
    T_max=5,
    eta_min=1e-6,
)

# 训练器配置
trainer = dict(
    max_epochs=5,
    log_every_n_steps=10,
    val_every_n_epochs=1,
)

# 损失函数配置
loss = dict(
    _target_="torch.nn.CrossEntropyLoss",
)

# 评估器配置
evaluator = dict(
    metrics=[
        dict(_target_="torchmetrics.Accuracy", task="multiclass", num_classes=3),
    ],
)

# 合并基础配置和当前配置
cfg = OmegaConf.create()
cfg = merge_cfg(cfg, _base_)
cfg = merge_cfg(cfg, OmegaConf.create(data=data, model=model, optimizer=optimizer, scheduler=scheduler, trainer=trainer, loss=loss, evaluator=evaluator))