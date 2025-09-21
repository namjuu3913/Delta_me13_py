# config.py
"""
A file that manages the main settings of the application.
Defines the path, network information, model parameters, etc. required to run the server.
"""

import sys
from pathlib import Path

# BASE location
if getattr(sys, 'frozen', False):
    #.exe 
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    #.py 
    BASE_DIR = Path(__file__).resolve().parent

# Llama.cpp server
SERVER_CONFIG = {
    # model and llama.cpp location
    "BIN": BASE_DIR / "AI" / "llama-b6347-bin-win-cuda-12.4-x64" / "llama-server.exe",
    "MODEL": BASE_DIR / "AI" / "models" / "Qwen3-14B-Q4_K_M.gguf",

    # network config
    "HOST": "127.0.0.1",
    "PORT": 8000,

    # model performance and parameter
    "CTX_SIZE": 8192,        # Total tokens
    "NGL": -1,               # GPU layers(-1 means put everything on gpu)
    "ALIAS": "qwen3-14b",    # Alias to use to identify models in the API

    # server options
    "VERBOSE": True,         # Will it print detailed logs?
    "BATCH_SIZE": 1024,      # Batch size for prompt
    "FLASH_ATTN": True,      # Use Flash Attention or not
    }




