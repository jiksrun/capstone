import streamlit as st

from src.app_state import initialize_state
from src.model_loader import get_device, load_model
from src.prediction import predict_image
from src.ui.inputs import get_input_candidates
from src.ui.layout import render_header, render_section_header
from src.ui.results import render_results
from src.ui.styles import inject_styles


st.set_page_config(
    page_title="Fruit Freshness Detection",
    page_icon=":material/nutrition:",
    layout="wide",
)


@st.cache_resource
def cached_model():
    device = get_device()
    model = load_model(device=device)
    return model, device


def predict_candidates(candidates):
    model, device = cached_model()
    predictions = []
    for index, candidate in enumerate(candidates, start=1):
        predictions.append(
            {
                "index": index,
                "name": candidate["name"],
                "source": candidate["source"],
                "image": candidate["image"],
                "result": predict_image(candidate["image"], model, device),
            }
        )
    return predictions


def render_empty_state():
    st.markdown(
        """
        <div class="empty-state">
            Add fruit images to see predictions, confidence, buying recommendations, and probability rankings.
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    initialize_state()
    inject_styles()
    render_header()

    input_col, result_col = st.columns([0.42, 0.58], gap="medium", vertical_alignment="top")

    with input_col:
        with st.container(border=True):
            candidates = get_input_candidates()

    with result_col:
        with st.container(border=True):
            render_section_header(
                "Step 2",
                "Review predictions",
                "Every selected image gets a prediction and recommendation, including rotten-only batches.",
            )

            if not candidates:
                render_empty_state()
                return

            try:
                render_results(predict_candidates(candidates))
            except Exception as exc:
                st.error("Prediction failed.")
                st.exception(exc)


if __name__ == "__main__":
    main()
