from omegaconf import OmegaConf
from rainbowneko.utils.cfg_tool import merge_cfg

# 定义基础配置
_base_ = ["../train_base.py"]

# 数据集配置 (与 image_classification 示例类似，为了简化，这里直接使用模拟数据)
data = dict(
    train=dict(
        _target_="torchvision.datasets.ImageFolder",
        root="../image_classification/data/train",
        transform=dict(
            _target_="torchvision.transforms.Compose",
            transforms=[
                dict(_target_="torchvision.transforms.Resize", size=(64, 64)),
                dict(_target_="torchvision.transforms.ToTensor"),
                dict(_target_="torchvision.transforms.Normalize", mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ],
        ),
    ),
    dataloader=dict(
        batch_size=32,
        num_workers=4,
        shuffle=True,
        drop_last=True,
    ),
)

# 模型配置 (使用一个更简单的模型进行演示)
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
    T_max=10,
    eta_min=1e-6,
)

# 训练器配置 (覆盖 train_base 中的部分参数)
trainer = dict(
    max_epochs=5, # DeepSpeed 训练可能更快，减少 epoch 数量
    log_every_n_steps=50,
    val_every_n_epochs=1,
)

# DeepSpeed 配置
deepspeed = dict(
    zero_optimization=dict(
        stage=2, # Zero Stage 2
    ),
    gradient_accumulation_steps=1,
    gradient_clipping=1.0,
    fp16=dict(
        enabled=True,
        initial_scale_power=16,
    ),
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
cfg = merge_cfg(cfg, OmegaConf.create(data=data, model=model, optimizer=optimizer, scheduler=scheduler, trainer=trainer, deepspeed=deepspeed, loss=loss, evaluator=evaluator))