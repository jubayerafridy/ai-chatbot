from app.schemas.rag import RetrievedChunk


class RAGPromptBuilder:

    SYSTEM_PROMPT = (
        "You are a helpful AI assistant.\n\n"
        "Answer ONLY using the provided context.\n\n"
        "If the answer is not found in the context, say:\n"
        "\"I don't have enough information in the uploaded documents.\""
    )

    def build(
        self,
        question: str,
        results: list[RetrievedChunk],
    ) -> str:

        context = "\n\n".join(
            chunk.content
            for chunk in results
        )

        return f"""
{self.SYSTEM_PROMPT}

Context:

{context}

Question:

{question}

Answer:
"""