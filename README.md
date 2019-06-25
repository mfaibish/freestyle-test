# robo-advisor

## SETUP
### Repo Setup
    1. Create new repository called robo-advisor (include gitignore file)
    2. Download repository to desktop
    3. After downloading the repo, navigate there from the command-line:

        ```sh
        cd ~/Desktop/robo-advisor
        ```

    4. Create new sub directory called app and add robo_advisor.py file to it
    5. Add the following contents to the file
        ```py
        # app/robo_advisor.py

        print("-------------------------")
        print("SELECTED SYMBOL: XYZ")
        print("-------------------------")
        print("REQUESTING STOCK MARKET DATA...")
        print("REQUEST AT: 2018-02-20 02:00pm")
        print("-------------------------")
        print("LATEST DAY: 2018-02-20")
        print("LATEST CLOSE: $100,000.00")
        print("RECENT HIGH: $101,000.00")
        print("RECENT LOW: $99,000.00")
        print("-------------------------")
        print("RECOMMENDATION: BUY!")
        print("RECOMMENDATION REASON: TODO")
        print("-------------------------")
        print("HAPPY INVESTING!")
        print("-------------------------")
        ```
    6. Create a requirements.txt file in the repo and add the following to it
        ```
        requests
        python-dotenv
        ```
### Environment Setup
    1. Create and activate a new Anaconda virtual environment:
        ```sh
        conda create -n stocks-env python=3.7 # (first time only)
        conda activate stocks-env
        ```
    2. From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:
        ```sh
        pip install -r requirements.txt
        pip install pytest # (only if you'll be writing tests)
        ```
    3. From within the virtual environment, demonstrate your ability to run the Python script from the command-line:
        ```sh
        python robo_advisor.py
        ```
## Requirements 
    1. Ensure the .env file is present in your .gitignore files created at the repository creation 
    2. Create a data directory in the repo with another .gitignore file. Plase the following inside 
        # data/.gitignore

        # h/t: https://stackoverflow.com/a/5581995/670433

        # ignore all files in this directory:
        *

        # except this gitignore file:
        !.gitignore
### Security Requirements
    3. Create an AlphaVantage API key as a variable and place within a .env file in the repo. This will be "hidden" as part of the .gitignore file

## USAGAE
    4. Execute the code by running 
   ```sh
   python robo_advisor.py
   ```
    A list of prices will export to a csv file after a successful run of the code and a printout today's prices should display.

## TESTING
    5. run tests by running pytest in the terminal
    ``` sh
    pytest
    ```