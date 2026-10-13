# Controle de Gastos Fim de Semana
import csv
from datetime import datetime

ARQUIVO = "gastos.csv"

def adicionar_gasto():
    data = input("Data (ex: 18/10): ")
    o_que = input("O que gastou (ex: Outback): ")
    categoria = input("Categoria [Alimentação/Transporte/Lazer/Outros]: ")
    valor = float(input("Valor R$: ").replace(",", "."))
    forma = input("Forma pgto [Pix/Cartão/Dinheiro]: ")

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([data, o_que, categoria, valor, forma])
    print(f"✅ Gasto salvo: {o_que} - R$ {valor}")

def ver_total():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            total = 0
            for row in reader:
                if len(row) >= 4 and row[0]!= "DATA":
                    total += float(row[3])
            print(f"\n💰 TOTAL DO FDS: R$ {total:.2f}")
    except FileNotFoundError:
        print("Nenhum gasto ainda.")

if __name__ == "__main__":
    print("=== GASTOS FDS ===")
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Ver total")
        print("3 - Sair")
        op = input("Escolha: ")
        if op == "1":
            adicionar_gasto()
        elif op == "2":
            ver_total()
        else:
            break
