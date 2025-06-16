import os # 파일 경로 설정 등에 사용
import sys # 한글 출력 인코딩에 사용
import io # 한글 출력 인코딩에 사용
from langchain import hub 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from collections import Counter

# openai 키 설정
from dotenv import load_dotenv
load_dotenv()
os.getenv("OPENAI_API_KEY")

# 출력 인코딩 utf-8 설정
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

class UTF8TextLoader(TextLoader):
  def __init__(self, file_path: str):
    super().__init__(file_path, encoding="utf-8")

loader = DirectoryLoader("./data", glob="*.txt", loader_cls=UTF8TextLoader)
documents = loader.load()
# print(len(documents))

# 텍스트 분할
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)
# print(len(texts))

# 벡터 스토어 생성
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents=texts, embedding=embeddings)
retriever = vectorstore.as_retriever()

# 대화 모델 생성 사전 프롬프팅 및 생성
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
  """당신은 질문-답변(Question-Answering)을 수행하는 친절한 AI 어시스턴트입니다. 당신의 임무는 주어진 문맥(context) 에서 주어진 질문(question) 에 답하는 것입니다.
  검색된 다음 문맥(context) 을 사용하여 질문(question) 에 답하세요. 만약, 주어진 문맥(context) 에서 답을 찾을 수 없다면, 답을 모른다면 `주어진 정보에서 질문에 대한 정보를 찾을 수 없습니다` 라고 답하세요.
  한글로 답변해 주세요. 단, 기술적인 용어나 이름은 번역하지 않고 그대로 사용해 주세요. 답변은 3줄 이내로 요약해 주세요.

  #Question: 
  {question} 

  #Context: 
  {context} 

  #Answer:"""
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

# 체인을 생성.
# RunnablePassthrough() : 데이터를 그대로 전달하는 역할. invoke 메서드를 통해 입력된 데이터를 그대로 반환
# StrOutputParser() : LLM이나 ChatModel에서 나오는 언어 모델의 출력을 문자열 형식으로 변환

# 체인 구성
rag_chain = (
  {"context": retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
)

# 질문 생성
# recieved_question = "청년을 위한 정책을 알려주세요"
recieved_question = sys.argv[1]

# 답변 생성
answer = rag_chain.invoke(recieved_question)
print(answer)