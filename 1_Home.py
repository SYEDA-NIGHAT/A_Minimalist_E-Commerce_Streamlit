import streamlit as st
import json

with open("data/products.json") as f:
    products = json.load(f)

if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🏠 All Products")

for product in products:
    st.subheader(product["name"])
    st.write(product["description"])
    st.write(f"**Price:** ${product['price']}")
    if st.button(f"Add to Cart {product['id']}"):
        st.session_state.cart.append(product)
        st.success(f"✅ Added {product['name']} to cart!")
