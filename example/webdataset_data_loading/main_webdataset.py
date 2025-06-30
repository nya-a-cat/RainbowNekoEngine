import os
import sys
from rainbowneko.parser.py_cfg import parse_config_args
from rainbowneko.train.trainer.trainer_ac import neko_train

if __name__ == "__main__":
    # 添加当前目录到 Python 路径，以便可以找到 webdataset_train_config.py
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # 解析命令行参数，获取配置文件路径
    args = parse_config_args()
    
    # 调用训练函数
    neko_train(args)