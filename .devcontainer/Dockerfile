# 使用 Python 3.9 作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /workspace

# 复制依赖文件并安装项目依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 安装开发工具依赖
RUN pip install --no-cache-dir black flake8 pytest

# 复制项目代码到工作目录
COPY . /workspace

# 设置默认启动命令
CMD ["bash"]
