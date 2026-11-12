# 🌊 CitizenTech - Projeto Boca de Lobo (MVP)

> **Global Solution 2026.2 - Secure DevOps Tools & Cloud Computing**

## 🎯 Objetivo do Projeto
O **Boca de Lobo** é um MVP de engenharia de software focado em segurança e emergências urbanas (enchentes). Antes de cada temporal, o sistema cruza o status de obstrução de bueiros/sarjetas com previsões meteorológicas para disparar ações preventivas para a equipe de limpeza e alertas de rota segura para moradores de regiões de risco.

---

## 🛠️ Ficha Técnica do MVP
* **Arquitetura:** Microsserviço containerizado em Python (FastAPI).
* **Containerização:** Docker (Multi-stage build, usuário não-root `appuser`, imagem enxuta baseada em `python:3.11-slim`).
* **Orquestração local:** Docker Compose.
* **Infraestrutura (IaC):** Terraform (AWS), com Remote State isolado em S3 e regras restritas de Security Groups (Porta SSH/22 nunca exposta para `0.0.0.0/0`).
* **Pipeline CI/CD:** GitHub Actions com escaneamento de segurança automatizado (**Gitleaks**, **Semgrep**, **Trivy**) e deploy automático via SSH.
* **Observabilidade:** Prometheus e Grafana (Métricas de Ouro) + Alerta crítico para falhas silenciosas na API de previsão de tempestades (`rain_api_up == 0`).

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* Docker e Docker Compose instalados.
* Git instalado.

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/boca-de-lobo-fiap.git](https://github.com/seu-usuario/boca-de-lobo-fiap.git)
   cd boca-de-lobo-fiap

2. Suba a stack com o Docker Compose:

    docker compose up --build -d

3. Acesse a aplicação:

    API de Risco: http://localhost:8000/bocas-risco

    Métricas Prometheus: http://localhost:8000/metrics