import streamlit as st
import time

st.set_page_config(page_title="Approach Countdown", layout="centered")
st.title("✈️ Approach Countdown Timer")

# --- User Inputs ---
speed = st.number_input("Speed (KIAS)", min_value=1.0, value=120.0, step=1.0)
faf_distance = st.number_input("Distance from FAF (NM)", min_value=0.0, value=5.0, step=0.1)
map_distance = st.number_input("FAF → MAP Distance (NM)", min_value=0.0, value=5.5, step=0.1)

# Countdown control
countdown_placeholder = st.empty()
stop_flag = st.session_state.get("stop_flag", False)

def start_countdown():
    st.session_state.stop_flag = False
    interval_sec = 360 / speed  # Convert KIAS to interval
    current = faf_distance
    restarted = False

    while True:
        if st.session_state.stop_flag:
            countdown_placeholder.markdown("⏹ Countdown Stopped")
            break

        countdown_placeholder.markdown(f"### {current:.1f} NM")
        time.sleep(interval_sec)
        current -= 0.1

        if current < 0:
            if not restarted:
                current = map_distance
                restarted = True
            else:
                countdown_placeholder.markdown("✅ Complete")
                break

# --- Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("Start Countdown"):
        start_countdown()
with col2:
    if st.button("Stop Countdown"):
        st.session_state.stop_flag = True
    