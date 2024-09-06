install:
    pip install -r requirements.txt

lint:
    flake8 ids706_mini_project

test:
    pytest tests
