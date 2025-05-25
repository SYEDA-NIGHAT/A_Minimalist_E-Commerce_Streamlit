import streamlit as st

st.title("💳 Checkout")

if "cart" not in st.session_state or not st.session_state.cart:
    st.info("🛒 Your cart is empty. Please add items before checking out.")
    st.stop()

# --- Cart Summary ---
st.subheader("🧾 Order Summary")
total = 0
for item in st.session_state.cart:
    st.write(f"- {item['name']} - ${item['price']}")
    total += item["price"]
st.write(f"### Total: ${round(total, 2)}")

# --- Billing Info Form ---
st.markdown("---")
st.subheader("📋 Billing Information")

with st.form("billing_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    address = st.text_area("Shipping Address")
    city = st.text_input("City")
    zip_code = st.text_input("Zip Code")
    payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "Cash on Delivery"])
    submitted = st.form_submit_button("✅ Confirm Order")

if submitted:
    if not name or not email or not address:
        st.error("Please fill in all the required fields.")
    else:
        st.success(f"🎉 Thank you, {name}! Your order has been placed.")
        st.balloons()
        st.session_state.cart.clear()
        st.write("You will receive a confirmation email shortly.")