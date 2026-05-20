from html import escape

import streamlit as st


SUPPORTED_CLASSES = [
    "Fresh Apple",
    "Fresh Banana",
    "Fresh Strawberry",
    "Rotten Apple",
    "Rotten Banana",
    "Rotten Strawberry",
]


def render_header():
    pills = "".join(f'<span class="pill">{escape(name)}</span>' for name in SUPPORTED_CLASSES)
    st.markdown(
        f"""
        <section class="hero">
            <div>
                <div class="kicker">Fruit Freshness Detection</div>
                <div class="hero-title">Check fruit freshness from an image</div>
                <p class="hero-copy">
                    Upload or capture apple, banana, and strawberry photos. The app returns the predicted class,
                    confidence, buying recommendation, and probability ranking for every candidate.
                </p>
                <div class="class-pills">{pills}</div>
            </div>
            <aside class="hero-side">
                <div class="hero-stat"><strong>3 fruits</strong><span>Apple, banana, strawberry</span></div>
                <div class="hero-stat"><strong>6 classes</strong><span>Fresh and rotten categories</span></div>
                <div class="hero-stat"><strong>Decision support</strong><span>Prediction, confidence, recommendation</span></div>
            </aside>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(step, title, caption):
    st.markdown(
        f"""
        <div class="section-head">
            <div>
                <div class="kicker">{escape(step)}</div>
                <div class="section-title">{escape(title)}</div>
                <p class="section-copy">{escape(caption)}</p>
            </div>
            <span class="step-badge">{escape(step)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
