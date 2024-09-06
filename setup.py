from setuptools import setup, find_packages

# 读取 requirements.txt 作为依赖
def parse_requirements(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

setup(
    name='my_python_project',  # 项目名称
    version='0.1',  # 项目版本
    packages=find_packages(),  # 自动查找所有包
    install_requires=parse_requirements('requirements.txt'),  # 安装项目运行所需的依赖
    extras_require={
        'dev': [
            'flake8',  # 用于 lint
            'black',   # 用于代码格式化
            'pytest',  # 用于测试
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # 指定最低 Python 版本要求
)
