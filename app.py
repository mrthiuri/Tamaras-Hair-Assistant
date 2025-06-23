import streamlit as st

main_page = st.Page(page="pages/home.py", icon="🏠", title="Home")
chatbot_page = st.Page(page="pages/Elsy.py",title="AI Assistant",icon="👽")
pg = st.navigation([main_page,chatbot_page])
pg.run()