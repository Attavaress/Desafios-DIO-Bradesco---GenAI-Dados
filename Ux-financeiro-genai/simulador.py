def simulador_investimento(capital, taxa, tempo):
    """Calcula o montante final com juros compostos."""
    montante = capital * (1 + taxa)**tempo
    return montante

def faq_inteligente(pergunta):
    """Simula uma resposta contextualizada de GenAI."""
    conhecimento = {
        "CDB": "O CDB é como emprestar dinheiro para o banco em troca de juros.",
        "SELIC": "A Taxa Selic é a taxa básica de juros da nossa economia.",
        "DIVERSIFICACAO": "Não colocar todos os ovos na mesma cesta para reduzir riscos."
    }
    
    for chave in conhecimento:
        if chave in pergunta.upper():
            return conhecimento[chave]
    return "Posso pesquisar mais sobre isso para você. O que deseja saber especificamente?"

# Exemplo de interação focada em UX
print("--- Assistente Financeiro B-GenAI ---")
nome = input("Como gostaria de ser chamado? ")
print(f"Olá, {nome}! Vamos planejar seu futuro.")

valor = float(input("Quanto pretende investir inicialmente? "))
# Simulação simples de 10% ao ano por 5 anos
resultado = simulador_investimento(valor, 0.10, 5)

print(f"\n[Análise de UX]: Em 5 anos, seu capital seria de R$ {resultado:.2f}")
print("Dica: Este valor considera uma taxa hipotética de 10% a.a.")
