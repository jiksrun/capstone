import streamlit as st


def inject_styles():
    st.markdown(
        """
        <style>
        :root {
            --bg: #f6f8f5;
            --surface: #ffffff;
            --surface-soft: #f0f5f1;
            --ink: #1f2933;
            --muted: #667085;
            --line: #d8e0da;
            --fresh: #167243;
            --fresh-soft: #e8f6ee;
            --fresh-line: #abd5bb;
            --rotten: #b42318;
            --rotten-soft: #fff0ec;
            --rotten-line: #f0b5a8;
            --blue-soft: #eaf2fb;
            --shadow: 0 14px 32px rgba(31, 41, 51, 0.07);
        }

        .stApp {
            background:
                linear-gradient(180deg, #edf6ee 0, #f7faf7 230px, var(--bg) 100%);
            color: var(--ink);
        }

        header[data-testid="stHeader"] {
            position: relative !important;
        }

        .block-container {
            max-width: 1320px;
            padding-top: 1rem;
            padding-bottom: 1.6rem;
        }

        [data-testid="stSidebar"],
        [data-testid="stSidebarNav"] {
            display: none;
        }

        h1, h2, h3, h4 {
            color: var(--ink);
            letter-spacing: 0;
        }

        .hero {
            background: rgba(255, 255, 255, 0.94);
            border: 1px solid var(--line);
            border-radius: 10px;
            box-shadow: var(--shadow);
            display: grid;
            gap: 1rem;
            grid-template-columns: minmax(0, 1fr) 260px;
            margin-bottom: .9rem;
            padding: 1rem;
        }

        .kicker {
            color: var(--fresh);
            font-size: .72rem;
            font-weight: 800;
            letter-spacing: .08em;
            margin-bottom: .22rem;
            text-transform: uppercase;
        }

        .hero-title {
            font-size: 1.7rem;
            font-weight: 820;
            line-height: 1.16;
            margin: 0 0 .25rem 0;
        }

        .muted {
            color: var(--muted);
        }

        .hero-copy {
            color: var(--muted);
            font-size: .92rem;
            margin: 0;
            max-width: 820px;
        }

        .class-pills {
            display: flex;
            flex-wrap: wrap;
            gap: .35rem;
            margin-top: .65rem;
        }

        .pill {
            background: var(--fresh-soft);
            border: 1px solid var(--fresh-line);
            border-radius: 999px;
            color: #14532d;
            font-size: .72rem;
            font-weight: 700;
            padding: .18rem .48rem;
        }

        .hero-side {
            background: var(--surface-soft);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: .75rem;
        }

        .hero-stat {
            border-bottom: 1px solid #d5ded8;
            padding: .35rem 0;
        }

        .hero-stat:first-child {
            padding-top: 0;
        }

        .hero-stat:last-child {
            border-bottom: 0;
            padding-bottom: 0;
        }

        .hero-stat strong {
            display: block;
            font-size: .9rem;
        }

        .hero-stat span {
            color: var(--muted);
            font-size: .74rem;
        }

        .section-head {
            align-items: flex-start;
            display: flex;
            gap: .75rem;
            justify-content: space-between;
            margin-bottom: .7rem;
        }

        .section-title {
            font-size: 1.08rem;
            font-weight: 820;
            margin: .05rem 0 .08rem 0;
        }

        .section-copy {
            color: var(--muted);
            font-size: .86rem;
            margin: 0;
        }

        .step-badge {
            background: #dff0e5;
            border: 1px solid var(--fresh-line);
            border-radius: 999px;
            color: #14532d;
            flex: 0 0 auto;
            font-size: .7rem;
            font-weight: 800;
            padding: .18rem .52rem;
        }

        .empty-state {
            align-items: center;
            background: transparent;
            border: 0;
            color: var(--muted);
            display: flex;
            justify-content: center;
            min-height: 92px;
            padding: .75rem .25rem;
            text-align: center;
        }

        .selected-note {
            color: var(--muted);
            font-size: .78rem;
            margin: .55rem 0 .35rem 0;
        }

        .camera-queue-head {
            align-items: center;
            display: flex;
            gap: .75rem;
            justify-content: space-between;
            margin: .65rem 0 .45rem 0;
        }

        .camera-queue-title {
            color: var(--ink);
            font-size: .9rem;
            font-weight: 820;
        }

        .camera-queue-count {
            color: var(--muted);
            font-size: .76rem;
            margin-top: .08rem;
        }

        .thumb-wrap div[data-testid="stImage"] img {
            aspect-ratio: 1 / 1;
            border-radius: 7px;
            object-fit: cover;
            width: 100%;
        }

        .camera-thumb-title {
            color: var(--muted);
            font-size: .72rem;
            font-weight: 760;
            margin-bottom: .35rem;
            text-transform: uppercase;
        }

        .summary-grid {
            display: grid;
            gap: .55rem;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            margin-bottom: .75rem;
        }

        .summary-card {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: .68rem;
        }

        .summary-value {
            color: var(--ink);
            font-size: 1.25rem;
            font-weight: 850;
            line-height: 1;
        }

        .summary-label {
            color: var(--muted);
            font-size: .72rem;
            margin-top: .24rem;
        }

        .recommend-card {
            background: var(--blue-soft);
            border: 1px solid #b8cce0;
            border-radius: 8px;
            margin-bottom: .8rem;
            padding: .8rem;
        }

        .recommend-card.no-buy {
            background: var(--rotten-soft);
            border-color: var(--rotten-line);
        }

        .small-label {
            color: var(--muted);
            font-size: .72rem;
            font-weight: 760;
            letter-spacing: .04em;
            text-transform: uppercase;
        }

        .recommend-title {
            color: var(--ink);
            font-size: 1.05rem;
            font-weight: 840;
            line-height: 1.2;
            margin-top: .16rem;
        }

        .candidate-card {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            margin-bottom: .75rem;
            overflow: hidden;
        }

        .candidate-fresh {
            border-color: var(--fresh-line);
        }

        .candidate-rotten {
            border-color: var(--rotten-line);
        }

        .candidate-top {
            background: #ffffff;
            border-bottom: 1px solid var(--line);
            padding: .75rem .8rem .65rem .8rem;
        }

        .candidate-fresh .candidate-top {
            background: linear-gradient(180deg, #ffffff 0, #f3fbf6 100%);
            border-bottom-color: var(--fresh-line);
        }

        .candidate-rotten .candidate-top {
            background: linear-gradient(180deg, #ffffff 0, #fff7f4 100%);
            border-bottom-color: var(--rotten-line);
        }

        .candidate-meta {
            align-items: center;
            display: flex;
            gap: .55rem;
            justify-content: space-between;
            margin-bottom: .3rem;
        }

        .candidate-source {
            color: var(--muted);
            font-size: .72rem;
            font-weight: 760;
            letter-spacing: .04em;
            overflow: hidden;
            text-overflow: ellipsis;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .status-chip {
            border-radius: 999px;
            flex: 0 0 auto;
            font-size: .7rem;
            font-weight: 820;
            padding: .16rem .48rem;
        }

        .status-fresh {
            background: var(--fresh-soft);
            border: 1px solid var(--fresh-line);
            color: var(--fresh);
        }

        .status-rotten {
            background: var(--rotten-soft);
            border: 1px solid var(--rotten-line);
            color: var(--rotten);
        }

        .prediction-name {
            font-size: 1.2rem;
            font-weight: 850;
            line-height: 1.12;
            margin: .1rem 0 .16rem 0;
        }

        .confidence-line {
            color: var(--muted);
            font-size: .84rem;
            margin-bottom: .28rem;
        }

        .confidence-rail {
            background: #e9efe9;
            border-radius: 999px;
            height: 7px;
            margin-top: .48rem;
            overflow: hidden;
        }

        .confidence-fill {
            background: var(--fresh);
            height: 7px;
        }

        .candidate-rotten .confidence-fill {
            background: var(--rotten);
        }

        .action-good,
        .action-avoid {
            font-size: .88rem;
            font-weight: 820;
            margin-top: .28rem;
        }

        .action-good {
            color: var(--fresh);
        }

        .action-avoid {
            color: var(--rotten);
        }

        .prob-row {
            margin-top: .42rem;
        }

        .prob-list {
            padding: .28rem .8rem .78rem .8rem;
        }

        .prob-head {
            display: flex;
            gap: .7rem;
            justify-content: space-between;
            margin-bottom: .16rem;
        }

        .prob-name,
        .prob-value {
            font-size: .78rem;
        }

        .prob-name {
            color: var(--ink);
            font-weight: 700;
        }

        .prob-value {
            color: var(--muted);
            font-variant-numeric: tabular-nums;
        }

        .prob-track {
            background: #edf2ee;
            border-radius: 999px;
            height: 6px;
            overflow: hidden;
        }

        .prob-fill {
            background: var(--fresh);
            height: 6px;
        }

        .prob-fill.rotten {
            background: var(--rotten);
        }

        .stFileUploader,
        .stCameraInput {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: .55rem;
        }

        @media (max-width: 820px) {
            .hero {
                grid-template-columns: 1fr;
            }

            .summary-grid {
                grid-template-columns: 1fr;
            }

            .section-head {
                display: block;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
