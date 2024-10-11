import hashlib
import streamlit as st
from db_config import get_user_by_email

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password):
    user = get_user_by_email(email)
    if user and user['senha_hash'] == hash_password(password):
        return user
    return None

def authenticate_user(email, password):
    user = login(email, password)
    if user:
        st.session_state['user'] = user
        return True
    return False

def is_admin():
    return st.session_state.get('user', {}).get('id_role') == 1  # Role ID 1 = Admin

def logout():
    st.session_state.pop('user', None)
