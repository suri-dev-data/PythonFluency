from abc import ABC, abstractmethod

# Estratégia base
class EstrategiaOtimizacao(ABC):
    @abstractmethod
    def calcular_score(self, dados_operacionais: dict) -> float:
        pass


# Factory para instanciar estratégias
strategies : list[EstrategiaOtimizacao] = []

def criar_estrategias(strategy : EstrategiaOtimizacao):
    strategies.append(strategy())
    return strategy


@criar_estrategias
# Estratégias concretas
class AltaPressao(EstrategiaOtimizacao):
    def calcular_score(self, dados):
        return dados["pressao"] * 0.8 - dados["consumo"]
    
@criar_estrategias
class BaixoConsumo(EstrategiaOtimizacao):
    def calcular_score(self, dados):
        return 100 / (dados["consumo"] + 1)
    
@criar_estrategias
class MaxVazao(EstrategiaOtimizacao):
    def calcular_score(self, dados):
        return dados["vazao"] * 1.2 - dados["temperatura"] * 0.5

# Função para escolher a melhor estratégia
def escolher_melhor_estrategia(dados_operacionais):
    melhor = max(strategies, key=lambda e: e.calcular_score(dados_operacionais))
    return melhor


# Simulação de dados operacionais
dados = {
    "pressao": 120,
    "consumo": 30,
    "vazao": 85,
    "temperatura": 60
}

# Escolher e aplicar a melhor estratégia
melhor_estrategia = escolher_melhor_estrategia(dados)
print(f"✅ Melhor estratégia: {melhor_estrategia.__class__.__name__}")
print(f"🔍 Score: {melhor_estrategia.calcular_score(dados):.2f}")

