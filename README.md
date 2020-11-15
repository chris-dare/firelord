# firelord

Sorry the documentation is terrible. I will update this after finishing a pending assignment :-)

There's a bug in training the model...I think. I'll come back to this after the precious assignment. If you find it :-)....feel free to open an issue on this repository....or submit a pull request to fix it if you're feeling like you wanna give it a try

- Chris

## Edit
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

** Comprehensive documentation will folow soon.

