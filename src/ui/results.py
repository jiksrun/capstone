from html import escape

import streamlit as st


def is_fresh(result):
    return result["class_name"].startswith("Fresh")


def action_text(result):
    return "Recommended action: Good to buy" if is_fresh(result) else "Recommended action: Avoid buying"


def probability_rows_html(result, limit=3):
    selected_scores = result["scores"][:limit]
    rows = []
    for item in selected_scores:
        probability = item["probability"] * 100
        bar_class = "rotten" if item["class"].startswith("Rotten") else ""
        rows.append(
            f'<div class="prob-row">'
            f'<div class="prob-head">'
            f'<span class="prob-name">{escape(item["class"])}</span>'
            f'<span class="prob-value">{probability:.1f}%</span>'
            f'</div>'
            f'<div class="prob-track">'
            f'<div class="prob-fill {bar_class}" style="width: {probability:.1f}%;"></div>'
            f'</div>'
            f'</div>'
        )
    return "".join(rows)


def render_summary(predictions):
    total = len(predictions)
    fresh_items = [item for item in predictions if is_fresh(item["result"])]
    rotten_count = total - len(fresh_items)
    best_item = max(fresh_items, key=lambda item: item["result"]["confidence"], default=None)

    st.markdown(
        f"""
        <div class="summary-grid">
            <div class="summary-card">
                <div class="summary-value">{total}</div>
                <div class="summary-label">Images checked</div>
            </div>
            <div class="summary-card">
                <div class="summary-value">{len(fresh_items)}</div>
                <div class="summary-label">Predicted fresh</div>
            </div>
            <div class="summary-card">
                <div class="summary-value">{rotten_count}</div>
                <div class="summary-label">Predicted rotten</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if best_item:
        result = best_item["result"]
        st.markdown(
            f"""
            <div class="recommend-card">
                <div class="small-label">Best predicted option</div>
                <div class="recommend-title">
                    {escape(best_item["name"])} - {escape(result["display_name"])} - {result["confidence"] * 100:.1f}% confidence
                </div>
                <div class="muted">Selected only from images predicted as fresh, using the highest model confidence.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    st.markdown(
        f"""
        <div class="recommend-card no-buy">
            <div class="small-label">Best predicted option</div>
            <div class="recommend-title">No recommended purchase</div>
            <div class="muted">All {total} selected image(s) were predicted as rotten, so every candidate is marked avoid buying.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def candidate_card_html(item, show_probabilities=True):
    result = item["result"]
    confidence = result["confidence"] * 100
    fresh = is_fresh(result)
    card_class = "candidate-fresh" if fresh else "candidate-rotten"
    action_class = "action-good" if fresh else "action-avoid"
    freshness = "Fresh" if fresh else "Rotten"
    status_class = "status-fresh" if fresh else "status-rotten"
    confidence_width = max(0, min(100, confidence))
    probability_section = (
        f'<div class="prob-list">{probability_rows_html(result, limit=3)}</div>'
        if show_probabilities
        else ""
    )

    return (
        f'<article class="candidate-card {card_class}">'
        f'<div class="candidate-top">'
        f'<div class="candidate-meta">'
        f'<div class="candidate-source">{escape(item["name"])}</div>'
        f'<span class="status-chip {status_class}">{freshness}</span>'
        f'</div>'
        f'<div class="prediction-name">{escape(result["display_name"])}</div>'
        f'<div class="confidence-line">{confidence:.1f}% model confidence</div>'
        f'<div class="{action_class}">{action_text(result)}</div>'
        f'<div class="confidence-rail">'
        f'<div class="confidence-fill" style="width: {confidence_width:.1f}%;"></div>'
        f'</div>'
        f'</div>'
        f'{probability_section}'
        f'</article>'
    )


def render_results(predictions):
    if len(predictions) > 1:
        render_summary(predictions)

    st.markdown("#### Candidate predictions")
    if len(predictions) == 1:
        st.markdown(candidate_card_html(predictions[0]), unsafe_allow_html=True)
        return

    for start in range(0, len(predictions), 2):
        row = predictions[start : start + 2]
        cols = st.columns(2, gap="medium")
        for index, item in enumerate(row):
            with cols[index]:
                st.markdown(candidate_card_html(item, show_probabilities=False), unsafe_allow_html=True)
