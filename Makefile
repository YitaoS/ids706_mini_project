# 变量设置
PYTHON_FILES := ids706_mini_project tests

# 安装依赖
install:
	pip install -r requirements.txt

# 代码格式化
format:
	black $(PYTHON_FILES)

# 代码检查
lint:
	flake8 $(PYTHON_FILES)

# 运行测试
test:
	pytest tests

# 清理缓存文件
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

# 检查代码格式（未格式化的文件）
check-format:
	black --check $(PYTHON_FILES)

# 自动化运行 lint, test, 和格式化检查
ci: lint test check-format
