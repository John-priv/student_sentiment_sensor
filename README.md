# The Student Sentiment Sensor (SSS)
<img src="https://lh3.googleusercontent.com/pw/AM-JKLVXPv5zsE2lErrMfOb7ofSLjWxL8Q4oKZeRAVmLScC1NXNfolqvaXcUKFhNwoKi0s5EsYabntapggd4_vTIgTlHV1wMbV033gZSyX2cRhM2AHHxNDWSPuYiTWE9vyyHzWLwaNi0k45zAW3YvqVbQlWs5w=w875-h492-no" alt="studentsWalking_img" width="350"/>

### Our Northeastern University senior capstone project
by Jack Carson, Tyler Ceballo, Mark Morton, Dave Pleteau, & John Privitera
<br><br/>

# The premise

## Some context
44% of college students in a 2021 national study reported symptoms of anxiety and depression (“College students and Depression,” Mayo Clinic Health System, 07-Sep-2021).
Although on-campus mental health resources exist, a limited amount of people may make the time for them and many who need help are reluctant to reach out for various reasons.

## Our solution
Leveraging 8MP computer vision (CV) from the FER Python library running on a Raspberry Pi we rapidly—in 3.0s—identified passing students who appear distressed and seeded a React-based touchscreen interaction with them.

We predicted each student's core stressors with a combination of the CV module’s facial emotion (classifying out of 7 total) detection and a Python-constructed decision tree of survey-like questions.<br>
![q_img](https://lh3.googleusercontent.com/pw/AM-JKLUUg7FehxbpHcQgpAmNSu-YMxOU05FIdaFqAdNqBhljv3tzxf5dlZjMmed8mqrWdz9DrjhcVjQvUodBHpDCqGiRGlMdCDfQDoExsv1mngoU-FwykihsijPz74Kv3bhpNnswbjl659txAcofEEjB4xlXHg=w1022-h412-no)

Finally, we provided users with curated support resources by email in order to actively advance student mental health by kickstarting the process.<br>
![resource_img](https://lh3.googleusercontent.com/pw/AM-JKLWETg96OYg8NruHogwboaUqrC3MoeseLTA-E0gFHp31j3x3UIMml_rKAQKpHa2xL3mRPNJAPZZ0RT-NEgeL4fg6Qo8xmRBY6stUitTDCZbXT7sywhRggaaenRWnY0NVzQMajWbOBKBsY_CriOgzUwwGRQ=w937-h497-no)

# Getting started with the stack

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
