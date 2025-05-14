import streamlit as st
from PIL import Image
import numpy as np
from streamlit_drawable_canvas import st_canvas

st.title("🖼️ Canvas Test")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.write("Image shape:", image_np.shape)

    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",
        stroke_width=0,
        image_data=image_np,
        update_streamlit=True,
        height=image_np.shape[0],
        width=image_np.shape[1],
        drawing_mode="point",
        point_display_radius=5,
        key="canvas"
    )
