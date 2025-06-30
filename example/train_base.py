# 这是一个基础训练配置文件，用于定义通用的训练参数和组件。
# 所有的训练示例都可以继承这个基础配置。

# 项目名称和输出目录
project_name = "image_classification_example"
output_dir = "./output"

# 训练器配置
trainer = dict(
    # 默认值，可以在具体配置中覆盖
    max_epochs=10,
    log_every_n_steps=10,
    val_every_n_epochs=1,
    save_every_n_epochs=1,
    save_total_limit=3,
    gradient_accumulation_steps=1,
    max_train_steps=None,
    amp=True, # 启用自动混合精度训练
    seed=42,
)

# 优化器配置 (占位符，具体示例中会定义)
optimizer = None

# 学习率调度器配置 (占位符，具体示例中会定义)
scheduler = None

# 数据加载器配置 (占位符，具体示例中会定义)
data = dict(
    dataloader=dict(
        batch_size=32,
        num_workers=4,
        shuffle=True,
        drop_last=True,
    ),
)

# 模型配置 (占位符，具体示例中会定义)
model = None

# 损失函数配置 (占位符，具体示例中会定义)
loss = None

# 评估器配置 (占位符，具体示例中会定义)
evaluator = None

# 日志器配置
loggers = [
    dict(_target_="rainbowneko.loggers.cli_logger.CliLogger"),
    dict(_target_="rainbowneko.loggers.tqdm_logger.TqdmLogger"),
    # dict(_target_="rainbowneko.loggers.tensorboard_logger.TensorboardLogger"),
    # dict(_target_="rainbowneko.loggers.wandb_logger.WandbLogger"),
]

# 检查点管理器配置
ckpt_manager = dict(
    # 默认值，可以在具体配置中覆盖
    save_best_model=True,
    monitor="val_loss", # 监控验证损失
    mode="min", # 监控模式：min 或 max
)

# 其他通用配置