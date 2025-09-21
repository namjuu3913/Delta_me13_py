from openai import OpenAI, BadRequestError, OpenAIError
from pathlib import Path
import json
import config as cfg

#load config
BIN:Path        = Path(cfg.SERVER_CONFIG["BIN"])
MODEL:Path      = Path(cfg.SERVER_CONFIG["MODEL"])
ALIAS:str       = cfg.SERVER_CONFIG["ALIAS"]
HOST:str        = cfg.SERVER_CONFIG["HOST"] 
PORT:int        = cfg.SERVER_CONFIG["PORT"]
NGL:int         = cfg.SERVER_CONFIG["NGL"]
CTX:int         = cfg.SERVER_CONFIG["CTX_SIZE"]
VERBOSE:bool    = cfg.SERVER_CONFIG["VERBOSE"]
BATCH_SIZE:int  = cfg.SERVER_CONFIG["BATCH_SIZE"]
FLASH_ATTN:bool = cfg.SERVER_CONFIG["FLASH_ATTN"]

class requestHandler:
    client : OpenAI
    temperature:float = 0.9
    max_tokens:int = 2000

    def __init__(self, client:OpenAI):
        self.client  = client

    def sendMsg(self, messages:json, turn_on_think:bool = False) -> str:
        try:
            r = self.client.chat.completions.create(
            model = ALIAS,
            messages = messages,
            temperature = self.temperature,
            max_tokens = self.max_tokens,
            )
            if(turn_on_think):
                return(f"CHAT:{r.choices[0].message.content}")
            else:
                return(f"CHAT:{self.cutThink(r.choices[0].message.content)}")

        except BadRequestError as e:
            # 400 본문을 그대로 출력해 원인 파악
            body = getattr(getattr(e, "response", None), "text", None)
            print("400 from server:", body or str(e))

    def cutThink(self, text:str) -> str | None:
        try:
            end_str = "</think>"
            end_idx = text.find(end_str) + len(end_str)

            if end_idx == -1:
                return None

            return text[end_idx:]

        except Exception:
            return None