install:
    pip install -r requirements.txt

lint:
    flake8 my_python_project

test:
    pytest tests
