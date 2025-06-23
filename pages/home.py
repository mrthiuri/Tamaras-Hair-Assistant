import streamlit as st

st.markdown("""
    <div style='text-align: center; font-family: "Playfair Display", serif; font-size: 64px; color: #003366;'>Tamara's Hair</div>
""", unsafe_allow_html=True)

# Sub-heading
st.markdown("""
    <div style='text-align: center; font-family: "Playfair Display", serif; font-size: 28px; color: #4B0082;'>Premium Haircare for African Hair Beauty</div>
""", unsafe_allow_html=True)

# Hero Image
st.markdown(
    "<div style='text-align: center;'>"
    "<img src='https://raw.githubusercontent.com/mrthiuri/Tamaras-Hair-AI-Assistant/main/Logo.png'"
    "style='width:70%; border-radius:20px;'>"
    "</div>",
    unsafe_allow_html=True
)

# About Section
st.markdown("""
    <div style='margin-top: 40px; font-size: 18px; font-family: Arial, sans-serif;'>
        <p><strong>Tamara’s Hair</strong> is a premium haircare brand specializing in products and services tailored for African hair, with a primary focus on Black women’s hair needs.</p>
        <p>Located along <strong>Moi Avenue, Kilele Mall, Nairobi</strong>, the business offers a curated range of high-quality haircare products including <em>shampoos</em>, <em>conditioners</em>, <em>detanglers</em>, <em>scalp oils</em>, and <em>hair mousses</em>.</p>
        <p>What sets <strong>Tamara’s Hair</strong> apart is its personalized product recommendation service, where clients undergo simple hair tests to determine the most suitable products for their unique hair type and condition. The brand is committed to celebrating and nurturing natural hair textures, providing solutions designed to moisturize, strengthen, and enhance the natural beauty of African hair.</p>
    </div>
""", unsafe_allow_html=True)

# Call to Action / Visit Us Section
st.markdown("""
    <div style='margin-top: 40px; text-align: center;'>
        <h4 style='font-family: "Playfair Display", serif; color: #4B0082;'>Visit Us Today at Moi Avenue, Kilele Mall, Nairobi 💖</h4>
        <a href='/Elsy' target = '_self' style='background-color: #003366; color: white; padding: 10px 25px; text-decoration: none; border-radius: 5px; font-size: 18px;'>Chat with Elsa👽</a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style='margin-top:50px;'>
    <div style='text-align: center; font-size: 14px; color: gray;'>
        &copy; 2025 Tamara's Hair. All rights reserved.
    </div>
""", unsafe_allow_html=True)