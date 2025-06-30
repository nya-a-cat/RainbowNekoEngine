import os
import random
from PIL import Image
import webdataset as wds
import io

def create_dummy_webdataset(tar_file="data.tar", num_samples=100, image_size=(64, 64), num_classes=3):
    """
    创建一个模拟的 WebDataset .tar 文件。
    每个样本包含一个图像和一个类别标签。
    """
    os.makedirs(os.path.dirname(tar_file) or ".", exist_ok=True) # 确保目录存在
    with wds.ShardWriter(tar_file, maxsize=1000000000) as sink: # maxsize 1GB
        for i in range(num_samples):
            class_idx = random.randint(0, num_classes - 1)
            
            # 创建一个简单的空白图片
            img = Image.new('RGB', image_size, color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            
            # 将图片转换为字节流
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            sample = {
                "__key__": f"sample_{i:06d}",
                "png": img_byte_arr,
                "cls": str(class_idx) # 标签通常以字符串形式存储
            }
            sink.write(sample)
    print(f"模拟 WebDataset 文件 '{tar_file}' 已创建，包含 {num_samples} 个样本。")

if __name__ == "__main__":
    create_dummy_webdataset()