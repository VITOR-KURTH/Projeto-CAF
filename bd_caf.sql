CREATE TABLE beneficiarios (
    id_beneficiario INTEGER PRIMARY KEY,
    nome VARCHAR,
    filiacao1 VARCHAR,
    filiacao2 VARCHAR,
    cpf VARCHAR,
    data_nascimento DATE,
    documento_identidade VARCHAR,
    nacionalidade VARCHAR,
    email VARCHAR
);

CREATE TABLE atendentes (
    id_atendente INTEGER PRIMARY KEY,
    nome VARCHAR
);

CREATE TABLE atendimentos (
    id_atendimento INTEGER PRIMARY KEY,
    data DATE,
    hora TIME,
    observacao VARCHAR,
    fk_beneficiarios_id_beneficiario INTEGER,
    fk_atendentes_id_atendente INTEGER
);

CREATE TABLE telefone (
    id_telefone INTEGER PRIMARY KEY,
    codigo_pais INTEGER,
    ddd INTEGER,
    numero INTEGER,
    descricao VARCHAR,
    fk_beneficiarios_id_beneficiario INTEGER
);

CREATE TABLE cidade (
    nome VARCHAR,
    id_cidade INTEGER PRIMARY KEY,
    fk_estado_id_estado INTEGER
);

CREATE TABLE bairro (
    id_bairro INTEGER PRIMARY KEY,
    nome VARCHAR,
    fk_cidade_id_cidade INTEGER
);

CREATE TABLE endereco (
    numero INTEGER,
    nome_logradouro VARCHAR,
    CEP INTEGER,
    complemento VARCHAR,
    id_endereco INTEGER PRIMARY KEY,
    fk_bairro_id_bairro INTEGER,
    fk_tipo_logradouro_id_tipo_logradouro INTEGER
);

CREATE TABLE pais (
    nome VARCHAR,
    id_pais INTEGER PRIMARY KEY,
    sigla VARCHAR
);

CREATE TABLE estado (
    id_estado INTEGER PRIMARY KEY,
    nome VARCHAR,
    fk_pais_id_pais INTEGER
);

CREATE TABLE tipo_logradouro (
    nome VARCHAR,
    id_tipo_logradouro INTEGER PRIMARY KEY
);

CREATE TABLE endereco_beneficiario_tem (
    tipo_endereco VARCHAR,
    fk_beneficiarios_id_beneficiario INTEGER,
    fk_endereco_id_endereco INTEGER
);
 
ALTER TABLE atendimentos ADD CONSTRAINT FK_atendimentos_2
    FOREIGN KEY (fk_beneficiarios_id_beneficiario)
    REFERENCES beneficiarios (id_beneficiario)
    ON DELETE RESTRICT;
 
ALTER TABLE atendimentos ADD CONSTRAINT FK_atendimentos_3
    FOREIGN KEY (fk_atendentes_id_atendente)
    REFERENCES atendentes (id_atendente)
    ON DELETE RESTRICT;
 
ALTER TABLE telefone ADD CONSTRAINT FK_telefone_2
    FOREIGN KEY (fk_beneficiarios_id_beneficiario)
    REFERENCES beneficiarios (id_beneficiario)
    ON DELETE RESTRICT;
 
ALTER TABLE cidade ADD CONSTRAINT FK_cidade_2
    FOREIGN KEY (fk_estado_id_estado)
    REFERENCES estado (id_estado)
    ON DELETE RESTRICT;
 
ALTER TABLE bairro ADD CONSTRAINT FK_bairro_2
    FOREIGN KEY (fk_cidade_id_cidade)
    REFERENCES cidade (id_cidade)
    ON DELETE RESTRICT;
 
ALTER TABLE endereco ADD CONSTRAINT FK_endereco_2
    FOREIGN KEY (fk_bairro_id_bairro)
    REFERENCES bairro (id_bairro)
    ON DELETE RESTRICT;
 
ALTER TABLE endereco ADD CONSTRAINT FK_endereco_3
    FOREIGN KEY (fk_tipo_logradouro_id_tipo_logradouro)
    REFERENCES tipo_logradouro (id_tipo_logradouro)
    ON DELETE RESTRICT;
 
ALTER TABLE estado ADD CONSTRAINT FK_estado_2
    FOREIGN KEY (fk_pais_id_pais)
    REFERENCES pais (id_pais)
    ON DELETE RESTRICT;
 
ALTER TABLE endereco_beneficiario_tem ADD CONSTRAINT FK_endereco_beneficiario_tem_1
    FOREIGN KEY (fk_beneficiarios_id_beneficiario)
    REFERENCES beneficiarios (id_beneficiario);
 
ALTER TABLE endereco_beneficiario_tem ADD CONSTRAINT FK_endereco_beneficiario_tem_2
    FOREIGN KEY (fk_endereco_id_endereco)
    REFERENCES endereco (id_endereco);