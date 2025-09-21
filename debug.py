import sys
from pathlib import Path

# --- 이 부분은 사용자의 실제 설정과 유사하게 구성했습니다 ---
# 프로젝트의 기본 경로를 이 파일의 위치를 기준으로 설정합니다.
BASE_DIR = Path(__file__).parent

# llama-server.exe 파일의 경로를 지정합니다.
BIN_DIR = BASE_DIR / "AI" / "llama-b6347-bin-win-cuda-12.4-x64"
BIN = BIN_DIR / "llama-server.exe"

# ---------------------------------------------------------------------
# !!! 중요 !!!
# 아래 파일 이름을 실제 가지고 있는 GGUF 모델 파일 이름으로 정확히 수정해주세요.
MODEL_FILENAME = "Qwen3-14B-Q4_K_M.gguf" 
# ---------------------------------------------------------------------
MODEL = BASE_DIR / "AI" / "models" / MODEL_FILENAME

# 서버 실행을 위한 기본 설정값들
ALIAS = "model"
HOST = "127.0.0.1"
PORT = 8080
NGL = 999 # GPU 레이어 수 (테스트를 위해 낮게 설정 가능)
CTX = 4096
BATCH_SIZE = 512

print("="*50)
print("[DEBUG] 테스트 스크립트를 시작합니다.")
print(f"Python Executable: {sys.executable}")
print("="*50)

# --- 실행할 명령어 리스트 생성 (기존 코드와 동일한 로직) ---
cmd = [
    str(BIN),
    "--model",        str(MODEL),
    "--alias",        ALIAS,
    "--host",         HOST,
    "--port",         str(PORT),
    "--n-gpu-layers", str(NGL),
    "--ctx-size",     str(CTX),
    "--batch-size",   str(BATCH_SIZE),
]

# 최종적으로 실행될 명령어 문자열 생성
final_command_string = " ".join(f'"{a}"' if " " in str(a) else str(a) for a in cmd)

print("\n[진단] 만약 이 메시지가 보인다면, 파이썬 환경은 정상입니다.")
print("\n[최종 명령어] 아래 명령어를 복사해서 CMD에서 직접 실행해보세요:\n")
print(final_command_string)
print("\n[진단 완료] 이 메시지까지 보이면 스크립트가 성공적으로 끝난 것입니다.")
