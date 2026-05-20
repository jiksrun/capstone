import streamlit as st
from PIL import Image

from src.model_loader import get_device, load_model
from src.prediction import predict_image


st.set_page_config(
    page_title="Fruit Freshness Detection",
    page_icon=":material/nutrition:",
    layout="wide",
)


def inject_styles():
    st.markdown(
        """
        <style>
        :root {
            --fresh: #1f8a4c;
            --fresh-soft: #e8f5ec;
            --warning: #b45309;
            --danger: #b42318;
            --danger-soft: #fff0ec;
            --ink: #1f2933;
            --muted: #667085;
            --line: #d9e2dc;
            --panel: #ffffff;
            --paper: #f5f7f3;
            --shadow: 0 18px 45px rgba(31, 41, 51, 0.08);
        }

        .stApp {
            background:
                linear-gradient(180deg, #eef6ee 0, #f7faf7 260px, #f5f7f3 100%);
            color: var(--ink);
        }

        .block-container {
            padding-top: 1.4rem;
            padding-bottom: 2.5rem;
            max-width: 1120px;
        }

        [data-testid="stSidebar"],
        [data-testid="stSidebarNav"] {
            display: none;
        }

        h1, h2, h3 {
            color: var(--ink);
            letter-spacing: 0;
        }

        .hero {
            background:
                linear-gradient(135deg, rgba(255,255,255,.98) 0%, rgba(236,247,239,.98) 100%);
            border: 1px solid var(--line);
            border-radius: 12px;
            display: grid;
            grid-template-columns: minmax(0, 1fr) 260px;
            gap: 1.2rem;
            padding: 1.5rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow);
        }

        .eyebrow {
            color: var(--fresh);
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.35rem;
        }

        .hero-title {
            font-size: 2.25rem;
            line-height: 1.18;
            font-weight: 780;
            margin: 0 0 0.35rem 0;
        }

        .hero-subtitle {
            color: var(--muted);
            font-size: 1rem;
            max-width: 860px;
            margin: 0;
        }

        .hero-side {
            background: rgba(255,255,255,.72);
            border: 1px solid #cfdfd3;
            border-radius: 10px;
            padding: 1rem;
        }

        .hero-side-title {
            color: var(--muted);
            font-size: .8rem;
            font-weight: 700;
            margin-bottom: .55rem;
            text-transform: uppercase;
        }

        .hero-stat {
            border-bottom: 1px solid #dce8df;
            padding: .46rem 0;
        }

        .hero-stat:last-child {
            border-bottom: 0;
            padding-bottom: 0;
        }

        .hero-stat strong {
            display: block;
            font-size: .95rem;
        }

        .hero-stat span {
            color: var(--muted);
            font-size: .82rem;
        }

        .panel {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1.05rem 1.15rem;
            margin-bottom: 1rem;
            box-shadow: 0 10px 28px rgba(31, 41, 51, 0.05);
        }

        .section-kicker {
            color: var(--fresh);
            font-size: .78rem;
            font-weight: 760;
            letter-spacing: .08em;
            text-transform: uppercase;
        }

        .section-title {
            font-size: 1.28rem;
            font-weight: 780;
            margin: .1rem 0 .1rem 0;
        }

        .panel-title {
            font-size: 1rem;
            font-weight: 760;
            margin-bottom: 0.45rem;
        }

        .muted {
            color: var(--muted);
        }

        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: 0.75rem;
        }

        .pill {
            border: 1px solid #b8d9c4;
            background: var(--fresh-soft);
            border-radius: 999px;
            color: #14532d;
            font-size: 0.82rem;
            font-weight: 650;
            padding: 0.26rem 0.58rem;
        }

        .result-fresh {
            background: #f0faf3;
            border-color: #b8d9c4;
        }

        .result-rotten {
            background: #fff6f3;
            border-color: #f2b7aa;
        }

        .small-label {
            color: var(--muted);
            font-size: 0.82rem;
            margin-bottom: 0.1rem;
        }

        .result-card {
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 1.15rem 1.2rem;
            margin-bottom: 1rem;
        }

        .result-label {
            font-size: 2.05rem;
            font-weight: 820;
            line-height: 1.12;
            margin-bottom: .2rem;
        }

        .confidence-band {
            background: #eef5ef;
            border-radius: 999px;
            height: 10px;
            margin-top: .75rem;
            overflow: hidden;
        }

        .confidence-fill {
            background: var(--fresh);
            height: 10px;
        }

        .prob-row {
            margin: .62rem 0;
        }

        .prob-head {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            font-size: .9rem;
            margin-bottom: .25rem;
        }

        .prob-name {
            color: var(--ink);
            font-weight: 650;
        }

        .prob-value {
            color: var(--muted);
            font-variant-numeric: tabular-nums;
        }

        .prob-track {
            background: #edf2ee;
            border-radius: 999px;
            height: 8px;
            overflow: hidden;
        }

        .prob-fill {
            background: #2f9461;
            height: 8px;
        }

        .empty-result {
            align-items: center;
            background: #ffffff;
            border: 1px dashed #b8c9bd;
            border-radius: 10px;
            color: var(--muted);
            display: flex;
            min-height: 310px;
            padding: 1.2rem;
        }

        .stFileUploader {
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 0.75rem;
        }

        .stCameraInput {
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 0.75rem;
        }

        @media (max-width: 760px) {
            .hero {
                grid-template-columns: 1fr;
            }
            .hero-title {
                font-size: 1.5rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_resource
def cached_model():
    device = get_device()
    model = load_model(device=device)
    return model, device


def render_header():
    classes = "".join(
        f'<span class="pill">{class_name}</span>'
        for class_name in ["Fresh Apple", "Fresh Banana", "Fresh Strawberry", "Rotten Apple", "Rotten Banana", "Rotten Strawberry"]
    )

    st.markdown(
        f"""
        <section class="hero">
            <div>
                <div class="eyebrow">Fruit Freshness Detection</div>
                <div class="hero-title">Check fruit freshness from an image</div>
                <p class="hero-subtitle">
                    Capture or upload a fruit photo. The prototype returns a freshness label, confidence score, and class probability ranking.
                </p>
                <div class="pill-row">{classes}</div>
            </div>
            <aside class="hero-side">
                <div class="hero-side-title">Demo Scope</div>
                <div class="hero-stat"><strong>3 fruits</strong><span>Apple, banana, strawberry</span></div>
                <div class="hero-stat"><strong>6 classes</strong><span>Fresh and rotten categories</span></div>
                <div class="hero-stat"><strong>Real-time use</strong><span>Upload or camera capture</span></div>
            </aside>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_prediction(result):
    confidence_percent = result["confidence"] * 100
    freshness = "Fresh" if result["class_name"].startswith("Fresh") else "Rotten"
    panel_class = "result-fresh" if freshness == "Fresh" else "result-rotten"
    decision = "The fruit appears fresh." if freshness == "Fresh" else "The fruit shows rotten/spoilage characteristics."
    confidence_width = max(0, min(100, confidence_percent))
    accent_color = "#1f8a4c" if freshness == "Fresh" else "#b42318"

    st.markdown(
        f"""
        <div class="result-card {panel_class}">
            <div class="small-label">Prediction</div>
            <div class="result-label">{result["display_name"]}</div>
            <div class="muted">{decision}</div>
            <div class="confidence-band">
                <div class="confidence-fill" style="width: {confidence_width:.1f}%; background: {accent_color};"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metric_col, status_col = st.columns(2)
    metric_col.metric("Confidence", f"{confidence_percent:.1f}%")
    status_col.metric("Freshness", freshness)

    st.markdown("#### Probability ranking")
    rows = []
    for item in result["scores"]:
        probability = item["probability"] * 100
        rows.append(
            f"""
            <div class="prob-row">
                <div class="prob-head">
                    <span class="prob-name">{item["class"]}</span>
                    <span class="prob-value">{probability:.1f}%</span>
                </div>
                <div class="prob-track">
                    <div class="prob-fill" style="width: {probability:.1f}%;"></div>
                </div>
            </div>
            """
        )
    st.markdown("".join(rows), unsafe_allow_html=True)


def get_input_image():
    st.markdown('<div class="section-kicker">Input</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Add fruit image</div>', unsafe_allow_html=True)
    st.caption("Use a clear image with one apple, banana, or strawberry visible in the frame.")

    input_mode = st.radio(
        "Image source",
        ["Upload", "Camera"],
        horizontal=True,
    )
    image = None
    source_label = None

    if input_mode == "Upload":
        uploaded_file = st.file_uploader(
            "Choose JPG or PNG file",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=False,
        )
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            source_label = "Uploaded image"
    else:
        camera_file = st.camera_input("Take a photo")
        if camera_file is not None:
            image = Image.open(camera_file)
            source_label = "Camera capture"

    if image is not None:
        st.image(image, caption=source_label, width="stretch")

    return image


def main():
    inject_styles()
    render_header()

    input_col, result_col = st.columns([0.92, 1.08], vertical_alignment="top")

    with input_col:
        image = get_input_image()

    with result_col:
        st.markdown('<div class="section-kicker">Output</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Freshness result</div>', unsafe_allow_html=True)

        if image is None:
            st.markdown(
                """
                <div class="empty-result">
                    Add an image to generate a freshness prediction, confidence score, and class probability ranking.
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            try:
                model, device = cached_model()
                result = predict_image(image, model, device)
                render_prediction(result)
            except Exception as exc:
                st.error("Prediction failed.")
                st.exception(exc)


if __name__ == "__main__":
    main()
