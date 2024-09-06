# My Python Project

## Setup

1. Clone the repo:
`git clone https://github.com/YitaoS/ids706_mini_project.git cd ids706_mini_project`

2. Build the development environment using the devcontainer:

If you're using VSCode:
- Open the project in VSCode and select "Reopen in Container".

Or manually:
`docker build -t ids706_mini_project . docker run -v $(pwd):/workspace -it ids706_mini_project`

3. Install dependencies:
`make install`


## Usage

To lint the code:

`make lint`

To run the tests:

`make test`


## CI/CD

![CI Status](https://github.com/YitaoS/ids706_mini_project/actions/workflows/ci.yml/badge.svg)
