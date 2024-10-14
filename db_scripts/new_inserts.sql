
INSERT INTO osint.urls_tor (id_url, url, data_coleta, conteudo_bruto, nivel_risco) VALUES
(gen_random_uuid(), 'http://exemplo.tor', CURRENT_TIMESTAMP, 'Conteúdo da página Tor 1', 'Alto'),
(gen_random_uuid(), 'http://teste.tor', CURRENT_TIMESTAMP, 'Conteúdo da página Tor 2', 'Médio'),
(gen_random_uuid(), 'http://projetos.tor', CURRENT_TIMESTAMP, 'Conteúdo da página Tor 3', 'Baixo'),
(gen_random_uuid(), 'http://dados.tor', CURRENT_TIMESTAMP, 'Conteúdo da página Tor 4', 'Alto'),
(gen_random_uuid(), 'http://seguranca.tor', CURRENT_TIMESTAMP, 'Conteúdo da página Tor 5', 'Médio');

INSERT INTO osint.analise_osint (id_analise, id_usuario, descricao, data_inicio, status) VALUES
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Alice'), 'Análise de segurança da URL http://exemplo.tor', CURRENT_TIMESTAMP, 'em andamento'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Bob'), 'Análise de vulnerabilidades da URL https://example.com', CURRENT_TIMESTAMP, 'concluída'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Carol'), 'Análise de conteúdo da URL https://teste.com', CURRENT_TIMESTAMP, 'em andamento'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'David'), 'Análise geral de dados coletados', CURRENT_TIMESTAMP, 'concluída'),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Eve'), 'Análise detalhada de segurança da URL http://seguranca.tor', CURRENT_TIMESTAMP, 'em andamento');

INSERT INTO osint.auditoria_movimentacao (id_dado, ip_origem, acao, data_hora) VALUES
(gen_random_uuid(), '192.168.1.1', 'INSERT', CURRENT_TIMESTAMP),
(gen_random_uuid(), '192.168.1.2', 'UPDATE', CURRENT_TIMESTAMP),
(gen_random_uuid(), '192.168.1.3', 'DELETE', CURRENT_TIMESTAMP),
(gen_random_uuid(), '192.168.1.4', 'INSERT', CURRENT_TIMESTAMP),
(gen_random_uuid(), '192.168.1.5', 'UPDATE', CURRENT_TIMESTAMP);

INSERT INTO osint.comentarios (id_comentario, id_analise, id_usuario, texto, data_criacao) VALUES
(gen_random_uuid(), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise de segurança da URL http://exemplo.tor'), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Bob'), 'Comentário sobre a análise.', CURRENT_TIMESTAMP),
(gen_random_uuid(), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise de vulnerabilidades da URL https://example.com'), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Alice'), 'Muito boa a análise!', CURRENT_TIMESTAMP),
(gen_random_uuid(), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise de conteúdo da URL https://teste.com'), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'David'), 'Precisamos revisar algumas informações.', CURRENT_TIMESTAMP),
(gen_random_uuid(), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise geral de dados coletados'), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Carol'), 'Análise interessante!', CURRENT_TIMESTAMP),
(gen_random_uuid(), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise detalhada de segurança da URL http://seguranca.tor'), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Eve'), 'Ótimo trabalho!', CURRENT_TIMESTAMP);

INSERT INTO osint.relatorios (id_relatorio, id_usuario, id_analise, titulo, conteudo, data_criacao) VALUES
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Alice'), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise de segurança da URL http://exemplo.tor'), 'Relatório de Análise de Segurança', 'Conteúdo do relatório...', CURRENT_TIMESTAMP),
(gen_random_uuid(), (SELECT id_usuario FROM osint.usuarios WHERE nome = 'Bob'), (SELECT id_analise FROM osint.analise_osint WHERE descricao = 'Análise de vulnerabilidades da URL https://example.com'), 'Relatório de Vulnerabilidades', 'Conteúdo do relatório...', CURRENT_TIMESTAMP);

INSERT INTO osint.eventos_seguranca (id_evento, descricao, nivel_seguranca, acao_tomada) VALUES
(gen_random_uuid(), 'Tentativa de acesso não autorizado', 'Alto', 'Bloqueio de IP'),
(gen_random_uuid(), 'Análise de tráfego suspeito', 'Médio', 'Monitoramento contínuo'),
(gen_random_uuid(), 'Falha na análise de dados', 'Baixo', 'Revisão manual'),
(gen_random_uuid(), 'Novo registro de URL na Surface Web', 'Baixo', 'Análise de segurança'),
(gen_random_uuid(), 'Acesso a URL da Tor', 'Alto', 'Investigação detalhada');
