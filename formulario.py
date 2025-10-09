from pessoa import Pessoa
from db import inicializar_banco, inserir_beneficiario, listar_beneficiarios

# Inicializa o banco se ainda não existir
inicializar_banco()

while True:
    print("\nDECLARAÇÃO ELETRÔNICA E DEMAIS MEIOS DE CONTATO")
    print("1 - Cadastrar nova pessoa")
    print("2 - Listar pessoas cadastradas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome completo: ").strip().capitalize()
        filiacao1 = input("Filiação 1: ").strip().capitalize()
        filiacao2 = input("Filiação 2: ").strip().capitalize()
        cpf = input("CPF (Quando disponível): ").strip()
        data_nasc = input("Data de nascimento (AAAA-MM-DD): ").strip()
        doc_identidade = input("Documento de identidade: ").strip()
        nacionalidade = input("Nacionalidade: ").strip()
        telefone = input("Telefone (apenas números): ").strip()
        email = input("E-mail: ").strip()
        endereco_residencial = input("Endereço residencial: ").strip()
        endereco_trabalho = input("Endereço do trabalho: ").strip()

        p = Pessoa(nome, filiacao1, filiacao2, data_nasc, doc_identidade,
                   nacionalidade, telefone, email,
                   endereco_residencial, endereco_trabalho, cpf)

        try:
            id_gerado = inserir_beneficiario(p)
            print(f"\n Pessoa {p.nome} cadastrada com sucesso (ID {id_gerado})")
        except Exception as e:
            print(f" Erro ao cadastrar: {e}")

    elif opcao == "2":
        beneficiarios = listar_beneficiarios()
        if not beneficiarios:
            print("\n Nenhuma pessoa cadastrada.")
        else:
            print("\n Pessoas cadastradas no banco:")
            for i, (id_benef, nome, cpf, data_nasc) in enumerate(beneficiarios, 1):
                print(f"{i}. ID: {id_benef} | Nome: {nome} | CPF: {cpf} | Nasc: {data_nasc}")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")
