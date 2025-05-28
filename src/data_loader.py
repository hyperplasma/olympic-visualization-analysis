import os
import pandas as pd

def scan_data(data_dir='data'):
    """
    扫描data目录下所有csv/xlsx文件和主要子文件夹，输出字段和样例数据
    """
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.csv') or file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                print(f"\n数据集文件: {file_path}")
                try:
                    if file.endswith('.csv'):
                        df = pd.read_csv(file_path, nrows=5)
                    else:
                        df = pd.read_excel(file_path, nrows=5)
                    print("字段名:", list(df.columns))
                    print("样例数据:")
                    print(df.head(2))
                except Exception as e:
                    print(f"读取失败: {e}")

if __name__ == "__main__":
    scan_data()