# queries.py

class AdminQueries:
    def __init__(self):
        # Consulta para contar o número de análises por status (por exemplo, ativo, inativo)
        self.analise_por_status = '''
            SELECT status, COUNT(*) AS quantidade
            FROM osint.analise_osint
            GROUP BY status;
        '''
        
        # Consulta para contar o número de URLs por nível de risco (por exemplo, alto, médio, baixo)
        self.url_por_nivel_risco = '''
            SELECT nivel_risco, COUNT(*) AS quantidade
            FROM osint.urls_tor
            GROUP BY nivel_risco;
        '''
        
        # Consulta para contar o número de usuários ativos e inativos
        self.usuarios_ativos_inativos = '''
            SELECT status, COUNT(*) AS quantidade
            FROM osint.usuarios
            GROUP BY status;
        '''
        
        # Consulta para contar o número de análises realizadas por cada usuário
        self.total_analise_por_usuario = '''
            SELECT u.nome, COUNT(a.id_analise) AS quantidade
            FROM osint.analise_osint a
            JOIN osint.usuarios u ON a.id_usuario = u.id_usuario
            GROUP BY u.nome;
        '''


        self.usuario_por_funcao = '''
            SELECT u.nome, r.nome_role
            FROM osint.usuarios u
            JOIN osint.roles r ON u.id_role = r.id_role;

        '''

        self.analise_por_usuario = '''
          SELECT a.descricao, u.nome AS usuario
            FROM osint.analise_osint a
            JOIN osint.usuarios u ON a.id_usuario = u.id_usuario;
        '''

        

       

    def get_analise_status(self):
        """Retorna a consulta para análise por status."""
        return self.analise_por_status
    
    def get_url_nivel_risco(self):
        """Retorna a consulta para contagem de URLs por nível de risco."""
        return self.url_por_nivel_risco
    
    def get_usuarios_ativos_inativos(self):
        """Retorna a consulta para contagem de usuários ativos e inativos."""
        return self.usuarios_ativos_inativos
    
    def get_total_analise_usuario(self):
        """Retorna a consulta para contagem de análises por usuário."""
        return self.total_analise_por_usuario
    
    def get_usuario_por_funcao(self):
        return self.usuario_por_funcao
    
    def get_analise_por_usuario(self):
        return self.analise_por_usuario



class UserQueries:
    def __init__(self, id_user):
        self.id_user = id_user

        # Consulta para obter descrições, status e datas de início das análises para um usuário específico
        self.analises_osint = '''
            SELECT 
                a.descricao,
                a.status,
                a.data_inicio
            FROM osint.analise_osint a
            WHERE a.id_usuario = %s;
        '''
       
        # Consulta para contar o número de análises por usuário, destacando o usuário atual
        self.analise_por_usuario = '''
             SELECT 
                u.nome, 
                COUNT(a.id_analise) AS total_analises,
                CASE 
                    WHEN u.id_usuario = %s THEN 'atual' 
                    ELSE 'outro' 
                END AS usuario_status
            FROM osint.usuarios u
            LEFT JOIN osint.analise_osint a ON u.id_usuario = a.id_usuario
            GROUP BY u.id_usuario, u.nome
            ORDER BY u.nome;
        '''
        
        # Consulta para contar o número de análises por status (por exemplo, ativo, inativo)
        self.contagem_analises_por_status = '''
            SELECT 
                status,
                COUNT(*) AS total
            FROM osint.analise_osint
            GROUP BY status;
        '''

        # Consulta para obter descrições e níveis de segurança de eventos
        self.eventos_seguranca = '''
            SELECT descricao ,
            nivel_seguranca,
            acao_tomada
            FROM osint.eventos_seguranca
            '''
       
    def get_analise_osint(self):
        """Retorna a consulta para obter análises OSINT de um usuário específico."""
        return self.analises_osint
    
    def get_analise_por_usuario(self):
        """Retorna a consulta para contar análises por usuário, destacando o usuário atual."""
        return self.analise_por_usuario
    
    def get_analise_por_status(self):
        """Retorna a consulta para contagem de análises por status."""
        return self.contagem_analises_por_status
    
    def get_eventos_seguranca(self):
        """Retorna a consulta para obter informações sobre eventos de segurança."""
        return self.eventos_seguranca
