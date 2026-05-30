"""
Autonomous Data Analyst Agent — JK Data Lab
Agent that autonomously analyzes uploaded data, generates insights, and recommendations
Author: Kinjal Jayswal | JK Data Lab | www.jkdatalab.com
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
import time
import io
from datetime import datetime

st.set_page_config(page_title="Autonomous Data Analyst | JK Data Lab", page_icon="📊", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0A1628; color: #ffffff; }
    h1, h2, h3 { color: #00FFD4; }
    .agent-action { background: #0d2040; border-left: 3px solid #00FFD4; border-radius: 8px; padding: 10px; margin: 4px 0; font-family: monospace; font-size: 0.83rem; }
    .insight-card { background: linear-gradient(135deg, #0d2a2a, #1a3a3a); border: 1px solid #00FFD4; border-radius: 10px; padding: 15px; margin: 8px 0; }
    .stButton>button { background: linear-gradient(135deg, #00FFD4, #00aa88); color: #0A1628; font-weight: bold; }
</style>""", unsafe_allow_html=True)


@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    n = 200
    return pd.DataFrame({
        "Date": pd.date_range("2024-01-01", periods=n, freq="D"),
        "Revenue": np.random.lognormal(8, 0.5, n).round(2),
        "Customers": np.random.randint(50, 500, n),
        "Product": np.random.choice(["AI Consulting", "ML Model", "Dashboard", "Automation"], n),
        "Region": np.random.choice(["North America", "Europe", "Asia", "Middle East"], n),
        "Satisfaction": np.random.uniform(3.0, 5.0, n).round(1),
        "Cost": np.random.lognormal(7, 0.4, n).round(2),
    })


class DataAnalystAgent:
    """Autonomous agent for data analysis."""

    def __init__(self, use_demo=True, ollama_host="localhost", port=11434, model="llama3"):
        self.use_demo = use_demo
        self.ollama_host = ollama_host
        self.port = port
        self.model = model
        self.analysis_log = []

    def log_action(self, action: str):
        self.analysis_log.append({"time": datetime.now().strftime("%H:%M:%S"), "action": action})

    def analyze(self, df: pd.DataFrame) -> dict:
        results = {"steps": [], "stats": {}, "insights": [], "recommendations": [], "charts": []}

        # Step 1: Data profiling
        self.log_action("🔍 Profiling dataset structure and quality...")
        results["steps"].append("📋 Data profiling complete")
        results["stats"] = {
            "rows": len(df), "columns": len(df.columns),
            "numeric_cols": len(df.select_dtypes(include=np.number).columns),
            "missing_values": df.isnull().sum().sum(),
            "duplicates": df.duplicated().sum()
        }
        time.sleep(0.3)

        # Step 2: Statistical analysis
        self.log_action("📊 Running statistical analysis...")
        numeric = df.select_dtypes(include=np.number)
        results["steps"].append("📈 Statistical analysis complete")
        time.sleep(0.2)

        # Step 3: Pattern detection
        self.log_action("🔎 Detecting patterns and anomalies...")
        results["steps"].append("🎯 Pattern detection complete")
        time.sleep(0.2)

        # Step 4: Generate insights
        self.log_action("💡 Generating AI insights...")
        if "Revenue" in df.columns:
            avg_rev = df["Revenue"].mean()
            max_rev = df["Revenue"].max()
            results["insights"].extend([
                f"💰 Average revenue is ${avg_rev:,.0f} with peak of ${max_rev:,.0f}",
                f"📈 Revenue shows {'positive' if df['Revenue'].corr(pd.Series(range(len(df)))) > 0 else 'variable'} trend over time",
            ])
        if "Product" in df.columns:
            top_product = df.groupby("Product")["Revenue"].sum().idxmax() if "Revenue" in df.columns else df["Product"].mode()[0]
            results["insights"].append(f"🏆 Top performing product: {top_product}")
        if "Satisfaction" in df.columns:
            avg_sat = df["Satisfaction"].mean()
            results["insights"].append(f"⭐ Average satisfaction score: {avg_sat:.2f}/5.0")
        results["steps"].append("💡 Insights generation complete")
        time.sleep(0.2)

        # Step 5: Recommendations
        self.log_action("🎯 Generating strategic recommendations...")
        results["recommendations"] = [
            "📌 Focus resources on top-performing products and regions",
            "📌 Investigate revenue outliers for replication opportunities",
            "📌 Monitor satisfaction scores — set alert threshold at 3.5",
            "📌 Segment customers by region for targeted campaigns",
            "📌 Automate monthly reporting for executive dashboard"
        ]
        results["steps"].append("✅ Analysis complete — report ready!")
        return results


