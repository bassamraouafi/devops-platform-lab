# 🚀 DevOps Platform Lab

A production-oriented DevOps laboratory demonstrating how to build, secure, containerize, deploy and monitor a cloud-native application.

The goal of this project is to demonstrate a complete DevOps lifecycle, from source code to deployment and observability.

---

## 🎯 Project Objective

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

## 🏗️ Architecture

```text
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
