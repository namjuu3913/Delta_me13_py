import os, json
from Character.Character import Character
from pathlib import Path
from typing import List

class CharacterHandler:
    charac_save_path: Path = Path(__file__).resolve().parent / "CharacterSave"

    #Check there is a character folder in CharacterSave
    def checkCharacter(self, name_charac: str) -> bool:
        target_path = self.charac_save_path / name_charac
        return target_path.is_dir()
    
    #Prompt the user to enter multiple lines (one item per line).
    #Finish by pressing Enter on an empty line or typing END/DONE/QUIT/Q.
    #Returns a list of non-empty, stripped strings.
    def _get_user_input_list(self, prompt: str) -> List[str]:     
        print(prompt)
        print("(Finish with an empty line or type END/DONE/QUIT/Q)")
        items: List[str] = []
        while True:
            try:
                line = input().strip()
            except (EOFError, KeyboardInterrupt):
                print("\nInput cancelled by user.")
                break

            if line == "" or line.upper() in {"END", "DONE", "QUIT", "Q"}:
                break
            items.append(line)
        return items

    #Make new Character
    def makeNewCharacter(self,name_of_char:str):
        while True:
            temp_in = input(f"Is {name_of_char} correct? (Y : N): ")

            if temp_in.upper() == "Y":
                break
            elif temp_in.upper() == "N":
                print("Character creation cancelled.")
                return 
            else:
                print("Invalid input! Please enter Y, N, or exit.")
        
        #Making VDB, GDB and root folder
        print(f"\nCreating folder for character '{name_of_char}'...")
        try:
            character_root_path = self.charac_save_path / name_of_char
            general_db_path = character_root_path / "GeneralDB"
            vector_db_path = character_root_path / "VectorDB"

            os.makedirs(general_db_path, exist_ok=True)
            os.makedirs(vector_db_path, exist_ok=True)
            print(f"Successfully created folder for '{name_of_char}'!")

        except Exception as e:
            print(f"An error occurred while creating folders: {e}")
            return

        #Make character.json
        print("""
-----------------------------------------------------------------------
Now, please enter the character's detailed information.
Finish lists with an empty line or type END/DONE/QUIT/Q.
The example below shows the format you will be following.

Example:
{
    "name": "Kaelus",
    "sex": "Male",
    "MBTI": "INTP",
    "age": "Unknown (Records Lost)",
    "back_story": "I am Kaelus, the last librarian of the 'Starlight Archive,'...",
    "constraints": [
        "Your personality must be based on your MBTI.",
        "You must adhere to the role of 'Kaelus' until the end, not an AI.",
        ...
    ],
    "safety": [
        "Never ask for or record personal information.",
        "Politely refuse unethical or dangerous requests...",
        ...
    ]
}
-----------------------------------------------------------------------
        """)

        new_persona = {
            "name": name_of_char,
            "sex": input("Sex: "),
            "MBTI": input("MBTI: ").upper(),
            "age": input("Age: "),
            "back_story": input("Backstory:\n"),
            "constraints": self._get_user_input_list("Enter character constraints (one per line):"),
            "safety": self._get_user_input_list("Enter safety settings (one per line):")
        }

        #save it as json file
        try:
            with open(character_root_path, 'w', encoding='utf-8') as f:
                json.dump(new_persona, f, ensure_ascii=False, indent=4)
            print(f"\nSuccessfully saved character information to '{character_root_path}'!")

        except PermissionError:
            print("\n[ERROR] Permission Denied!")
            print(f"Could not write to the directory: {character_path}")
            print("Please check if your antivirus software or Windows Defender's 'Controlled Folder Access' is blocking the application.")
            return False

        except Exception as e:
            print(f"\nAn error occurred while saving the JSON file: {e}")