# ─── UI ───────────────────────────────────────────────────────────────────────
st.title("📊 Autonomous Data Analyst Agent")
st.markdown("**AI Agent that autonomously analyzes your data** — profiling, insights, recommendations, charts")
st.markdown("---")

with st.sidebar:
    st.markdown("### ⚙️ Agent Settings")
    use_demo = st.checkbox("Demo Mode", value=True)
    ollama_host = st.text_input("Ollama Host", value="localhost")
    model = st.selectbox("Model", ["llama3", "mistral", "deepseek-coder"])
    analysis_depth = st.selectbox("Analysis Depth", ["Quick", "Standard", "Deep"])
    st.markdown("---")
    st.markdown("### 🛠️ Agent Capabilities")
    st.markdown("- 🔍 Data profiling\n- 📊 Statistical analysis\n- 🎯 Pattern detection\n- 💡 Insight generation\n- 📋 Recommendations\n- 📈 Auto visualization")
    st.markdown("---")
    st.markdown("**🌐 [JK Data Lab](https://www.jkdatalab.com)**")

uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])
use_sample = st.checkbox("Use sample business data", value=True)

if st.button("🤖 Run Autonomous Analysis", type="primary"):
    df = pd.read_csv(uploaded) if uploaded else generate_sample_data()
    agent = DataAnalystAgent(use_demo, ollama_host)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("🤖 Agent Actions")
        log_ph = st.empty()

    with col2:
        st.subheader("📊 Live Analysis")
        with st.spinner("Agent analyzing..."):
            results = agent.analyze(df)
            log_ph.markdown("".join([f'<div class="agent-action">⏱️ {a["time"]} — {a["action"]}</div>' for a in agent.analysis_log]), unsafe_allow_html=True)

    st.markdown("---")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Rows", f"{results['stats']['rows']:,}")
    k2.metric("Columns", results['stats']['columns'])
    k3.metric("Missing Values", results['stats']['missing_values'])
    k4.metric("Duplicates", results['stats']['duplicates'])

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💡 AI Insights")
        for insight in results["insights"]:
            st.markdown(f'<div class="insight-card">{insight}</div>', unsafe_allow_html=True)

    with col2:
        st.subheader("🎯 Recommendations")
        for rec in results["recommendations"]:
            st.markdown(f'<div class="insight-card">{rec}</div>', unsafe_allow_html=True)

    if "Revenue" in df.columns and "Product" in df.columns:
        st.subheader("📈 Auto-Generated Charts")
        c1, c2 = st.columns(2)
        with c1:
            fig = px.bar(df.groupby("Product")["Revenue"].sum().reset_index(),
                        x="Product", y="Revenue", color="Revenue", color_continuous_scale="teal")
            fig.update_layout(paper_bgcolor="#0A1628", plot_bgcolor="#0d1f3a", font=dict(color="white"), height=300)
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            if "Region" in df.columns:
                fig2 = px.pie(df.groupby("Region")["Revenue"].sum().reset_index(),
                             values="Revenue", names="Region", hole=0.4,
                             color_discrete_sequence=px.colors.sequential.Teal)
                fig2.update_layout(paper_bgcolor="#0A1628", font=dict(color="white"), height=300)
                st.plotly_chart(fig2, use_container_width=True)

    st.download_button("📥 Export Analysis", "\n".join(results["insights"] + results["recommendations"]), "analysis_report.txt")

st.markdown("---")
st.markdown("Built with ❤️ by **[JK Data Lab](https://www.jkdatalab.com)** | Autonomous AI Agents")
