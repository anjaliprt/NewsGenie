import streamlit as st
from workflow import graph

st.set_page_config(
    page_title="NewsGenie",
    page_icon="📰",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []


# ---------------- CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}
/* Center app container */
.block-container {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    padding-top: 2rem;
}


/* Center text */
.center {
    text-align:center;
}


           

/* Search Button */
.stButton > button {
    background: #2563EB;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 18px;
    font-weight: 600;
}

/* News card */
.news-card {
    background: #E0F2FE;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

/* Link button */
.stLinkButton a {
    background: #ffffff;
    color: #2563EB !important;
    border: 2px solid #2563EB;
    padding: 8px 14px;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none !important;
}

.stLinkButton a:hover {
    background: #2563EB;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- UI HEADER ----------------
st.title("📰 NewsGenie")
st.caption("AI-powered News & Information Assistant")

# ---------------- QUERY INPUT ----------------

query = st.text_input("🔎 Enter your query",
                      placeholder="Ask about the latest news or any general topic...",
                      key="current_query")

# ---------------- BUTTON ----------------
if st.button("Search"):

    if not query.strip():
        st.warning("Please enter a query")
        st.stop()
    try:    

        with st.spinner("Thinking... 🧠"):
          result = graph.invoke({"query": query})
    except Exception as e:
        st.error(f"System error: {e}")
        st.stop()    

    response = result.get("response")
    query_type = result.get("query_type", "general")

    st.success(f"Detected Type: {query_type.upper()}")

    # ---------------- CHATBOT RESPONSE ----------------
    if isinstance(response, str):
        st.markdown("### 💬 Answer")
        st.write(response)

    # ---------------- NEWS RESPONSE ----------------
    elif isinstance(response, list):
        st.markdown("### 📰 Top News Results")

        for article in response:
            if isinstance(article, dict):

                st.markdown(f"""
                <div class="news-card">
                    <h4>📰 {article.get('title', 'No Title')}</h4>
                    <p>{article.get('summary', '')}</p>
                </div>
                """, unsafe_allow_html=True)

                st.link_button("📖 Read More", article.get("url", "#"))

                st.divider()

    # ---------------- SAFETY FALLBACK ----------------
    else:
        st.error("Unexpected response format from graph.")
 # ---------------- SAVE TO HISTORY ----------------
    st.session_state.history.append({
        "query": query,
        "type": query_type,
        "response": response
    })
# ---------------- DISPLAY HISTORY ----------------
st.markdown("### 📜 Conversation History")

for item in reversed(st.session_state.history):

    st.markdown(f"#### 🔎 Query: {item['query']}")
    st.info(f"Type: {item['type'].upper()}")

    response = item["response"]
    if isinstance(response, str):
       st.write(response)

    elif isinstance(response, list):

       for article in response:

          st.markdown(f"**📰 {article['title']}**")
          st.write(article["summary"])
          st.link_button("Read More", article["url"])
if st.button("🗑 Clear History"):
    st.session_state.history = []
    st.rerun()        