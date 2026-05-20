# Fruit Freshness Detection

Streamlit prototype for classifying fruit freshness from an image. The app supports apple, banana, and strawberry images, then predicts one of six classes:

- Fresh Apple
- Fresh Banana
- Fresh Strawberry
- Rotten Apple
- Rotten Banana
- Rotten Strawberry

The application is built as a capstone project demo. It focuses on the user workflow: add an image, preview it, and view the predicted freshness label with confidence.

## Features

- Upload an image from local storage.
- Capture an image using the device camera.
- Preview the selected image.
- Run inference with a trained PyTorch model.
- Display the predicted class, freshness group, confidence score, and probability ranking.

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── model_loader.py
│   ├── prediction.py
│   └── preprocessing.py
└── model/
    └── best_food_freshness_model.pth
```

## Model

The app expects the trained model file here:

```text
model/best_food_freshness_model.pth
```

The current app reconstructs a ResNet-18 classifier and loads the saved PyTorch `state_dict`. The class order is defined in `src/config.py`; keep that order aligned with training.

## Local Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, usually:

```text
http://localhost:8501
```

<!-- ## Deployment Notes -->
<!---->
<!-- For Streamlit deployment, make sure these files are included in the repository: -->
<!---->
<!-- - `app.py` -->
<!-- - `requirements.txt` -->
<!-- - `.streamlit/config.toml` -->
<!-- - `src/` -->
<!-- - `model/best_food_freshness_model.pth` -->
<!---->
<!-- The `data/`, `laporan/`, and most notebook files are intentionally ignored by Git. Only notebooks beginning with `CAPSTONE` are allowed by `.gitignore`. -->
<!---->
<!-- ## Git Ignore Policy -->
<!---->
<!-- This project excludes large or non-deployment files: -->
<!---->
<!-- ```text -->
<!-- data/ -->
<!-- laporan/ -->
<!-- .venv/ -->
<!-- notebook/*.ipynb -->
<!-- !notebook/CAPSTONE*.ipynb -->
<!-- model/*.pth -->
<!-- !model/best_food_freshness_model.pth -->
<!-- ``` -->
<!---->
<!-- The deployed model is currently about 43 MB, so regular Git is still acceptable. Git LFS is not required unless future model files grow significantly or multiple checkpoints need to be tracked. -->
<!---->
<!-- ## Troubleshooting -->
<!---->
<!-- If model loading fails, check that: -->
<!---->
<!-- - `model/best_food_freshness_model.pth` exists. -->
<!-- - The architecture in `src/model_loader.py` matches the training architecture. -->
<!-- - The class order in `src/config.py` matches training. -->
<!---->
<!-- If image prediction fails inside `torchvision.transforms`, confirm the installed NumPy version is below 2: -->
<!---->
<!-- ```bash -->
<!-- python -c "import numpy; print(numpy.__version__)" -->
<!-- ``` -->
<!---->
<!-- The dependency file pins `numpy<2` for compatibility with the current PyTorch CPU build. -->
