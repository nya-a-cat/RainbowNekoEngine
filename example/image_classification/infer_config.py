from omegaconf import OmegaConf
from rainbowneko.utils.cfg_tool import merge_cfg

# 定义基础配置
_base_ = ["../infer_base.py"]

# 数据集配置
data = dict(
    infer=dict(
        _target_="torchvision.datasets.ImageFolder",
        root="./data/val", # 使用验证集进行推理
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
        shuffle=False,
    ),
)

# 模型配置
model = dict(
    _target_="torchvision.models.resnet18",
    pretrained=False,
    num_classes=3,  # 模拟数据集有3个类别
)

# 检查点加载配置
ckpt_path = "output/ckpt/dummy_model.pt" # 替换为实际训练得到的模型路径

# 推理器配置
infer = dict(
    workflow=[
        dict(
            _target_="rainbowneko.infer.workflow.data.InferDataLoader",
            data_cfg="${data.infer}",
            dataloader_cfg="${data.dataloader}",
        ),
        dict(
            _target_="rainbowneko.infer.workflow.model.InferModel",
            model_cfg="${model}",
            ckpt_path=ckpt_path,
        ),
        dict(
            _target_="rainbowneko.infer.workflow.classify.ClassifyPredictor",
        ),
        dict(
            _target_="rainbowneko.infer.workflow.io.PrintResults",
            keys=["predict_label", "ground_truth_label"],
        ),
    ]
)

# 合并基础配置和当前配置
cfg = OmegaConf.create()
cfg = merge_cfg(cfg, _base_)
cfg = merge_cfg(cfg, OmegaConf.create(data=data, model=model, infer=infer))