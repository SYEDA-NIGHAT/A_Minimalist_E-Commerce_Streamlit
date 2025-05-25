import streamlit as st

st.title("🛍️ Your Cart")

if "cart" not in st.session_state or not st.session_state.cart:
    st.info("Your cart is empty.")
else:
    total = 0
    for i, item in enumerate(st.session_state.cart):
        st.write(f"{i+1}. {item['name']} - ${item['price']}")
        total += item["price"]
    st.write(f"### Total: ${round(total, 2)}")
