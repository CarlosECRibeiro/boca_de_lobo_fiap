from fastapi import FastAPI, Response
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
import requests

app = FastAPI(title="Boca de Lobo API", version="1.0.0")

# Métricas de Ouro (Prometheus)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency')
RAIN_API_UP = Gauge('rain_api_up', 'Status da API externa de Previsão de Chuva (1=Up, 0=Down)')

@app.get("/health")
def health_check():
    # Simula verificação da API externa de previsão meteorológica
    try:
        # Exemplo simulado: checa se um serviço externo responde
        RAIN_API_UP.set(1)
        return {"status": "healthy", "service": "Boca de Lobo MVP", "rain_api": "online"}
    except Exception:
        RAIN_API_UP.set(0)
        return {"status": "degraded", "rain_api": "offline"}

@app.get("/bocas-risco")
def listar_bocas_risco():
    REQUEST_COUNT.labels(method='GET', endpoint='/bocas-risco', http_status=200).inc()
    return [
        {"id": "BL-042", "bairro": "Itaquera", "status": "Entupida (Lixo/Folhas)", "risco": "Alto", "lat": -23.54, "lng": -46.45},
        {"id": "BL-109", "bairro": "Grajaú", "status": "Drenagem Crítica", "risco": "Iminente", "lat": -23.75, "lng": -46.68}
    ]

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)