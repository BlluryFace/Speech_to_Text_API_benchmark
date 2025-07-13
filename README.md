# Transcription API Benchmarking

**Supervisor**: Roy Hyunjin Han  
**Developer**: Bllury Face

---

## 🧭 Introduction

### 📌 Purpose
This project aims to assemble a robust test dataset and benchmarking framework to evaluate the performance of different transcription APIs in a real-world utility call context.

### 🚨 Problem Statement
Twilio's native transcription API currently delivers subpar accuracy while also
being cost-inefficient. This has prompted an exploration into third-party transcription
solutions that may offer better performance at lower cost.

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

**Word Error Rate (WER)**:  
- Measures transcription accuracy by comparing predicted text to reference transcripts.
- Formula: WER = (S + D + I) / N  
  Where:  
  S = Substitutions  
  D = Deletions  	
  I = Insertions  
  N = Number of words in the reference transcript
- Punctuation and capitalization are stripped, and variations are standardized 
(e.g., "color" vs "colour", "two" vs "2")
- JiWER library will be used to calculate WER after each run
- Documentation: https://pypi.org/project/jiwer/

---
## 📏 Testing methodology

* **Data collection** 
5 set of cause slugs, 10 cause slugs each set will be picked and said by the 
utility personnel, saying dot for after each cause slugs. Each round will 
have no overlapping cause slugs. 
 
* **Benchmarking**
The recording will be transcribed through 5 API Transcription providers to 
produce text result. Removing the word dot or '.' in the transcription text and 
then calculating the WER against expected text. Record the result the 5 runs  
and then plot the result on a box plot

---

## 🔧 Technology Stack

- **Backend**: Python + FastAPI
- **API Integrations**: OpenAI GPT-4o Transcribe, Gemini 2.5 Pro, Gemini 2.5 Flash,
ElevenLabs, AssemblyAI 
- **Reference Point**: Twilio Transcription API
- **Evaluation Tools**: Python scripts for WER analysis 

---
