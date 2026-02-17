import streamlit as st
import openai
from google.oauth2 import service_account

# 1. Setup Page Branding
st.set_page_config(page_title="Neural Shadow", page_icon="🛡️")
st.title("🛡️ Neural Shadow: Security Agent")
st.subheader("Cloud Vulnerability & Threat Analysis")

# 2. Securely Load Secrets (Pulling from the TOML we saved)
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    gcp_info = st.secrets["gcp_service_account"]
    credentials = service_account.Credentials.from_service_account_info(gcp_info)
    project_id = st.secrets["GCP_PROJECT_ID"]
    st.success("✅ Securely connected to OpenAI and GCP")
except Exception as e:
    st.error(f"❌ Connection Error: Ensure your Secrets box is filled correctly.")
    st.stop()

# 3. Simple UI for your Demo
tab1, tab2 = st.tabs(["Scan Dashboard", "Agent Chat"])

with tab1:
    st.write(f"**Target Project:** `{project_id}`")
    if st.button("Run Security Audit"):
        with st.spinner("Analyzing cloud permissions..."):
            # This is where your scanning logic goes
            st.info("Scanning IAM policies for leaked GCP keys...")
            st.warning("Found 1 potential info disclosure on Ansible server.")

with tab2:
    user_input = st.chat_input("Ask the agent about a vulnerability...")
    if user_input:
        st.chat_message("user").write(user_input)
        # OpenAI Agent Response
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.chat_message("assistant").write(response.choices[0].message.content)
