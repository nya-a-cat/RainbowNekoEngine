import os
import random
from PIL import Image

def create_dummy_dataset(base_dir="data", num_classes=3, images_per_class=10):
    """
    创建模拟图像分类数据集。
    数据集结构:
    data/
    ├── train/
    │   ├── class_0/
    │   │   ├── img_00.png
    │   │   ├── ...
    │   ├── class_1/
    │   ├── ...
    └── val/
        ├── class_0/
        ├── ...
    """
    train_dir = os.path.join(base_dir, "train")
    val_dir = os.path.join(base_dir, "val")

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    for phase_dir, count_multiplier in [(train_dir, 0.8), (val_dir, 0.2)]:
        for class_idx in range(num_classes):
            class_name = f"class_{class_idx}"
            class_path = os.path.join(phase_dir, class_name)
            os.makedirs(class_path, exist_ok=True)

            num_images = int(images_per_class * num_classes * count_multiplier)
            for i in range(num_images):
                img_name = f"img_{i:02d}.png"
                img_path = os.path.join(class_path, img_name)
                # 创建一个简单的空白图片
                img = Image.new('RGB', (64, 64), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                img.save(img_path)
    print(f"模拟数据集已创建在: {os.path.abspath(base_dir)}")

if __name__ == "__main__":
    create_dummy_dataset()