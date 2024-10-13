import streamlit as st
from auth import authenticate_user, is_admin, logout
from views.admin_dash import admin_dash
from views.user_dash import user_dash
from db_config import testar_conn

st.title('OSINT Dashboard')

if 'user' not in st.session_state:
    user = st.text_input("Email")
    password = st.text_input("Senha", type="password")
    
    if st.button("Login"):
        if authenticate_user(user, password):
            st.success("Login bem-sucedido!")
        else:
            st.error("Login falhou. Verifique suas credenciais.")

    st.button('Testar conexao' , on_click= testar_conn)


        
else:
    user = st.session_state['user']
    st.sidebar.write(f"Bem-vindo, {user['nome']}")
    
    if is_admin():
        admin_dash()
    else:
        user_dash()
    
    if st.button("Logout"):
        logout()
        st.rerun()

