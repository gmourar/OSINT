-- 1. Inserir registros na tabela de Roles
INSERT INTO osint.roles (id_role, nome_role, descricao_role) VALUES
(1, 'admin', 'Administrador do sistema com todas as permissões'),
(2, 'user', 'Usuário comum com permissões limitadas'),
(3, 'analista', 'Usuário com permissões para realizar análises'),
(4, 'moderador', 'Usuário com permissões para moderar conteúdo'),
(5, 'desenvolvedor', 'Usuário responsável pelo desenvolvimento e manutenção do sistema');

-- 2. Inserir registros na tabela de Usuários
INSERT INTO osint.usuarios (id_usuario, nome, email, senha_hash, status, data_criacao, id_role) VALUES
(gen_random_uuid(), 'Alice', 'alice@example.com', 'hash1', 'ativo', CURRENT_TIMESTAMP, 1),
(gen_random_uuid(), 'Bob', 'bob@example.com', 'hash2', 'ativo', CURRENT_TIMESTAMP, 2),
(gen_random_uuid(), 'Carol', 'carol@example.com', 'hash3', 'ativo', CURRENT_TIMESTAMP, 3),
(gen_random_uuid(), 'David', 'david@example.com', 'hash4', 'inativo', CURRENT_TIMESTAMP, 4),
(gen_random_uuid(), 'Eve', 'eve@example.com', 'hash5', 'ativo', CURRENT_TIMESTAMP, 2);

-- 3. Inserir registros na tabela de Permissões
INSERT INTO osint.permissoes (id_permissao, nome_permissao, descricao, id_role) VALUES
(gen_random_uuid(), 'criar_usuario', 'Permissão para criar novos usuários', 1),
(gen_random_uuid(), 'deletar_usuario', 'Permissão para deletar usuários', 1),
(gen_random_uuid(), 'visualizar_analise', 'Permissão para visualizar análises', 2),
(gen_random_uuid(), 'editar_analise', 'Permissão para editar análises', 3),
(gen_random_uuid(), 'gerar_relatorio', 'Permissão para gerar relatórios', 5);

-- 4. Inserir registros na tabela de URLs da Surface Web
INSERT INTO osint.urls_surface (id_url, url, data_coleta, conteudo_bruto, palavras_chave) VALUES
(gen_random_uuid(), 'https://example.com', CURRENT_TIMESTAMP, 'Conteúdo da página 1', ARRAY['exemplo', 'teste']),
(gen_random_uuid(), 'https://teste.com', CURRENT_TIMESTAMP, 'Conteúdo da página 2', ARRAY['teste', 'análise']),
(gen_random_uuid(), 'https://projetos.com', CURRENT_TIMESTAMP, 'Conteúdo da página 3', ARRAY['projetos', 'desenvolvimento']),
(gen_random_uuid(), 'https://dados.com', CURRENT_TIMESTAMP, 'Conteúdo da página 4', ARRAY['dados', 'informação']),
(gen_random_uuid(), 'https://seguranca.com', CURRENT_TIMESTAMP, 'Conteúdo da página 5', ARRAY['segurança', 'proteção']);

-- 5. Inserir registros na tabela de Análise de OSINT
INSERT INTO osint.analise_osint (id_analise, id_usuario, descricao, data_inicio, data_termino, status) VALUES
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Alice'), 'Análise sobre phishing', CURRENT_TIMESTAMP, NULL, 'em andamento'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Bob'), 'Análise sobre dados vazados', CURRENT_TIMESTAMP, NULL, 'em andamento'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Carol'), 'Análise sobre fraudes financeiras', CURRENT_TIMESTAMP, NULL, 'em andamento'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'David'), 'Análise sobre ataques cibernéticos', CURRENT_TIMESTAMP, NULL, 'em andamento'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Eve'), 'Análise sobre redes sociais', CURRENT_TIMESTAMP, NULL, 'em andamento');

-- 6. Inserir registros na tabela de Etiquetas
INSERT INTO osint.etiquetas (id_etiqueta, nome, descricao) VALUES
(gen_random_uuid(), 'Phishing', 'Relativo a tentativas de fraudes digitais'),
(gen_random_uuid(), 'Dados Vazados', 'Refere-se a dados expostos indevidamente'),
(gen_random_uuid(), 'Fraude', 'Relativo a práticas enganosas em finanças'),
(gen_random_uuid(), 'Cibersegurança', 'Refere-se a práticas de segurança digital'),
(gen_random_uuid(), 'Social Media', 'Análise relacionada a redes sociais');

-- 7. Inserir registros na tabela de Análise de Imagens
INSERT INTO osint.analise_imagens (id_imagem, url_imagem, id_analise, data_envio, status_analise, conclusao) VALUES
(gen_random_uuid(), 'https://example.com/imagem1.jpg', (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise sobre phishing'), CURRENT_TIMESTAMP, 'pendente', NULL),
(gen_random_uuid(), 'https://example.com/imagem2.jpg', (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise sobre dados vazados'), CURRENT_TIMESTAMP, 'pendente', NULL),
(gen_random_uuid(), 'https://example.com/imagem3.jpg', (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise sobre fraudes financeiras'), CURRENT_TIMESTAMP, 'pendente', NULL),
(gen_random_uuid(), 'https://example.com/imagem4.jpg', (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise sobre ataques cibernéticos'), CURRENT_TIMESTAMP, 'pendente', NULL),
(gen_random_uuid(), 'https://example.com/imagem5.jpg', (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise sobre redes sociais'), CURRENT_TIMESTAMP, 'pendente', NULL);

-- 8. Inserir registros na tabela de Fontes
INSERT INTO osint.fontes (id_fonte, nome, url, descricao, data_registro) VALUES
(gen_random_uuid(), 'Fonte 1', 'https://fonte1.com', 'Descrição da fonte 1', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'Fonte 2', 'https://fonte2.com', 'Descrição da fonte 2', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'Fonte 3', 'https://fonte3.com', 'Descrição da fonte 3', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'Fonte 4', 'https://fonte4.com', 'Descrição da fonte 4', CURRENT_TIMESTAMP),
(gen_random_uuid(), 'Fonte 5', 'https://fonte5.com', 'Descrição da fonte 5', CURRENT_TIMESTAMP);