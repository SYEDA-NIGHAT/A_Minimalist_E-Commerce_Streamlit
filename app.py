import streamlit as st
import json

st.set_page_config(page_title="My Shop", layout="centered")

st.title("🛒 Welcome to My E-Commerce App")
st.write("Use the sidebar to navigate between pages.")

# --- About Us ---
st.markdown("---")
st.header("📢 About Us")
st.write("""
Welcome to **My Shop** – your one-stop store for quality tech accessories at unbeatable prices.
We are passionate about bringing you the best products with the best service.

- ✅ Trusted by 1000+ customers  
- 🚚 Fast delivery  
- 💬 24/7 support  
""")

# --- Featured Products Slider ---
st.markdown("---")
st.header("📦 Featured Products")

# Load products
with open("data/products.json") as f:
    products = json.load(f)

# Use specific products as featured (not the first few)
featured = [products[4], products[6], products[7]]  # Example: Headphones, SSD, Speaker

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

product = featured[st.session_state.slide_index]
st.subheader(product["name"])
st.write(product["description"])
st.write(f"**Price:** ${product['price']}")

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Previous"):
        st.session_state.slide_index = (st.session_state.slide_index - 1) % len(featured)
with col3:
    if st.button("Next ➡️"):
        st.session_state.slide_index = (st.session_state.slide_index + 1) % len(featured)
