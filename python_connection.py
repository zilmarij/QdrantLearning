from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct,VectorParams, Distance
#qdrant_client = QdrantClient("localhost",port=6333)
qdrant_client = QdrantClient(
    url="https://c5748386-d8be-4bff-b52e-e88710a95438.eu-west-2-0.aws.cloud.qdrant.io:6333", 
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.dH4xAIqP1Tn8LlgrK-cwz8dDps6sDHzDwxyM8OkpZWI",
)

print(qdrant_client.get_collections())
'''
qdrant_client.create_collection(
    collection_name="test_collection",
    vectors_config=VectorParams(size=4, distance=Distance.COSINE),
)
op_info = qdrant_client.upsert(
    collection_name="test_collection",
    wait=True,
    points=[
        PointStruct(id=1, vector=[0.1, 0.2, 0.3, 0.4]),
        PointStruct(id=2, vector=[0.2, 0.3, 0.4, 0.5]),
    ],  
)

print(op_info)
'''
search_result = qdrant_client.query_points(
    collection_name="test_collection",
    query=[0.2,0.1,0.9,0.7],
    with_payload=False,
    limit=3,
).points

print(search_result)