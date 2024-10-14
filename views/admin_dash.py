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
        
      
        st.write("Distribuição de Status")
        fig_donut = px.pie(status_df, values='Quantidade', names='Status', hole=0.4, title='Distribuição de Status', color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_donut)

    # URLs por Nível de Risco
    st.subheader("URLs por Nível de Risco")
    risco_data = execute_query(queries.get_url_nivel_risco())
    if risco_data:
        risco_df = pd.DataFrame(risco_data, columns=["Nível de Risco", "Quantidade"])

        
        st.write("URLs por Nível de Risco")
        fig_risco_scatter = px.scatter(risco_df, x='Nível de Risco', y='Quantidade', size='Quantidade', color='Nível de Risco', title='URLs por Nível de Risco', color_discrete_sequence=px.colors.sequential.YlGn)
        st.plotly_chart(fig_risco_scatter)

    # Usuários Ativos/Inativos
    st.subheader("Usuários Ativos e Inativos")
    usuarios_data = execute_query(queries.get_usuarios_ativos_inativos())
    if usuarios_data:
        usuarios_df = pd.DataFrame(usuarios_data, columns=["Status", "Quantidade"])
        
        
        st.write("Distribuição de Usuários")
        fig_usuarios_pizza = px.pie(usuarios_df, values='Quantidade', names='Status', title='Distribuição de Usuários', color_discrete_sequence=px.colors.sequential.Viridis)
        st.plotly_chart(fig_usuarios_pizza)

    # Total de Análises por Usuário
    st.subheader("Total de Análises por Usuário")
    usuario_data = execute_query(queries.get_total_analise_usuario())
    if usuario_data:
        usuario_df = pd.DataFrame(usuario_data, columns=["Usuário", "Quantidade"])
        
        
        st.write("Análise por Usuário")
        fig_bubble = px.scatter(usuario_df, x='Usuário', y='Quantidade', size='Quantidade', color='Usuário', title='Análise por Usuário', color_discrete_sequence=px.colors.sequential.Cividis)
        st.plotly_chart(fig_bubble)

    # Gráfico: Usuário por Função
    st.subheader("Usuário por Função")
    usuario_funcao_data = execute_query(queries.get_usuario_por_funcao())
    if usuario_funcao_data:
        usuario_funcao_df = pd.DataFrame(usuario_funcao_data, columns=["Usuário", "Função"])
        
      
        st.write("Função por Usuário")
        fig_funcao = px.histogram(usuario_funcao_df, x='Função', color='Usuário', title='Funções por Usuário', barmode='group', color_discrete_sequence=px.colors.sequential.Blugrn)
        st.plotly_chart(fig_funcao)

   # Gráfico: Análise por Usuário
    st.subheader("Análise por Usuário")
    analise_usuario_data = execute_query(queries.get_analise_por_usuario())
    if analise_usuario_data:
        analise_usuario_df = pd.DataFrame(analise_usuario_data, columns=["Descrição", "Usuário"])
        
        st.write("Análise por Usuário")
        fig_treemap = px.treemap(
            analise_usuario_df, 
            path=['Usuário', 'Descrição'], 
            title='Análise por Usuário', 
            color='Usuário', 
            color_discrete_sequence=px.colors.sequential.Rainbow
        )

       
        fig_treemap.update_layout(
            margin=dict(t=50, l=25, r=25, b=25),  
            height=800,  
            width=800,   
            uniformtext=dict(minsize=10, mode='hide')  
        )

        # Exibir o gráfico
        st.plotly_chart(fig_treemap)


if __name__ == "__main__":
    admin_dash()
