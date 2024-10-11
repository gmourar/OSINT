import streamlit as st
from auth import authenticate_user, is_admin, logout
from views.admin_dash import admin_dash
from views.user_dash import user_dash

st.title('OSINT Dashboard')

if 'user' not in st.session_state:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if authenticate_user(email, password):
            st.success("Login bem-sucedido!")
        else:
            st.error("Login falhou. Verifique suas credenciais.")
else:
    user = st.session_state['user']
    st.sidebar.write(f"Bem-vindo, {user['nome']}")
    
    if is_admin():
        admin_dash()
    else:
        user_dash()
    
    if st.button("Logout"):
        logout()
        st.experimental_rerun()
