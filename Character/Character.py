﻿import json
from Character.Fuli import Fuli
from pathlib import Path

class Character:
    def __init__(self, char_name:str, GM:int = 10, LTM:int = 5):
        char_data_path = Path(__file__).resolve().parent/"CharacterSave"/char_name/f"{char_name}.json"
        print(char_data_path)
        with open(f"{char_data_path}", "r", encoding="utf-8") as f:
            char_data = json.load(f)
        self.name = char_data["name"]
        self.sex = char_data["sex"]
        self.MBTI = char_data["MBTI"]
        self.age = char_data["age"]
        self.back_story = char_data["back_story"]
        self.constraints = char_data["constraints"]
        self.safety = char_data["safety"]

        self.memory = Fuli(self.name)

        self.short_term_mem_num:int = GM
        self.long_term_mem_num:int = LTM

        self.last_coversation:json

    def updateMemory(self, user_input:dict):
        self.memory.add_conversation(user_input)
        self.memory.saveDB()

    def updateLastConversation(self,):
        self.last_coversation

    #get conversations from last general_mem_max turns
    def getShortTermMem(self) -> str:  
        return self.memory.searchGDB(self.short_term_mem_num)

    #memory from vector database(num = long_term_mem_num)
    def getLongTermMem(self, user_input:str):
        return self.memory.searchVDB(user_input, self.long_term_mem_num)
        
    # list[dict] to str -> Not using now
    def format_conversations_to_string(self,conversations: list[dict]) -> str:
        if not conversations:
            return "No related conversation"
        formatted_list = [f"User: {conv['user']}\n{self.name}: {conv['from_you']}" for conv in conversations]
        return "\n\n".join(formatted_list)

    #get total memory
    def getMemoryForLLM(self, user_input:str) -> dict:
        return {
            f"conversations from last {self.long_term_mem_num} turns" : self.getShortTermMem(),
            "relative conversations from DB" : self.getLongTermMem(user_input)
            }

    def changeNumOfMem(self, num_vdb, num_gdb) -> None:
        if num_vdb:
            self.long_term_mem_num = num_vdb
        if num_gdb:
            self.short_term_mem_num = num_gdb

    def getMemoryForUser(self) -> json:
        return (f"""
        conversations from last {self.long_term_mem_num} turns:\n
        {self.getShortTermMem()}\n
        \n
        relative conversations from DB:\n
        {self.memory.getRandomVDB(10)}"""
        )
        
    def getCharJsonLLM(self, user_input:str) -> json:
        j:json = {
            "name"          : self.name,
            "MBTI"          : self.MBTI,
            "sex"           : self.sex,
            "age"           : self.age,
            "backstory"     : self.back_story,
            "contsraints"   : self.constraints,
            "safety"        : self.safety,
            "memory"        : self.getMemoryForLLM(user_input)
            }
        return j

    def getCharInfo(self) -> json:
        j:json = {
            "name"          : self.name,
            "MBTI"          : self.MBTI,
            "sex"           : self.sex,
            "age"           : self.age,
            "backstory"     : self.back_story,
            "contsraints"   : self.constraints,
            "safety"        : self.safety,
            "memory"        : self.getMemoryForUser()
            }
        return j



