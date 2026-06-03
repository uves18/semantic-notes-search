import streamlit as st
from app.vector_store import get_collection, add_notes
from app.search import search_notes

def init_session():
    if 'collection' not in st.session_state:
        st.session_state.collection = get_collection()
        st.session_state.notes_loaded = False

def render_sidebar():
    with st.sidebar:
        st.header("📁 Manage Notes")

        uploaded_files = st.file_uploader(
            "Upload text files",
            type=['txt'],
            accept_multiple_files=True
        )

        if st.button("Load Notes") and uploaded_files:
            documents = []
            ids = []
            metadatas = []

            for file in uploaded_files:
                content = file.read().decode('utf-8')
                documents.append(content)
                ids.append(file.name)
                metadatas.append({'filename': file.name})

            add_notes(st.session_state.collection, documents, ids, metadatas)
            st.session_state.notes_loaded = True
            st.success(f"Loaded {len(documents)} notes!")

        if st.session_state.notes_loaded:
            st.info(f"Total notes: {st.session_state.collection.count()}")

def render_search():
    query = st.text_input("🔍 Search your notes:", placeholder="What are you looking for?")

    if query:
        results = search_notes(st.session_state.collection, query)

        st.subheader("Results:")

        if results:
            for result in results:
                with st.expander(f"📄 {result['filename']} - {result['relevance']:.1f}% match"):
                    st.markdown(result['content'])
                    st.caption(f"Relevance score: {result['relevance']:.1f}%")
        else:
            st.warning("No results found. Try uploading some notes first!")