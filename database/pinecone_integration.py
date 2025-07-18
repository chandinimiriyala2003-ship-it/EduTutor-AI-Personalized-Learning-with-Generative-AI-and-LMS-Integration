import pinecone

def init_pinecone():
    pinecone.init(api_key="YOUR_API_KEY", environment="us-west1-gcp")
    index = pinecone.Index("edu-quizzes")
    return index