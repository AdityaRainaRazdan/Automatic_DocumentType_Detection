# Automatic_DocumentType_Detection

# 🚀 Auto Document Type Detection System (AI + ASP.NET MVC + FastAPI)

An AI-powered document classification platform that automatically detects and categorizes uploaded documents using OCR and machine learning.

This system integrates an **ASP.NET MVC frontend** with a **FastAPI-based ML service** to enable scalable, intelligent document processing workflows.

---

# 📌 Overview

Modern enterprise systems require automated document processing for identity verification, workflow automation, and intelligent data handling.

This project provides:

* Automated document classification
* OCR-based text extraction
* Dynamic document type detection
* Scalable AI service architecture
* Enterprise-ready MVC ↔ ML integration

The system supports processing PDFs and images such as:

* Identity documents
* Government IDs
* Licenses
* Custom documents
* Unknown document types

---

# 🎯 Problem Statement

Traditional document systems require manual classification and rule-based logic.

Challenges addressed:

* Manual document categorization
* Static document type handling
* Unstructured document processing
* Lack of AI integration in web systems
* Performance bottlenecks in document pipelines

This system introduces a machine learning–driven classification approach with dynamic category handling.

---

# 🏗 System Architecture

## High-Level Flow

```
Client Browser
      ↓
ASP.NET MVC Web Application
      ↓ HTTP Request
FastAPI ML Service
      ↓
OCR Processing Engine
      ↓
Feature Extraction (TF-IDF)
      ↓
Similarity-Based Classification
      ↓
Prediction Response
      ↓
MVC Result Rendering
```

---

## Architecture Components

### 1️⃣ ASP.NET MVC Frontend

Responsibilities:

* File upload interface
* Request handling
* API communication
* Result presentation
* Client-side validation

Key Design Goals:

* Clean MVC separation
* Stateless communication
* Service-oriented interaction
* UI independence from ML logic

---

### 2️⃣ FastAPI Machine Learning Service

Responsibilities:

* File ingestion
* OCR processing
* Text extraction
* Feature generation
* Document classification
* Result serialization

Key Design Goals:

* Independent ML service
* High throughput processing
* Python ecosystem utilization
* Horizontal scalability

---

### 3️⃣ Machine Learning Pipeline

```
File → OCR → Text → TF-IDF → Vector Similarity → Classification
```

Components:

* OCR: Text extraction from document images
* Feature Engineering: TF-IDF vectorization
* Classification: Cosine similarity matching
* Dynamic learning capability

---

# 🧠 Machine Learning Strategy

## Feature Extraction

* TF-IDF vectorization
* Token normalization
* Text similarity modeling

## Classification Method

* Cosine similarity scoring
* Best match category selection
* Unknown type detection capability

## Why Similarity-Based Classification?

Advantages:

* No heavy training required
* Fast inference
* Adaptable to new document types
* Low computational cost
* Incremental data addition

---

# ⚡ Performance Considerations

## Current Bottlenecks

* OCR processing time
* PDF to image conversion
* Model retraining overhead

## Optimization Strategies

* Background processing queue
* Model caching
* Vector database storage
* Asynchronous request handling
* Batch processing support

---

# 📦 Project Structure

```
AutoDocumentDetection/

├── mvc_frontend/
│   ├── Controllers/
│   │   └── HomeController.cs
│   ├── Models/
│   │   └── ClassificationResponse.cs
│   ├── Views/
│   ├── Program.cs
│   └── wwwroot/
│
├── ml_api/
│   ├── main.py
│   ├── model.py
│   ├── requirements.txt
│   └── saved_models/
│
├── uploads/
└── README.md
```

---

# 🛠 Technology Stack

## Frontend

* ASP.NET MVC (.NET 6+)
* Razor Views
* HttpClient Integration

## Backend

* Python
* FastAPI
* Uvicorn

## AI / ML

* Scikit-learn
* TF-IDF
* Cosine Similarity
* Tesseract OCR
* PDF2Image

---

# 🔌 API Documentation

## Upload Document

### Endpoint

```
POST /upload
```

### Request

```
multipart/form-data
file: Document file
```

### Response

```json
{
  "Category": "Aadhar",
  "Score": 0.91
}
```

---

# ⚙️ Installation Guide

## Prerequisites

* .NET SDK 6+
* Python 3.10 (recommended)
* Tesseract OCR
* Poppler utilities

---

## Setup ML Backend

```
cd ml_api
pip install -r requirements.txt
uvicorn main:app --reload
```

Test API:

```
http://127.0.0.1:8000/docs
```

---

## Setup MVC Frontend

1. Open project in Visual Studio
2. Build solution
3. Run application

---

# 🔄 System Workflow

1. User uploads document
2. MVC sends request to ML API
3. FastAPI processes file
4. OCR extracts text
5. ML model predicts category
6. Result returned to MVC
7. UI displays prediction

---

# 📊 Scalability Strategy

Future architecture evolution:

```
Load Balancer
      ↓
MVC Frontend Instances
      ↓
API Gateway
      ↓
ML Worker Pool
      ↓
Vector Database
```

Planned Enhancements:

* Microservice decomposition
* Queue-based processing
* Distributed model service
* Horizontal scaling
* Container deployment

---

# 🚀 Deployment Strategy

Recommended Production Setup:

* Docker containers
* Reverse proxy (Nginx)
* Background worker queue
* Model caching layer
* Persistent storage

---

# 🔐 Security Considerations

* File size validation
* Content type validation
* API request limits
* Input sanitization
* Upload isolation

---

# 🧪 Testing Strategy

* API endpoint testing
* File upload validation
* OCR accuracy tests
* Performance benchmarking

---

# 🐞 Troubleshooting

## API Not Responding

* Ensure FastAPI server running
* Verify endpoint URL
* Check port conflicts

## OCR Errors

* Verify Tesseract installation
* Verify Poppler configuration

## Timeout Issues

* Increase HttpClient timeout
* Optimize OCR pipeline

---

# 🔮 Future Enhancements

* Deep learning classification models
* Document entity extraction
* Multi-language OCR support
* Agentic AI workflow automation
* Vector database integration
* Real-time processing pipeline
* Model retraining automation
* Document storage system

---

# 🤝 Contribution Guidelines

1. Fork repository
2. Create feature branch
3. Commit changes
4. Submit pull request

---

# 📜 License

For educational and research use.

---

# 👨‍💻 Engineering Notes

This project demonstrates integration of:

* Enterprise web systems
* AI processing pipelines
* OCR-based document analysis
* Service-oriented architecture

Designed as a foundation for intelligent document processing platforms.

---
