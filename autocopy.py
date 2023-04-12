import shutil
import os
import tkinter as tk
from tkinter import filedialog

# 创建GUI窗口
root = tk.Tk()

# 隐藏主窗口
root.withdraw()

# 弹出选择源文件夹的对话框
src_folder = filedialog.askdirectory(title='选择源文件夹')

# 弹出选择目标文件夹的对话框
dest_folder = filedialog.askdirectory(title='选择目标文件夹')

# 复制文件
for file_name in os.listdir(src_folder):
    # 构造源文件和目标文件的绝对路径
    src_file_path = os.path.join(src_folder, file_name)
    dest_file_path = os.path.join(dest_folder, file_name)

    # 如果是文件而不是文件夹，就复制文件
    if os.path.isfile(src_file_path):
        shutil.copy(src_file_path, dest_file_path)

# 完成备份后进行提示
print("Backup complete.")

