# Como executar

## Pré-requisitos

- Docker e Docker Compose instalados.

## Como Executar

Na pasta do projeto, execute:

```bash
docker-compose up --build
```

## Resultados

Os arquivos (CSVs e gráficos) serão gerados na pasta `output_docker` após a execução do Docker Compose.
Os arquivos gerados incluem:

- `results_10_exceptions.csv`
- `results_10_failures.csv`
- `results_10_stats_history.csv`
- `results_10_stats.csv`
- `results_50_exceptions.csv`
- `results_50_failures.csv`
- `results_50_stats_history.csv`
- `results_50_stats.csv`
- `results_100_exceptions.csv`
- `results_100_failures.csv`
- `results_100_stats_history.csv`
- `results_100_stats.csv`
- `results_250_exceptions.csv`
- `results_250_failures.csv`
- `results_250_stats_history.csv`
- `results_250_stats.csv`
- `grafico_escalabilidade_scatter.png`
- `grafico_escalabilidade.png`
- `grafico_percentis_barras.png`
- `grafico_percentis.png`
- `grafico_throughput_area.png`
- `grafico_throughput.png`
