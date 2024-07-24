import os
from PIL import Image

def downsample_image(input_path, output_path, target_width=160, target_height=90):
    # 打开图像
    img = Image.open(input_path)

    # 获取原始图像的尺寸
    width, height = img.size

    # 确保原始图像的尺寸是1920x1080
    if width != 1920 or height != 1080:
        raise ValueError("Input image must be 1920x1080 in size")

    # 创建一个新的图像用于存储降采样后的图像
    downsampled_img = Image.new("RGB", (target_width, target_height))

    # 计算每个块的尺寸
    block_width = width // target_width
    block_height = height // target_height

    for i in range(target_width):
        for j in range(target_height):
            # 计算中心像素的位置
            center_x = i * block_width + block_width // 2
            center_y = j * block_height + block_height // 2

            # 获取中心像素的值
            center_pixel = img.getpixel((center_x, center_y))

            # 将中心像素的值赋给降采样后的图像
            downsampled_img.putpixel((i, j), center_pixel)

    # 保存降采样后的图像
    downsampled_img.save(output_path)

def process_images(input_dir, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, 1856):
        input_file = os.path.join(input_dir, f"{i:04d}.png")
        output_file = os.path.join(output_dir, f"{i:04d}.png")
        
        try:
            downsample_image(input_file, output_file)
            print(f"Processed {input_file} -> {output_file}")
        except Exception as e:
            print(f"Failed to process {input_file}: {e}")

# 示例用法
input_directory = r"D:\workspace\Repo\Render\Blender\Donut\Output"  # 输入图像所在目录
output_directory = r"D:\workspace\Repo\Render\Blender\Donut\Output - Downsample"  # 输出图像保存目录

process_images(input_directory, output_directory)

