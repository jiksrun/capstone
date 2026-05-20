# Fruit Freshness Detection

Streamlit prototype for classifying fruit freshness from images. The app supports apple, banana, and strawberry, then predicts one of six classes:

- Fresh Apple
- Fresh Banana
- Fresh Strawberry
- Rotten Apple
- Rotten Banana
- Rotten Strawberry

The application is built as a capstone demo for consumer decision support. It lets users check one fruit image or compare multiple candidates, then returns a predicted freshness label, model confidence, and practical buying recommendation.

## Features

- Upload one or multiple fruit images.
- Capture fruit images one by one using the device camera.
- Compare multiple candidates in the same session.
- Show predicted class, freshness group, and model confidence.
- Recommend `Good to buy` for images predicted as fresh.
- Recommend `Avoid buying` for images predicted as rotten.
- For multiple candidates, show the best predicted option among images predicted as fresh.

Important wording: the app compares model predictions and model confidence. It does not claim to measure true biological freshness directly.

## Project Structure

```text
.
|-- app.py
|-- requirements.txt
|-- README.md
|-- TODO.md
|-- .gitignore
|-- .streamlit/
|   `-- config.toml
|-- src/
|   |-- __init__.py
|   |-- config.py
|   |-- model_loader.py
|   |-- prediction.py
|   `-- preprocessing.py
|-- model/
|   `-- best_food_freshness_model.pth
`-- notebook/
    |-- CAPSTONE_AUGMENTATION.ipynb
    `-- CAPSTONE_MODELING.ipynb
```

The app does not depend on notebooks at runtime. The notebooks document development, augmentation, and model training work.

## Model

The app expects the trained model file here:

```text
model/best_food_freshness_model.pth
```

The current app reconstructs a ResNet-18 classifier and loads the saved PyTorch `state_dict`. The class order is defined in `src/config.py`; keep that order aligned with the training notebook.

## Local Setup

Clone the repo and change dir:
```bash
git clone https://github.com/jiksrun/capstone.git
cd capstone
```

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

Full one:
```bash
git clone https://github.com/jiksrun/capstone.git
cd capstone
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```


<!-- ## Deployment -->
<!---->
<!-- For Streamlit deployment, include: -->
<!---->
<!-- - `app.py` -->
<!-- - `requirements.txt` -->
<!-- - `.streamlit/config.toml` -->
<!-- - `src/` -->
<!-- - `model/best_food_freshness_model.pth` -->
<!---->
<!-- The `data/`, `laporan/`, `.venv/`, and non-CAPSTONE notebooks are intentionally excluded from Git. -->
<!---->
<!-- The model file is about 43 MB. Regular Git is acceptable for now; Git LFS is not required unless future model files become much larger or multiple checkpoints are tracked. -->
<!---->
<!-- ## Troubleshooting -->
<!---->
<!-- If model loading fails, check that: -->
<!---->
<!-- - `model/best_food_freshness_model.pth` exists. -->
<!-- - The architecture in `src/model_loader.py` matches the training architecture. -->
<!-- - The class order in `src/config.py` matches training. -->
<!---->
<!-- If image prediction fails inside `torchvision.transforms`, confirm NumPy is below version 2: -->
<!---->
<!-- ```bash -->
<!-- python -c "import numpy; print(numpy.__version__)" -->
<!-- ``` -->
<!---->
<!-- The dependency file pins `numpy<2` for compatibility with the current PyTorch CPU build. -->
