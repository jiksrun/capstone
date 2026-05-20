from io import BytesIO

import streamlit as st
from PIL import Image, ImageOps

from src.app_state import add_camera_candidate, clear_camera_candidates, remove_camera_candidate, reset_uploads
from src.ui.layout import render_section_header


def image_from_bytes(data):
    return Image.open(BytesIO(data)).convert("RGB")


def thumbnail_image(image, size=180):
    return ImageOps.fit(image.convert("RGB"), (size, size), method=Image.Resampling.LANCZOS)


def get_input_candidates():
    render_section_header(
        "Step 1",
        "Add fruit images",
        "Use the uploader for batches, or add camera captures one at a time.",
    )

    input_mode = st.radio("Image source", ["Upload", "Camera compare"], horizontal=True)
    candidates = []

    if input_mode == "Upload":
        uploaded_files = st.file_uploader(
            "Choose JPG or PNG files",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key=f"uploaded-files-{st.session_state.upload_reset_version}",
        )
        for index, uploaded_file in enumerate(uploaded_files or [], start=1):
            data = uploaded_file.getvalue()
            candidates.append(
                {
                    "kind": "upload",
                    "name": f"Upload {index}",
                    "source": uploaded_file.name,
                    "image": image_from_bytes(data),
                }
            )

        if uploaded_files and st.button("Delete all imported files", width="stretch"):
            reset_uploads()
            st.rerun()
    else:
        camera_file = st.camera_input("Take a photo")
        if camera_file is not None and st.button("Add capture to comparison", type="primary"):
            add_camera_candidate(camera_file.getvalue())
            st.rerun()

        if st.session_state.camera_candidates:
            render_camera_queue_header(len(st.session_state.camera_candidates))

        for index, data in enumerate(st.session_state.camera_candidates, start=1):
            candidates.append(
                {
                    "kind": "camera",
                    "camera_index": index - 1,
                    "name": f"Camera {index}",
                    "source": "Camera capture",
                    "image": image_from_bytes(data),
                }
            )

    if candidates:
        st.markdown(f'<div class="selected-note">{len(candidates)} image(s) selected</div>', unsafe_allow_html=True)
        render_preview_grid(candidates)

    return candidates


def render_camera_queue_header(count):
    st.markdown(
        f"""
        <div class="camera-queue-head">
            <div>
                <div class="camera-queue-title">Camera queue</div>
                <div class="camera-queue-count">{count} capture(s) ready for comparison</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Clear all camera captures", width="stretch"):
        clear_camera_candidates()
        st.rerun()


def render_preview_grid(candidates):
    st.markdown('<div class="thumb-wrap">', unsafe_allow_html=True)
    for start in range(0, len(candidates), 3):
        row = candidates[start : start + 3]
        cols = st.columns(3)
        for index, candidate in enumerate(row):
            with cols[index]:
                render_preview_card(candidate)
    st.markdown("</div>", unsafe_allow_html=True)


def render_preview_card(candidate):
    if candidate.get("kind") != "camera":
        with st.container(border=True):
            st.image(thumbnail_image(candidate["image"], 132), caption=candidate["name"], width="stretch")
        return

    with st.container(border=True):
        st.markdown(f'<div class="camera-thumb-title">{candidate["name"]}</div>', unsafe_allow_html=True)
        st.image(thumbnail_image(candidate["image"], 132), width="stretch")
        if st.button("Remove", key=f"remove-camera-{candidate['camera_index']}", width="stretch"):
            remove_camera_candidate(candidate["camera_index"])
            st.rerun()
