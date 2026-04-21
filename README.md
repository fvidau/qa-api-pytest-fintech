# QA API Pytest – Fintech Testing Suite

Suite de pruebas de API desarrollada con **Python + Pytest + Requests**, orientada a validar endpoints de un contexto fintech mediante tests funcionales y negativos.

## Objetivo

Demostrar automatización de pruebas backend para APIs, aplicando:

- validación de status codes
- chequeo de estructura básica de respuestas
- pruebas negativas
- uso de fixtures reutilizables
- configuración desacoplada para ejecución local y CI

## Stack Tecnológico

- Python
- Pytest
- Requests

## Estructura del proyecto

```text
qa-api-pytest-fintech/
├── tests/
│   ├── conftest.py
│   ├── test_negativos.py
│   └── test_transactions.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md

## Security Testing

This project includes basic security checks:

- Validation of security headers:
  - Content-Security-Policy
  - X-Content-Type-Options
  - X-Frame-Options

- Negative testing for invalid endpoints

- Stability checks under multiple requests