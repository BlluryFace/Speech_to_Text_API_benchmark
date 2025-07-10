# Transcription API Benchmarking

**Supervisor**: Roy Hyunjin Han  
**Developer**: Bllury Face

---

## 🧭 Introduction

### 📌 Purpose
This project aims to assemble a robust test dataset and benchmarking framework to evaluate the performance of different transcription APIs in a real-world utility call context.

### 🚨 Problem Statement
Twilio's native transcription API currently delivers subpar accuracy while also being cost-inefficient. This has prompted an exploration into third-party transcription solutions that may offer better performance at lower cost.

### 🎯 Target Audience
- **Field personnel at utilities companies** making or handling recorded phone calls.
- **Utilities companies** that require high-quality transcriptions for downstream tasks, such as cause slug extraction.

---

## 🎯 Objectives

### ✅ Goals
- Evaluate the transcription **accuracy** of the top 5 Speech-to-Text providers.
- Determine the **best provider** to integrate into our Twilio-based pipeline.

### 🚫 Non-Goals
- Delve into the internal ML models used by each provider.
- Research STT training methodologies or build custom transcription systems.

---

## 📏 Evaluation Metrics

### 📌 Primary Metric
**Word Error Rate (WER)**:  
- Measures transcription accuracy by comparing predicted text to reference transcripts.
- Formula: WER = (S + D + I) / N  
  Where:  
  S = Substitutions  
  D = Deletions  	
  I = Insertions  
  N = Number of words in the reference transcript
- JiWER library will be used to calculate WER after each run
- Documentation: https://pypi.org/project/jiwer/

---

## 🔧 Technology Stack

- **Backend**: Python + FastAPI
- **API Integrations**: OpenAI, Webhook endpoints, Twilio (for reference)
- **Evaluation Tools**: Python scripts for WER analysis (planned)

---
