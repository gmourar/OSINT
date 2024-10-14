
import streamlit as st
import pandas as pd
import plotly.express as px
from queries import AdminQueries
from db_config import get_connection

queries = AdminQueries()

def execute_query(query):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")
        finally:
            conn.close()
    return []

def admin_dash():
    st.header("Painel de Administração")

    # Análise por Status
    st.subheader("Análise por Status")
    status_data = execute_query(queries.get_analise_status())
    if status_data:
        status_df = pd.DataFrame(status_data, columns=["Status", "Quantidade"])
        
        # Criando colunas para gráficos lado a lado
        col1, col2 = st.columns(2)

        with col1:
            st.write("Distribuição de Status")
            fig_pizza = px.pie(status_df, values='Quantidade', names='Status', title='Distribuição de Status', color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig_pizza)

        with col2:
            st.write("Status em Números")
            fig_bar = px.bar(status_df, x='Status', y='Quantidade', title='Quantidade por Status', color='Quantidade', color_continuous_scale=px.colors.sequential.Blugrn)
            st.plotly_chart(fig_bar)

    # URLs por Nível de Risco
    st.subheader("URLs por Nível de Risco")
    risco_data = execute_query(queries.get_url_nivel_risco())
    if risco_data:
        risco_df = pd.DataFrame(risco_data, columns=["Nível de Risco", "Quantidade"])
        
        st.write("URLs por Nível de Risco")
        fig_risco = px.bar(risco_df, y='Nível de Risco', x='Quantidade', orientation='h', title='URLs por Nível de Risco', color='Quantidade', color_continuous_scale=px.colors.sequential.YlGn)
        st.plotly_chart(fig_risco)

    # Usuários Ativos/Inativos
    st.subheader("Usuários Ativos e Inativos")
    usuarios_data = execute_query(queries.get_usuarios_ativos_inativos())
    if usuarios_data:
        usuarios_df = pd.DataFrame(usuarios_data, columns=["Status", "Quantidade"])
        
        col3, col4 = st.columns(2)

        with col3:
            st.write("Atividade dos Usuários")
            fig_usuarios = px.bar(usuarios_df, x='Status', y='Quantidade', title='Usuários Ativos e Inativos', color='Quantidade', color_continuous_scale=px.colors.sequential.Plasma)
            st.plotly_chart(fig_usuarios)

        with col4:
            st.write("Distribuição de Usuários")
            fig_usuarios_pizza = px.pie(usuarios_df, values='Quantidade', names='Status', title='Distribuição de Usuários', color_discrete_sequence=px.colors.sequential.Viridis)
            st.plotly_chart(fig_usuarios_pizza)

    # Análise por Usuário
    st.subheader("Análise por Usuário")
    usuario_data = execute_query(queries.get_analise_usuario())
    if usuario_data:
        usuario_df = pd.DataFrame(usuario_data, columns=["Usuário", "Quantidade"])
        
        st.write("Análise por Usuário")
        fig_usuario_line = px.line(usuario_df, x='Usuário', y='Quantidade', title='Análise por Usuário', markers=True, line_shape='linear', color='Quantidade', color_discrete_sequence=px.colors.sequential.Cividis)
        st.plotly_chart(fig_usuario_line)

if __name__ == "__main__":
    admin_dash()
