🚀 DevOps Platform Lab

A production-oriented DevOps laboratory demonstrating how to build, secure, containerize, deploy and monitor a cloud-native application.

The goal of this project is to demonstrate a complete DevOps lifecycle, from source code to deployment and observability.

---

🎯 Project Objective

This project implements a small REST API and focuses on the DevOps platform around the application.

The platform will demonstrate:

- CI/CD automation
- Automated testing
- Code quality analysis
- Security scanning
- Containerization
- Container image management
- Kubernetes/OpenShift deployment
- Helm-based deployment
- GitOps practices
- Monitoring and observability

---

🏗️ Architecture

Developer
    │
    ▼
  GitHub
    │
    ▼
GitHub Actions
    │
    ├── Tests
    ├── Code Quality
    ├── Security Scan
    └── Docker Build
            │
            ▼
   Container Registry
            │
            ▼
          Helm
            │
            ▼
   Kubernetes / OpenShift
            │
       ┌────┴────┐
       ▼         ▼
 Prometheus   Application
       │
       ▼
    Grafana

---

🧩 Application

The project includes a lightweight REST API for managing application services.

Example service:

{
  "name": "payment-api",
  "environment": "production",
  "version": "2.4.1",
  "status": "healthy"
}

Main endpoints:

GET    /services
GET    /services/{id}
POST   /services
PUT    /services/{id}
DELETE /services/{id}

GET    /health
GET    /metrics

The application itself is intentionally simple.

The main focus of the project is the DevOps lifecycle and platform engineering.

---

🔄 CI/CD Pipeline

The CI/CD pipeline will automate:

Git Push
   │
   ▼
Automated Tests
   │
   ▼
Code Quality Analysis
   │
   ▼
Security Scanning
   │
   ▼
Docker Image Build
   │
   ▼
Container Image Scan
   │
   ▼
Container Registry
   │
   ▼
Helm Deployment

---

🔐 Security

Security will be integrated directly into the delivery pipeline.

Planned tools:

- "Trivy"
- "SonarQube"
- "CodeQL"
- Dependency scanning
- Container image scanning
- SBOM generation

---

☁️ Containerization & Deployment

The application will be packaged as a Docker container.

Deployment will use:

- "Docker"
- "Kubernetes"
- "OpenShift"
- "Helm"

The same application will be deployable to both Kubernetes and OpenShift environments.

---

📦 Helm

The Kubernetes/OpenShift deployment will be packaged as a Helm chart.

The chart will manage:

- Deployments
- Services
- ConfigMaps
- Environment configuration
- OpenShift Routes

---

📊 Observability

The platform will expose application metrics through:

/metrics

Monitoring will use:

- "Prometheus"
- "Grafana"

The objective is to monitor:

- Application availability
- Request rate
- Response time
- Errors
- Container health
- Resource usage

---

🛠️ Technology Stack

Application

"Python" "FastAPI" "REST API"

DevOps

"Git" "GitHub Actions" "Docker" "Helm" "Kubernetes" "OpenShift"

Security & Quality

"SonarQube" "Trivy" "CodeQL" "SBOM"

Observability

"Prometheus" "Grafana"

---

📁 Project Structure

devops-platform-lab/
│
├── app/
├── docker/
├── helm/
├── monitoring/
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── sonar-project.properties
├── .gitignore
└── README.md

---

🚧 Project Status

🟡 In development

Planned implementation:

- [ ] FastAPI application
- [ ] Unit tests
- [ ] Docker containerization
- [ ] GitHub Actions CI
- [ ] SonarQube integration
- [ ] Trivy security scanning
- [ ] Container registry
- [ ] Helm chart
- [ ] Kubernetes deployment
- [ ] OpenShift deployment
- [ ] Prometheus metrics
- [ ] Grafana dashboards
- [ ] Continuous deployment
- [ ] GitOps workflow
- [ ] Complete documentation

---

🎯 Learning Goals

This project is designed to demonstrate practical experience with:

- CI/CD engineering
- Containerization
- Kubernetes/OpenShift
- Helm
- DevSecOps
- GitOps
- Observability
- Infrastructure automation
- Cloud-native application delivery

---

👨‍💻 Author

Bassam Raouafi

DevOps • Cloud • AI Engineer

GitHub: "@bassamraouafi" (https://github.com/bassamraouafi)