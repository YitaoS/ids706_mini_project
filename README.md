# My Python Project

## Setup

1. Clone the repo:
`git clone https://github.com/YitaoS/my_python_project.git cd my_python_project`

2. Build the development environment using the devcontainer:

If you're using VSCode:
- Open the project in VSCode and select "Reopen in Container".

Or manually:
`docker build -t my_python_project . docker run -v $(pwd):/workspace -it my_python_project`

3. Install dependencies:
`make install`


## Usage

To lint the code:

`make lint`

To run the tests:

`make test`


## CI/CD

![CI Status](https://github.com/YitaoS/my_python_project/actions/workflows/ci.yml/badge.svg)
