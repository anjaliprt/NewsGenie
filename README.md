
# 🚀 NewsGenie: AI-Powered Information & News Assistant

![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)
![Tavily Search](https://img.shields.io/badge/Search%20API-Tavily-00E5FF?style=for-the-badge&logo=google-search&logoColor=black)
![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph%20%7C%20StateGraph-orange?style=for-the-badge&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**NewsGenie** is an intelligent orchestration system that delivers filtered, real-time news updates and instant query processing within a unified interface. Driven by **Google Gemini** for conversational reasoning and classification, and integrated with **Tavily Search API** for dynamic web intelligence, the platform coordinates inputs via **LangGraph** and **Streamlit**. It intelligently triages user intent to bypass misinformation, isolate trustworthy data pools, and guarantee comprehensive answers using automated API fallback routes.

---

## 🏗️ System Architecture & Workflow

The orchestration graph governs state transformation using a deterministic routing system that intercepts unstructured inputs, labels intent, and assigns downstream processing workers.

```text
               ┌────────────────────────┐
               │   User Query Input     │
               └───────────┬────────────┘
                           │
                           ▼
               ┌────────────────────────┐
               │    classifier Node     │
               └───────────┬────────────┘
                           │
            ┌──────────────┴──────────────┐
            │ [query_type == 'news']      │ [query_type == 'general']
            ▼                             ▼
┌───────────────────────┐     ┌───────────────────────┐
│       news Node       │     │     chatbot Node      │
└───────────┬───────────┘     └───────────┬───────────┘
            │                             │
    ┌───────┴───────┐             ┌───────┴───────┐
    │ Success?      │             │ Success?      │
    ├───────────────┤             ├───────────────┤
    │ YES ──► Output│             │ YES ──► Output│
    │ NO  ──► Tavily│             │ NO  ──► Tavily│
    │         Search│             │         Search│
    └───────┬───────┘             └───────┬───────┘
            │                             │
            └──────────────┬──────────────┘
                           │
                           ▼
               ┌────────────────────────┐
               │          END           │
               └────────────────────────┘
```

### Strategic Graph Pipeline
* **Intent Routing (`classifier` Node):** Runs a localized zero-shot prompt evaluation via **Google Gemini** to determine whether an input requires real-time journalistic feeds (`news`) or general historical synthesis (`general`).
* **Curated News Retrieval (`news` Node):** Directs incoming search strings into a dedicated **NewsAPI** ingestion utility to pull the latest headlines across major publications.
* **Contextual Assistant Engine (`chatbot` Node):** Implements prompt constraints using **Google Gemini**, ensuring clear, highly relevant formatting within a strict 80-to-120-word boundary.

---


### 🖥️ Main Dashboard Overview

https://github.com/user-attachments/assets/195dde3b-de3e-437b-9eaa-78bef196586d

---

## 🛠️ Technology Stack Breakdown

The core application architecture leverages a modern, decoupled AI engineering ecosystem for state tracking, model execution, and user interface delivery:

* **Core Language Model Engine:** Powered by **Google Gemini**, processing zero-shot intent routing tokens and executing natural conversation responses.
* **State Management & Agentic Routing:** Engineered using **LangGraph (`StateGraph`)**, orchestrating cyclical state validation, conditional branch mapping, and sequential node executions.
* **Frontend Interface & UI Layer:** Designed using **Streamlit**, ensuring single-page state consistency, asynchronous layout streaming, and seamless session tracking.
* **External Integration Providers:**
  * **News Ingestion Engine:** Connected directly to **NewsAPI** to handle programmatic categorization filter structures.
  * **Real-Time Web Synthesis:** Integrated with **Tavily Search API** to fetch ground-truth, search-optimized global text results when primary assets respond with missing data objects.
* **Environment Configuration:** Built on **Python 3.10+** utilizing `python-dotenv` for securely isolating environment API tokens.

---

## 💻 Query Typology Comparison

To optimize token consumption and performance speed, queries are triaged at the entry point according to the matrix below:

| Attribute | 📰 News-Specific Query (`news`) | 💬 General Inquiry (`general`) |
| :--- | :--- | :--- |
| **Primary Objective** | Fetch active, dynamic updates and journalistic feeds. | Answer logical, conceptual, or historical questions. |
| **Primary Source** | Live NewsAPI Streams | Google Gemini Core LLM Engine |
| **Fallback Asset** | Tavily Search API Engine | Tavily Search Deep Context Synthesis |
| **Response Format** | Bulleted headline list with publication anchors. | Structured text explanation under 120 words. |

---

## 🧠 Streamlit Session Management

The front-end user interface leverages a persistent tracking architecture to ensure fluid, high-performance interactions:

* **State Persistence:** Caches full conversation records across multiple round-trips to prevent page-refresh context loss.
* **Category Memory:** Safely locks user-selected stream filters (e.g., Technology, Finance, Sports) within current sessions to deliver tailored updates instantly.
* **Rate-Limit Optimization:** Tracks active data state keys to intercept duplicate actions, reducing wasteful API request loops.
* **Graceful Clearing:** Provides visual controls to safely clear current thread logs and reset state graphs to zero instantly.

---

## 📰 NewsAPI Integration Context

When the runtime state settles on the `news` processing route, execution passes to an internal API wrapper module that acts as a bridge to standard **NewsAPI endpoints**:

* **Target Endpoints:** Dynamically targets headline protocols for broad stream categories and falls back to universal content indices for deep semantic keyphrase searches.
* **Payload Parameters:** Configures standard structural payloads passing targeted keywords, regional language limits (`en`), sorting priorities (`publishedAt`), and cryptographic developer identification parameters.
* **Data Parsing:** Raw downstream JSON payloads are mapped, filtering out broken image links or redacted placeholders, and returned to the main state as a list of structured news elements.

---

## 🛡️ Error Handling & System Resilience

The architecture integrates a multi-layered fallback layout to maintain continuity despite network anomalies or threshold limits:

* **Classifier Recovery:** If **Google Gemini** experiences connection limits, validation crashes, or returns an unsupported category format, the handler automatically falls back to `"general"` to maintain graph execution.
* **Chatbot Node Resiliency:** If the contextual assistant returns an empty response block, the application triggers a runtime **Tavily Search** fallback to deliver answers rather than crashing the interface.
* **NewsAPI Endpoint Resilience:** When **NewsAPI** returns connection error codes, rate-limiting statuses (e.g., HTTP 429), or empty article arrays, the graph defaults directly to a deep web search via **Tavily**. This ensures the UI displays raw web search alternatives instead of rendering an empty screen.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher installed on your local environment.
* Valid API Keys for Google Gemini, NewsAPI, and Tavily Search.

### Installation
1. **Clone the project repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/NewsGenie.git
   cd NewsGenie
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment keys:**
   Create a `.env` configuration file in the project's root folder:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   NEWSAPI_KEY=your_news_api_org_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Launch the User Interface:**
   ```bash
   streamlit run app.py
   ```

---

## 📄 License

Distributed under the **MIT License**. See the `LICENSE` file for more details.
