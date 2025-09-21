import os, json
from Character.Character import Character
from pathlib import Path

class CharacterHandler:
    charac_save_path: Path = Path(__file__).resolve().parent / "CharacterSave"

    #Check there is a character folder in CharacterSave
    def checkCharacter(self, name_charac:str) -> bool:
        for name_charac in os.listdir(self.charac_save_path):
            target_path = os.path.join(self.charac_save_path, name_charac)
            if (os.path.isdir(target_path)):
                return True
        
        return False

    #Make new Character
    def makeNewCharacter(self):
        #Choose character name
        name_of_char:str
        while True:
            name_of_char = input("Character name: ")
            if not name_of_char:
                print("Name cannot be empty.")
                continue

            temp_in = input(f"Is {name_of_char} correct? (Y : N : exit): ")

            if temp_in.upper() == "Y":
                break
            elif temp_in.upper() == "N":
                continue
            elif temp_in.upper() == "EXIT":
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
        except Exception as e:
            print(f"\nAn error occurred while saving the JSON file: {e}")
