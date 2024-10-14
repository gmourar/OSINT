import streamlit as st
import pandas as pd
import plotly.express as px
from queries import UserQueries
from db_config import get_connection

def execute_query(query, params=None):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            st.error(f"Erro ao executar a consulta: {e}")
        finally:
            conn.close()
    return []

def user_dash(email, id_user, user_name):
    st.header("Painel do Usuário")
    st.write(f"Bem-vindo(a), {user_name}. Acompanhe suas análises e relatórios.")

    queries = UserQueries(id_user)


    
    analises_data = execute_query(queries.get_analise_osint(), (id_user,))
    if analises_data:
        df_analises = pd.DataFrame(analises_data, columns=['Descricao', 'Status', 'Data_Inicio'])
        contagem_status = df_analises['Status'].value_counts().reset_index()
        contagem_status.columns = ['Status', 'Total']

        fig_analises = px.bar(contagem_status, x='Status', y='Total', title=f'Análises OSINT - {user_name}')
    else:
        fig_analises = None

    # Gráfico: total de análises
    status_data = execute_query(queries.get_analise_por_status())
    if status_data:
        df_status = pd.DataFrame(status_data, columns=['Status', 'Total'])
        fig_status = px.bar(df_status, x='Status', y='Total', title='Total Análises - STATUS')
    else:
        fig_status = None


    # Gráfico: Análises por Usuário
    usuario_data = execute_query(queries.get_analise_por_usuario(), (id_user,))
    if usuario_data:
        df_usuario = pd.DataFrame(usuario_data, columns=['Nome', 'Total_Analises', 'Usuario_Status'])

        # destacar o usuario atual
        df_usuario['Destaque'] = df_usuario['Usuario_Status'].apply(lambda x: 'Atual' if x == 'atual' else 'Outro')

        fig_usuario = px.bar(df_usuario, x='Nome', y='Total_Analises', 
                              title='Total de Análises por Usuário',
                              color='Destaque', 
                              color_discrete_map={'Atual': 'blue', 'Outro': 'gray'})
    else:
        fig_usuario = None

    
    col1, col2 = st.columns(2)
    if fig_status:
        with col1:
            st.plotly_chart(fig_status)
    else:
        with col1:
            st.write("Nenhuma análise encontrada.")

    if fig_analises:
        with col2:
            st.plotly_chart(fig_analises)
    else:
        with col2:
            st.write("Nenhuma análise encontrada para o usuário.")

    # Gráfico: Eventos de Segurança
    st.subheader("Eventos de Segurança")
    eventos_data = execute_query(queries.get_eventos_seguranca())
    if eventos_data:
        df_eventos = pd.DataFrame(eventos_data, columns=['Descricao', 'Nivel_Seguranca', 'Acao_Tomada'])
        contagem_nivel_seguranca = df_eventos['Nivel_Seguranca'].value_counts().reset_index()
        contagem_nivel_seguranca.columns = ['Nivel_Seguranca', 'Total']

        # Gráfico de barras para eventos de segurança
        fig_eventos_barras = px.bar(contagem_nivel_seguranca, x='Nivel_Seguranca', y='Total', title='Distribuição de Níveis de Segurança', color='Nivel_Seguranca')


        # Gráfico de pizza para eventos de segurança
        fig_eventos_pizza = px.pie(contagem_nivel_seguranca, names='Nivel_Seguranca', values='Total', title='Distribuição de Níveis de Segurança')
        
      
        col3, col4 = st.columns(2)
        if fig_usuario:
            with col3:
                st.plotly_chart(fig_usuario)
        else:
            st.write("Nenhuma análise encontrada para o usuário.")
        with col4:
            #st.plotly_chart(fig_eventos_pizza)
            st.plotly_chart(fig_eventos_barras)
    else:
        st.write("Nenhum evento de segurança encontrado.")

