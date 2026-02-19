🛡️ Neural Shadow
Autonomous Cloud Threat Orchestrator & Reconnaissance Suite

Neural Shadow is a high-performance security dashboard designed to bridge the gap between raw vulnerability detection and actionable intelligence. Developed by a former Law Enforcement Officer and Lead Diesel Technician, this tool applies a diagnostic "root-cause" mindset to modern cloud infrastructure.

🚀 Core Features
🧠 Neural Brain (AI): Leverages GPT-4o-mini to perform real-time Kill Chain analysis and remediation planning on raw log data.

🔑 OWEN Engine: A specialized validator for leaked Google Cloud Platform (GCP) service account keys.

📡 Global Recon & Mapping: Discovers subdomains via Certificate Transparency logs and geolocates assets on a global threat map.

🛡️ Header Audit: Instantly evaluates a target's HTTP security posture (CSP, HSTS, XFO, etc.).

🛠️ Installation & Setup
Clone the Repository:

Bash
git clone https://github.com/yourusername/neural-shadow.git
cd neural-shadow
Install Dependencies:

Bash
pip install -r requirements.txt
Configure Secrets:
Create a .env file in the root directory or add to Streamlit Secrets:

Plaintext
OPENAI_API_KEY=your_sk_key_here
Run the Application:

Bash
streamlit run app.py
📐 Technical Architecture
Neural Shadow is built using a modular Python architecture to ensure scalability and security:

Frontend: Streamlit (Custom CSS "Cyber Ops" Theme)

AI Orchestration: OpenAI API (GPT-4o-mini)

Cloud Integration: Google Auth & GCP IAM Validation

Intelligence: crt.sh API & IP-API Geolocation

👤 About the Developer
I am a Computer and Information Sciences student at South University. My approach to cybersecurity is informed by years of experience in Texas Law Enforcement and Mechanical Diagnostics. I specialize in identifying information disclosures and have submitted reports to the U.S. Department of Defense and major tech platforms via HackerOne.
