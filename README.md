# The Student Sentiment Sensor (SSS)
### Our Northeastern University senior capstone project
by Jack Carson, Tyler Ceballo, Mark Morton, Dave Pleteau, & John Privitera
<br><br/>

# Getting started

## Prerequisites
- Python3 is installed.
- Node.js is installed (Version < 17.0)
  - Note: Do not install node via a package manager like Debian's `apt`. Consider using `nvm`.
  - Note: "sudo apt-get install node npm" may work/be a potential fix
- *A Linux-type environment works best.*

## Setup
`git clone <remote_url>`
TODO: it might be necessary to install several packages with `pip`.
### Node local dependencies
First, navigate to the project root directory.
```bash
cd ./frontend/fe-filesystem-api/
npm install
```
Second, open a new terminal and navigate to the project root directory.
```bash
cd ./frontend/fe-main/
npm install
```

## Running the app
First, navigate to the project root directory.
```bash
cd ./backend/
# `python3` may be substituted for `python` if necessary.
python3 backend.py
```

Second, open a new terminal and navigate to the project root directory.
```bash
cd ./frontend/fe-filesystem-api/
# `yarn` may be substituted for `npm` if desired.
npm start
```

Third, open a new terminal and navigate to the project root directory.
```bash
cd ./frontend/fe-main/
# `yarn` may be substituted for `npm` if desired.
npm start
```
