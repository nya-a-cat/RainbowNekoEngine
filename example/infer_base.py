# 这是一个基础推理配置文件，用于定义通用的推理参数和组件。
# 所有的推理示例都可以继承这个基础配置。

# 项目名称和输出目录
project_name = "inference_example"
output_dir = "./inference_output"

# 数据加载器配置 (占位符，具体示例中会定义)
data = dict(
    dataloader=dict(
        batch_size=32,
        num_workers=4,
        shuffle=False,
    ),
)

# 模型配置 (占位符，具体示例中会定义)
model = None

# 推理流程配置 (占位符，具体示例中会定义)
infer = dict(
    workflow=[]
)

# 其他通用配置