from qdrant_client.http.models import ScoredPoint


class RAGPromptBuilder:

    def build(
        self,
        question: str,
        results: list[ScoredPoint],
    ) -> str:

        context = "\n\n".join(
            point.payload["content"]
            for point in results
        )

        return f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:

"I don't have enough information in the uploaded documents."

Context:

{context}

Question:

{question}

Answer:
"""