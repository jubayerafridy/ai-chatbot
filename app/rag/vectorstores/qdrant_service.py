from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchAny,
    PointStruct,
    VectorParams,
)

from app.core.settings import settings
from app.rag.vectorstores.base import BaseVectorStore


class QdrantVectorStore(
    BaseVectorStore,
):

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
        )

        self.collection_name = (
            settings.QDRANT_COLLECTION
        )

    def create_collection(
        self,
    ) -> None:

        collections = (
            self.client.get_collections()
        )

        existing = [
            collection.name
            for collection
            in collections.collections
        ]

        if self.collection_name in existing:
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

    def upsert(
        self,
        ids: list[int],
        vectors: list[list[float]],
        payloads: list[dict],
    ) -> None:

        points = []

        for point_id, vector, payload in zip(
            ids,
            vectors,
            payloads,
        ):

            points.append(
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload=payload,
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(
        self,
        vector: list[float],
        limit: int = 5,
        document_ids: list[int] | None = None,
    ):

        query_filter = None

        if document_ids:

            query_filter = Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match=MatchAny(
                            any=document_ids,
                        ),
                    )
                ]
            )

        return self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            limit=limit,
            query_filter=query_filter,
        ).points