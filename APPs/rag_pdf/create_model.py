from langchain_community.document_loaders import UnstructuredPDFLoader # PDF 파일 로드 모듈
from langchain.text_splitter import RecursiveCharacterTextSplitter # 텍스트 분할 모듈
from langchain_huggingface import HuggingFaceEmbeddings # 허깅페이스 임베딩 모듈
from langchain_community.vectorstores import FAISS # 벡터 스토어 모듈
from langchain.schema import Document # 문서 스키마 모듈 - 문서 객체 생성

# pdf 파일 docling 처리 및 로드
def load_and_process_pdf(file_path): # 파일 경로를 파라미터로 받음
  loader = UnstructuredPDFLoader(file_path) # 파일 로더 생성
  documents = loader.load() # 파일 로드

  processed_docs = [] # 처리된 문서 객체 저장 리스트 초기화
  for doc in documents:
    cleaned_text = doc.page_content.strip() # 문서 중 공백 제거
    cleaned_text = " ".join(cleaned_text.split()) # 공백 제거 후 문자열 합치기

    # 처리된 문서 목록 추가
    processed_docs.append(
      Document(
        page_content=cleaned_text, # 처리된 텍스트 페이지 콘텐츠 속서 값으로 지정
        metadata={"source": file_path} # 소스 파일 경로 추가
      )
    )
  return processed_docs

# 파일 로드 및 처리 후 확인
pdf_path = "./data/lawmang_cm.pdf"
documents = load_and_process_pdf(pdf_path)
# print(f"처리된 문서 수: {len(documents)}")

# 문서 내용 샘플
# print(documents[2])

# 문서 청크 생성 - 문서 내용 분할
def create_chunks(extracted_data):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""] # 청크 분리 기준
  )
  text_chunks = text_splitter.split_documents(extracted_data) # 문서 청크 생성
  return text_chunks

text_chunks = create_chunks(extracted_data=documents)
# print(f"문서 청크 수: {len(text_chunks)}")

# 벡터 임베딩 생성: 허깅페이스 모델 사용
def get_embedding_model():
  embedding_model = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask",
    model_kwargs={"device": "cpu"}, # 모델 실행 장치
    encode_kwargs={"normalize_embeddings": True} # 임베딩 정규화
  )
  return embedding_model

embedding_model = get_embedding_model()

# Faiss 벡터 스토어 생성
DB_FAISS_PATH = "vectorstore/db_faiss"
db = FAISS.from_documents(text_chunks, embedding_model) # 문서 청크와 임베딩 모델을 사용하여 벡터 스토어에 저장
db.save_local(DB_FAISS_PATH)