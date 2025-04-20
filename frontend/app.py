import streamlit as st
import requests

st.title("SHL Assessment Recommender")

query = st.text_area("Enter job description or query")

if st.button("Get Recommendations"):
    with st.spinner("Thinking..."):
        res = requests.post("http://localhost:8000/recommend", json={"query": query})
        data = res.json()["results"]

        st.subheader("Recommended SHL Assessments")
        for item in data:
            st.markdown(f"- [{item['Assessment Name']}]({item['URL']})")
            st.write(f"🔹 Remote Support: {item['Remote Support']}")
            st.write(f"🔹 Adaptive: {item['Adaptive Support']}")
            st.write(f"🔹 Duration: {item['Duration']}")
            st.write(f"🔹 Type: {item['Test Type']}")
            st.divider()
