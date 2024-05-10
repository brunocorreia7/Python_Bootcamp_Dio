def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Exemplo de uso:
consumo = float(input("Digite o consumo médio mensal de dados em GB: "))
plano_recomendado = recomendar_plano(consumo)
print("O plano ideal para você é:", plano_recomendado)
