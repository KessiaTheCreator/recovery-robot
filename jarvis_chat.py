import os
import sys
from llama_cpp import Llama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Paths
BASE_DIR = os.path.expanduser("~/recovery_robot")
MODEL_PATH = os.path.join(BASE_DIR, "llama.cpp/recovery_voice.gguf")
# This points directly to the binary file
PIPER_BIN = os.path.join(BASE_DIR, "venv/bin/piper")
# This points to the model file we just downloaded
VOICE_MODEL = os.path.join(BASE_DIR, "en_GB-alan-medium.onnx")
VECTOR_STORE = os.path.join(BASE_DIR, "knowledge_base_vector/vector_store")
PROMPT_FILE = os.path.join(BASE_DIR, "jarvis_system_prompt.txt")

# Load Brain
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, verbose=False)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory=VECTOR_STORE, embedding_function=embeddings)

def speak(text):
    clean = text.replace('"', '').replace('*', '').replace('#', '').replace('\n', ' ')
    # We call the binary directly, ignoring the python library's internal requirements
    cmd = f'echo "{clean}" | {PIPER_BIN} --model {VOICE_MODEL} --output_file response.wav'
    os.system(cmd)
    os.system('aplay -q response.wav')

def get_response(user_input):
    with open(PROMPT_FILE, "r") as f:
        system = f.read()
    docs = db.similarity_search(user_input, k=2)
    context = "\n".join([d.page_content for d in docs])
    prompt = f"System: {system}\nContext: {context}\nUser: {user_input}\nJarvis:"
    response = llm(prompt, max_tokens=100, stop=["User:", "\n"], echo=False)
    return response['choices'][0]['text']

print("Jarvis is online.")
while True:
    user_q = input("\nYou: ")
    if user_q.lower() == "exit": break
    answer = get_response(user_q)
    print("Jarvis:", answer)
    speak(answer)
