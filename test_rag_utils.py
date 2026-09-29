from langchain_core.documents import Document
from rag_utils import split_documents


def test_split_documents():
    docs = [
        Document(
            page_content="This is a simple test document for our RAG pipeline."
        )
    ]

    chunks = split_documents(
        docs,
        chunk_size=20,
        chunk_overlap=5
    )

    assert len(chunks) > 1
