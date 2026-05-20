import streamlit as st


def initialize_state():
    if "camera_candidates" not in st.session_state:
        st.session_state.camera_candidates = []
    if "upload_reset_version" not in st.session_state:
        st.session_state.upload_reset_version = 0


def reset_uploads():
    st.session_state.upload_reset_version += 1


def add_camera_candidate(data):
    st.session_state.camera_candidates.append(data)


def clear_camera_candidates():
    st.session_state.camera_candidates = []


def remove_camera_candidate(index):
    if 0 <= index < len(st.session_state.camera_candidates):
        del st.session_state.camera_candidates[index]
