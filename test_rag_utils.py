from rag_utils import chunk_text

def test_chunk_text():
    text = "abcdefghij"

    chunks = chunk_text(text, chunk_size=4)

    assert chunks == ["abcd", "efgh", "ij"]
