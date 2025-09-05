class Pessoa:

    nome: str
    filiacao1: str
    filiacao2: str
    data_nasc: str
    doc_identidade: int
    nacionalidade: str
    telefone: str
    email: str
    endereco_residencial: str
    endereco_trabalho: str
    cpf: str | None = None

    def __init__(self, nome, filiacao1, filiacao2, data_nasc, doc_identidade, nacionalidade,telefone, email, endereco_residencial, endereco_trabalho, cpf=None):
        self.nome = nome
        self.filiacao1 = filiacao1
        self.filiacao2 = filiacao2
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.doc_identidade = doc_identidade
        self.nacionalidade = nacionalidade
        self.telefone = telefone
        self.email = email
        self.endereco_residencial = endereco_residencial
        self.endereco_trabalho = endereco_trabalho
    
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data Nasc: {self.data_nasc}"
        
Pessoas = {
    "Pessoas": [],
}

while True:
    print("DECLARAÇÃO ELETRÔNICA E DEMAIS MEIOS DE CONTATO")
    print("1 - Cadastrar nova pessoa")
    print("2 - Listar pessoas cadastradas")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome completo: ").capitalize()
        filiacao1 = input("Filiação 1: ").capitalize()
        filiacao2 = input("Filiação 2: ").capitalize()
        cpf = input("CPF (Quando disponivel): ").capitalize()
        data_nasc = input("Data de nascimento: ").capitalize()
        doc_identidade = input("Documento de identidade: ").capitalize()
        nacionalidade = input("Nacionalidade: ").capitalize()
        telefone = input("Telefones (com DDD): ").capitalize()
        email = input("Endereço eletrônico (E-mail): ").capitalize()
        endereco_residencial = input("Endereço residencial (com CEP): ").capitalize()
        endereco_trabalho = input("Endereço do trabalho (com CEP): ").capitalize()
    
    
        p = Pessoa(nome, filiacao1, filiacao2, data_nasc, doc_identidade, nacionalidade, telefone, email, endereco_residencial, endereco_trabalho, cpf)
        Pessoas["Pessoas"].append(p)
        print(f"\nPessoa {p.nome} cadastrada com sucesso!")

    elif opcao == "2":
        if not Pessoas["Pessoas"]:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("Pessoas cadastradas") 
            for i, pessoa in enumerate(Pessoas["Pessoas"], 1):
                print(f"{i}. {pessoa}")

    elif opcao == "0":
        break

