from rainbowneko.data.source.base import BaseSource
from torch.utils.data import Dataset
import os

class MyCustomDataset(Dataset):
    """
    一个模拟的自定义 PyTorch Dataset，用于演示自定义数据处理。
    """
    def __init__(self, data_file, transform=None):
        self.data = []
        with open(data_file, 'r') as f:
            for line in f:
                self.data.append(line.strip())
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # 模拟数据处理，例如将文本转换为数字或特征
        item = self.data[idx]
        # 假设这里 item 是一个字符串 "feature1,feature2,label"
        parts = item.split(',')
        features = [float(p) for p in parts[:-1]]
        label = int(parts[-1])
        
        # 如果有 transform，则应用 transform
        if self.transform:
            features = self.transform(features)
        
        return {"data": features, "label": label}


class MyCustomSource(BaseSource):
    """
    一个自定义的 RainbowNeko 数据源，包装 MyCustomDataset。
    """
    def __init__(self, data_file_path, **kwargs):
        super().__init__(**kwargs)
        self.data_file_path = data_file_path
        # 模拟创建数据文件
        self._create_dummy_data_file()

    def _create_dummy_data_file(self):
        """
        创建一个模拟的数据文件，例如 CSV 格式。
        """
        if not os.path.exists(self.data_file_path):
            os.makedirs(os.path.dirname(self.data_file_path), exist_ok=True)
            with open(self.data_file_path, 'w') as f:
                for i in range(100): # 100个样本
                    f.write(f"{i*0.1},{i*0.2},{i % 2}\n") # 两个特征，一个二分类标签
            print(f"模拟数据文件已创建: {self.data_file_path}")

    def get_dataset(self, transform=None):
        """
        返回一个 PyTorch Dataset 实例。
        """
        return MyCustomDataset(self.data_file_path, transform=transform)

    def get_len(self):
        """
        返回数据集的长度。
        """
        # 简单起见，这里直接返回模拟数据文件的行数
        with open(self.data_file_path, 'r') as f:
            return sum(1 for line in f)

    def get_labels(self):
        """
        返回所有可能的标签。
        """
        return [0, 1] # 模拟二分类