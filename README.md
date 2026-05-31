# 📊 Autonomous Data Analyst Agent — JK Data Lab

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.22+-3F4F75?style=flat&logo=plotly&logoColor=white)](https://plotly.com)
[![Agentic AI](https://img.shields.io/badge/Agentic-AI-00FFD4?style=flat)](https://www.jkdatalab.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Author](https://img.shields.io/badge/JK_Data_Lab-www.jkdatalab.com-00FFD4?style=flat)](https://www.jkdatalab.com)

> AI agent that autonomously analyzes uploaded data, generates business insights, and delivers strategic recommendations — no manual prompting required.

---

## What It Does

- **Autonomous multi-step analysis** — the agent profiles data, runs statistics, detects patterns, generates insights, and produces recommendations in a single click
- **CSV / Excel upload** — accepts any `.csv` or `.xlsx` file; falls back to built-in sample business data for instant demo
- **Auto-generated charts** — revenue by product (bar) and revenue by region (donut) rendered with Plotly inside a dark theme UI
- **Ollama LLM integration** — optionally connects to a local Ollama instance (llama3, mistral, deepseek-coder) for AI-powered narrative
- **One-click export** — downloads all insights and recommendations as a plain-text report

---

## Architecture

```
app.py
│
├── generate_sample_data()      # cached synthetic business dataset (200 rows)
│
├── DataAnalystAgent
│   ├── __init__()              # configures Ollama host, model, demo flag
│   ├── log_action()            # appends timestamped agent steps
│   └── analyze(df)             # 5-step pipeline → stats, insights, recommendations
│
└── Streamlit UI
    ├── Sidebar                 # demo toggle, Ollama host, model select, depth
    ├── File uploader           # CSV / Excel
    ├── "Run Analysis" button   # triggers DataAnalystAgent.analyze()
    ├── KPI metrics row         # rows, columns, missing values, duplicates
    ├── Insights + Recommendations columns
    ├── Auto-generated charts   # bar + donut via Plotly Express
    └── Export button           # downloads report as .txt
```

---

## Quick Start

### 1. Clone & install

```powershell
# Windows (PowerShell)
git clone <repo-url>
cd 03_autonomous_data_analyst
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# macOS / Linux
git clone <repo-url>
cd 03_autonomous_data_analyst
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Configuration

| Setting | Where | Default | Notes |
|---------|-------|---------|-------|
| Demo Mode | Sidebar checkbox | `True` | Disables Ollama calls; uses rule-based insights |
| Ollama Host | Sidebar text input | `localhost` | Hostname or IP of Ollama server |
| Ollama Port | `DataAnalystAgent.__init__` | `11434` | Change in code if non-default |
| Model | Sidebar selectbox | `llama3` | `llama3`, `mistral`, `deepseek-coder` |
| Analysis Depth | Sidebar selectbox | `Quick` | UI label only — extend `analyze()` to wire up |

### Optional: Ollama LAN setup

```bash
ollama pull llama3
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Enable **Demo Mode** in the sidebar to run fully offline without Ollama.

---

## Project Structure

```
03_autonomous_data_analyst/
├── app.py               # Main Streamlit app + DataAnalystAgent class
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── venv/                # Local virtual environment (not committed)
```

---

## Requirements

| Package | Purpose |
|---------|---------|
| `streamlit` | Web UI framework |
| `pandas` | DataFrame operations and CSV/Excel parsing |
| `numpy` | Numerical computations and random data generation |
| `openpyxl` | Excel (`.xlsx`) file reading |
| `plotly` | Interactive bar and donut charts |
| `requests` | HTTP calls to Ollama REST API |
| `langchain` | LLM abstraction layer |
| `langchain-community` | Ollama community integration |

---

## Agent Pipeline

The `DataAnalystAgent.analyze()` method runs five sequential steps:

1. **Data profiling** — row/column counts, missing values, duplicates
2. **Statistical analysis** — numeric column summary statistics
3. **Pattern detection** — trend direction, outlier flagging
4. **Insight generation** — revenue trends, top product, satisfaction score
5. **Recommendations** — strategic action items based on findings

---

## License

MIT © [Kinjal Jayswal](https://www.jkdatalab.com)

---

<div align="center">

Built with ❤️ by **[JK Data Lab](https://www.jkdatalab.com)**  
📧 kinjal@jkdatalab.com | 🌐 www.jkdatalab.com | AI & Data Science Consulting

</div>
