myopenkey = ""

from langchain.document_loaders import TextLoader
loader = TextLoader(file_path="mypersonal.txt")
document = loader.load()


from langchain.text_splitter import CharacterTextSplitter
textChunk = CharacterTextSplitter(chunk_size=1000)
texts = textChunk.split_documents(document)
len(texts)

from langchain.embeddings import OpenAIEmbeddings
myembedmodel = OpenAIEmbeddings(openai_api_key=myopenkey)


mypinekey = "93eaf3db-f010-44ce-b795-f031de17"
from langchain.vectorstores import Pinecone
# pip  install pinecone-client
import pinecone
# Vector DB
pinecone.init(
    api_key=mypinekey,
    environment="gcp-starter"
)


docsearch = Pinecone.from_documents(
                documents=texts,
                embedding=myembedmodel,
                index_name="myspindex"
)

import os
os.environ["OPENAI_API_KEY"] = myopenkey



from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever()
)

myquery = "how is vimal daga, tell me in 10 words"
qa( { "query": myquery  })

