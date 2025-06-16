import os
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage # 메시지 타입 정의
from langchain_core.runnables import RunnableWithMessageHistory # 메시지 기록 처리
from langchain_core.chat_history import BaseChatMessageHistory # 채팅 기록 처리

from langchain_huggingface import HuggingFaceEndpoint # 허깅페이스 엔드포인트 모듈
from langchain_core.prompts import PromptTemplate # 프롬프트 템플릿 모듈
from langchain.chains import RetrievalQA # 검색 체인 모듈
from langchain_huggingface import HuggingFaceEmbeddings # 허깅페이스 임베딩 모듈
from langchain_community.vectorstores import FAISS # FAISS 벡터 스토어 모듈
from dotenv import load_dotenv # 환경 변수 로드 모듈

# 환경 변수 로드
load_dotenv()

# 허깅페이스 API 키 설정
HF_TOKEN = os.environ.get("HF_TOKEN")
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3" # LLM 모델 저장

# 허깅페이스 LLM 모델 초기화 함수
def load_llm(huggingface_repo_id):
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repo_id,
        temperature=0.1,
        # 확률 집중 파라미터 - 확률 집중 파라미터는 확률 분포에서 샘플링을 위한 확률 집중 파라미터입니다. 0.9는 90%의 확률 집중을 의미.
        # top_p 값이 낮을수록 보수적인 출력, 높을수록 다양하고 창의적인 출력.
        top_p=0.9,
        # 반복 금지 패널티 설정
        # 1.0 : 아무런 패널티 없이 일반 생성과 동일
        # 1.0보다 작으면 반복을 오히려 장려
        # 높으면 반복 금지
        repetition_penalty=1.0, 
        do_sample=False, # 샘플링 사용 없이 최대 확률 답변 생성
        # model_kwargs={
        #     "token" : HF_TOKEN ,
        #     "max_length" : 512
        # }
        max_new_tokens = 1000,
        huggingfacehub_api_token=HF_TOKEN
    )
    return llm

# QA 시스템을 위한 프롬프트 템플릿 정의
CUSTOM_PROMPT_TEMPLATE = """
당신은 주어진 문서의 내용만을 기반으로 답변하는 AI 어시스턴트입니다.
절대로 문서에 없는 내용으로 답변을 생성하지 마세요.
문서의 내용에 관련된 답변이 없다면 "주어진 문서에서 관련 정보를 찾을 수 없습니다."라고 답변하세요.
답변은 반드시 한글로 답변하세요.


컨텍스트: {context}
질문: {question}


답변은 문서의 내용만을 기반으로 작성하세요:
"""

# 프롬포트 템플릿 설정 함수
def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["context" ,"question"])
    return prompt

# FAISS 데이터 베이스 설정
DB_FAISS_PATH = "vectorstore/db_faiss"
embedding_model = HuggingFaceEmbeddings(model_name="jhgan/ko-sroberta-multitask")

# 텍스트 임베딩 함수
def embed_text(text):
    if isinstance(text, list):
        text = " ".join(str(t) for t in text)
    return embedding_model.embed_query(text)

# 데이터베이스 로드
db = FAISS.load_local(
    DB_FAISS_PATH,
    embed_text,
    # 보안 경고를 무시하고 잠재적으로 위험한 객체를 직열화 할지 여부
    # 로컬 pickle 파일의 경우 일반적으로 True 설정
    allow_dangerous_deserialization=True
)

# 채팅 기록을 메모리에 저장
class InMemoryHistory(BaseChatMessageHistory):
    def __init__(self):
        self.messages : List[BaseMessage] = [] # 메모리에 저장되는 메시지 초기화

    def add_message(self, message: BaseMessage) -> None: # void 표현
        self.messages.append(message) # 메세지 추가

    def clear(self) -> None:
        self.messages = [] # 메모리에 저장된 메세지 목록 초기화

# QA 체인 생성 및 채팅 형식으로 변환
def get_chat_chain():
    chain = RetrievalQA.from_chain_type(
        llm=load_llm(HUGGINGFACE_REPO_ID),
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={'k' : 3}), # 검색 결과 수 설정
        return_source_documents=True, # 문서 출처 반환 여부
        chain_type_kwargs={
            "prompt" : set_custom_prompt(CUSTOM_PROMPT_TEMPLATE),
        }# 사용자 정의 프롬포트 설정
    )

    # 세션 클래스 호출 함수
    def get_session_history():
        return InMemoryHistory()

    # 체인 생성
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="query",
        output_messages_key="result",
    )
    return chain_with_history

# 메인 실행 함수
if __name__ == "__main__":
    chat_chain = get_chat_chain() # 채팅 체인 생성
    session_id = "default"
    
    while True:
        user_query = input("질문을 입력하세요(종료는 q) : ")
        if user_query.lower() == "q":
            break
        response = chat_chain.invoke(
            {"query": user_query},
            config={"configurable": {"session_id": session_id}}
        )
        print("답변: ", response['result'])