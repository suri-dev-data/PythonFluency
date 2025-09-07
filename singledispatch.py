from functools import singledispatch
from datetime import datetime

@singledispatch
def processar_dado(dado):
    print(f"[GENÉRICO] Tipo não reconhecido: {type(dado).__name__}")

@processar_dado.register(float)
def _(valor):
    if valor < 0:
        print(f"[ALERTA] Valor negativo detectado: {valor}")
    else:
        print(f"[OK] Sensor registrou: {valor:.2f}")

@processar_dado.register(dict)
def _(pacote):
    equipamento = pacote.get("equipamento", "desconhecido")
    status = pacote.get("status", "indefinido")
    print(f"[PACOTE] Equipamento: {equipamento} | Status: {status}")

@processar_dado.register(str)
def _(texto):
    if "vazamento" in texto.lower():
        print(f"[RELATÓRIO] ⚠️ Vazamento reportado: {texto}")
    else:
        print(f"[RELATÓRIO] Log recebido: {texto}")

@processar_dado.register(list)
def _(serie):
    media = sum(serie) / len(serie) if serie else 0
    print(f"[SÉRIE TEMPORAL] Média das leituras: {media:.2f}")

# Simulação de dados recebidos
dados = [
    78.5,
    {"equipamento": "Bomba P-302", "status": "operando"},
    "Relatório diário: tudo normal.",
    "Detectado vazamento na linha 7 às 14h.",
    [72.1, 74.3, 75.0, 73.8],
    True
]

print(f"📡 Início do processamento: {datetime.now()}\n")
for d in dados:
    processar_dado(d)
