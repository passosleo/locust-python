FROM python:3.9-slim

WORKDIR /app

RUN pip install locust pandas matplotlib seaborn

COPY locustfile.py . 
COPY gerar_graficos.py .

CMD ["sh", "-c", "locust -f locustfile.py --headless -u 10 -r 2 --run-time 2m --csv=results_10 && locust -f locustfile.py --headless -u 50 -r 2 --run-time 2m --csv=results_50 && locust -f locustfile.py --headless -u 100 -r 5 --run-time 2m --csv=results_100 && locust -f locustfile.py --headless -u 250 -r 10 --run-time 2m --csv=results_250 && python gerar_graficos.py"]
