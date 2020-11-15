# firelord

Sorry the documentation is (edit:still quite) terrible. I will update this after finishing a pending assignment. Code comments will come soon :-)

There's a bug in training the model...I think. I'll come back to this after the precious assignment. If you find it :-)....feel free to open an issue on this repository....or submit a pull request to fix it if you're feeling like you wanna give it a try

- Chris

# About
Todo: complete
## Motivation

## Setup
Install packages with pip or Poetry:
### Poetry
Packages are installed and managed by [poetry](https://python-poetry.org/). 
To install poetry (linux/OSX) run the following command:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
Detailed setup instructions for poetry are available [here](https://python-poetry.org/docs/)

Dependencies for the project can be seen in `./pyproject.toml`. 
Install dependencies with:
```bash
poetry install
```

### Alternative: Pip 
If you'd rather not install your dependencies with poetry, you can install raw pip to get the job done.
That said, raw pip installs can bring dependency management issues. So brace yourself. 
Install dependencies
```pip install -r requirements.txt```
If you have connection timeouts whilst installing some of the packages, considering increasing the default timeout
```bash
pip install -r requirements.txt --default-timeout=1000 
```

## File project structure


## Usage

### Getting data
Text goes here

#### Downloading the dataset
Text goes here

#### Getting training and testing data
Text goes here

### Training the machine learning model
Text goes here



## Launching the application (entry points)
The sample app has 3 entry points:
1. The ML API.
The entry point is `./api/main.py`
It runs on FastAPI. To launch this execute this command from the root:
```bash
uvicorn api.main:app --reload --port 8080
```

2. The web app.
The entry point is `./app.py`
It runs on streamlit. To launch, execute this command from the root:
```bash
streamlit run app.py
```

3. The cli for retraining the model
The entry point is `./cli.py`
This is currently buggy, I will update the code next (hopefully) unless someone beats me to it with a pull request.

** Comprehensive documentation will follow soon.

