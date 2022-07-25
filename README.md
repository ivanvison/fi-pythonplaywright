Thank you for getting to this point. This repository was created for a quick run/test using Python and Playwright after 2 courses (Playwright with Java and Playwright with Python).

The application used for testing purposes was Fusion Invoice Online Demo. Shoutout to them :D [Link](https://www.fusioninvoice.com/)

## The basics (nor particular order):
- Test login with parametrization
- Assert login screen
- Assert dashboard
- Create and Assert new clients (using CSV file) and Make sure they appear in the main list
- Fail test cases on purpose
- Use GitHub Actions

## Install / Usage Process (My personal setup)
1. Installed [VS Code](https://code.visualstudio.com).
2. Installed [Python](https://python.org).
3. Added Environment Variables
    - The path to `python.exe`, usually `C:\Users\Ivan\AppData\Local\Programs\Python\Python310\`
    - Press Start > Write `environment` > Click `Edit the system variables environment`
    - Click Environment Variables
    - Under System variables, click New
    - Variable Name = python
    - Variable Value = C:\Users\Ivan\AppData\Local\Programs\Python\Python310\
    - Ok > Ok

4. Install needed Libraries 
    - `pip install pytest-playwright`
    - `playwright install`
    - `pip install pytest-reporter-html1`
    - `pip install pytest-xdist`
    - `pip install pytest_dotenv`
    - `pip install pytest-playwright-visual`

5. Create GitHub Action
    - Add Secret variables
    - Update YML file

## Run
`pytest` -- then sit back, relax and enjoy the ride!