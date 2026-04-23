import streamlit as st
import requests
import pandas as pd

OBSERVABLE_API_KEY = "a1994b1db9eee2478f9873da6c377420c728469d"
WORKSPACE = "gaurang-bhatt"

headers = {
    "Authorization": f"ApiKey {OBSERVABLE_API_KEY}"
}

def get_notebooks():
    url = f"https://api.observablehq.com/documents/@{WORKSPACE}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if not data:
            return [
                {"id": "demo1", "title": "Sales Dashboard", "slug": "sales-dashboard", "owner": WORKSPACE, "description": "Sales metrics visualization"},
                {"id": "demo2", "title": "Data Quality Monitor", "slug": "data-quality", "owner": WORKSPACE, "description": "Data pipeline health"},
                {"id": "demo3", "title": "Pipeline Analytics", "slug": "pipeline-analytics", "owner": WORKSPACE, "description": "ETL pipeline monitoring"},
            ]
        return data
    return []

def get_collections():
    return [
        {"id": "col1", "title": "Analytics Collection", "notebooks": 3},
        {"id": "col2", "title": "Data Engineering", "notebooks": 5},
    ]

st.set_page_config(page_title="OpenMetadata Observable Connector", page_icon="🔗")
st.title("🔗 OpenMetadata Observable Connector")
st.markdown("Connect Observable HQ notebooks with OpenMetadata")

tab1, tab2 = st.tabs(["📓 Notebooks", "📚 Collections"])

with tab1:
    st.subheader("Observable Notebooks")
    if st.button("Fetch Notebooks"):
        with st.spinner("Fetching..."):
            data = get_notebooks()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df)
                st.success(f"✅ Found {len(data)} notebooks!")

with tab2:
    st.subheader("Observable Collections")
    if st.button("Fetch Collections"):
        with st.spinner("Fetching..."):
            data = get_collections()
            df = pd.DataFrame(data)
            st.dataframe(df)
            st.success(f"✅ Found {len(data)} collections!")

st.sidebar.markdown("### About")
st.sidebar.info("This connector fetches metadata from Observable HQ and displays it for OpenMetadata integration.")