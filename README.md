🛡️ Neural Shadow
Autonomous Cloud Security & AI-Driven Threat Correlation

Neural Shadow is an AI-powered security dashboard designed to identify, validate, and prioritize cloud vulnerabilities. By combining traditional scanning logic with LLM reasoning, it helps security teams bridge the gap between "finding a leak" and "understanding the risk."

🚀 Key Features
Multi-Threat Correlation Engine: Automatically analyzes high-risk vulnerabilities including TOKEN_LEAKAGE, OPEN_FIREWALL, and PUBLIC_BUCKET.

AI Reasoning Engine: Uses OpenAI's GPT-4o-mini to perform Kill Chain Analysis and suggest remediation strategies.

Mission Control UI: A streamlined Streamlit dashboard that provides a real-time view of your cloud security posture.

Zero-Trust Architecture: Securely manages GCP and OpenAI credentials using encrypted environment secrets.

🛠️ Tech Stack
Language: Python 3.x

Framework: Streamlit

Intelligence: OpenAI API (GPT-4o-mini)

Cloud: Google Cloud Platform (SCC & IAM)

Deployment: Streamlit Cloud with GitHub CI/CD

⚙️ Installation & Setup
Clone the Repo:

Bash
git clone https://github.com/jonathanrey87/Neural-Shadow.git
Install Dependencies:

Bash
pip install -r requirements.txt
Configure Secrets:
Create a .streamlit/secrets.toml file or use the Streamlit Cloud Secrets dashboard to add:

OPENAI_API_KEY

GCP_PROJECT_ID

[gcp_service_account] (Service account JSON details)

🎓 About the Developer
Developed by Jonathan Mendiola, an IT Professional and student at South University. Built for the HackFest Cybersecurity Hackathon on Devpost.
