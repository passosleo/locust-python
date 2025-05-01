import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

# Define os arquivos e configurações dos testes
configs = [10, 50, 100, 250]
base_filename = "results_{}_stats.csv"

# Estruturas para armazenar os dados agregados
throughputs = []
percentis_p90 = []
percentis_p95 = []

for users in configs:
    path = base_filename.format(users)
    if not os.path.exists(path):
        print(f"Arquivo {path} não encontrado, pulando...")
        continue

    df = pd.read_csv(path)

    # Remove total row se existir
    df = df[df["Name"] != "Aggregated"]

    # Agrupar métricas relevantes
    total_reqs = df["Request Count"].sum()
    total_failures = df["Failure Count"].sum()
    avg_rps = df["Requests/s"].sum()

    # Pega percentis
    p90 = df["90%"].mean()
    p95 = df["95%"].mean()

    throughputs.append({"users": users, "rps": avg_rps})
    percentis_p90.append({"users": users, "p90": p90})
    percentis_p95.append({"users": users, "p95": p95})

# Converte para DataFrame
df_throughput = pd.DataFrame(throughputs)
df_p90 = pd.DataFrame(percentis_p90)
df_p95 = pd.DataFrame(percentis_p95)

# === GRÁFICO 1: Percentis ===
plt.figure(figsize=(10, 6))
sns.lineplot(x="users", y="p90", data=df_p90, marker="o", label="p90")
sns.lineplot(x="users", y="p95", data=df_p95, marker="o", label="p95")
plt.title("Percentis de Tempo de Resposta (p90 e p95)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Tempo de resposta (ms)")
plt.legend()
plt.tight_layout()
plt.savefig("grafico_percentis.png")
plt.close()

# === GRÁFICO 2: Throughput ===
plt.figure(figsize=(10, 6))
sns.lineplot(x="users", y="rps", data=df_throughput, marker="o", color="green")
plt.title("Throughput (Requests por Segundo)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Requests/s")
plt.tight_layout()
plt.savefig("grafico_throughput.png")
plt.close()

# === GRÁFICO 3: Escalabilidade ===
plt.figure(figsize=(10, 6))
sns.regplot(x="users", y="rps", data=df_throughput, marker="o", color="purple", ci=None)
plt.title("Comportamento sob Escalabilidade")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Requests/s")
plt.tight_layout()
plt.savefig("grafico_escalabilidade.png")
plt.close()

# === GRÁFICO 1B: Percentis - BARRAS ===
plt.figure(figsize=(10, 6))
sns.barplot(x="users", y="p90", data=df_p90, color="skyblue", label="p90")
sns.barplot(x="users", y="p95", data=df_p95, color="salmon", alpha=0.7, label="p95")
plt.title("Percentis de Tempo de Resposta (Barras)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Tempo de resposta (ms)")
plt.legend()
plt.tight_layout()
plt.savefig("grafico_percentis_barras.png")
plt.close()

# === GRÁFICO 2B: Throughput - ÁREA ===
plt.figure(figsize=(10, 6))
plt.fill_between(df_throughput["users"], df_throughput["rps"], color="lightgreen", alpha=0.6)
plt.plot(df_throughput["users"], df_throughput["rps"], marker="o", color="green")
plt.title("Throughput (Área)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Requests/s")
plt.tight_layout()
plt.savefig("grafico_throughput_area.png")
plt.close()

# === GRÁFICO 3B: Escalabilidade - SCATTER ===
plt.figure(figsize=(10, 6))
sns.scatterplot(x="users", y="rps", data=df_throughput, s=100, color="purple")
plt.title("Escalabilidade (Scatter)")
plt.xlabel("Usuários simultâneos")
plt.ylabel("Requests/s")
plt.tight_layout()
plt.savefig("grafico_escalabilidade_scatter.png")
plt.close()

print("Gráficos gerados com sucesso:")
print(" - grafico_percentis.png")
print(" - grafico_throughput.png")
print(" - grafico_escalabilidade.png")
print(" - grafico_percentis_barras.png")
print(" - grafico_throughput_area.png")
print(" - grafico_escalabilidade_scatter.png")
print("Verifique os arquivos gerados para análise.")



