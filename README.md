
## About the Project
Delta-me13 Python Prototype is a character chatbot that runs locally using a quantized GGUF LLM and multilingual sentence embeddings. It aims to provide responsive, multilingual dialog while keeping resource usage modest.

**Highlights**
- Multilingual conversations via `paraphrase-multilingual-mpnet-base-v2`
- Local LLM (GGUF) inference for privacy and speed
- FAISS-based vector search for fast retrieval over dialogue/context


### Installation

Follow these steps to set up the project environment locally. This guide covers installing necessary system-level dependencies, setting up a Python virtual environment, and downloading the required models.

1.  **Prerequisites**
    Before you begin, ensure you have the following software installed on your system.
    
    * Python 3.11: This code is based on Python 3.11
        * You can download it from the [Python Downloads](https://www.python.org/downloads/)
    * NVIDIA CUDA Toolkit 12.9: Required for GPU acceleration.
        * You can download it from the [NVIDIA CUDA Toolkit Archive.](https://developer.nvidia.com/cuda-12-9-0-download-archive)
    * Git LFS (Large File Storage): This project uses Git LFS to manage large model files.
        * Download and install it from the [official Git LFS website.](https://git-lfs.com/) After installing, run ``` git lfs install``` in your terminal once to initialize it.
          
3.  Setup Steps
    1. Clone the Repository
    ```sh
    git clone https://github.com/namjuu3913/Delta_me13_py.git
    ```
    
    2. Navigate to the project directory.
    ```sh
    cd Delta_me13_py
    ```
    
    3. Create a Python Virtual Environment
       We recommend using a virtual environment to isolate project dependencies. The following command will create a folder named .venv in your project directory.
    ```sh
    
    python -m venv .venv
    ```
    
    4. Activate the Virtual Environment
        You must activate the environment before installing packages.
       * On Windows (PowerShell/CMD):
         ```sh
            .\.venv\Scripts\Activate
         ```
       * On macOS/Linux (Bash/Zsh):
         ```sh
            source .venv/bin/activate
         ```
        (I'm not sure it will work on macOS and Linux)
    
    5. Install Required Python Packages
        Install all the necessary libraries from the requirements.txt file into your active virtual environment.
         ```sh
            pip install -r requirements.txt
         ```

    6. Download Large Model Files
       Finally, pull the large model and data files managed by Git LFS.
     ```sh
     git lfs pull
     ```
     
 4. Download Models
   * #### LLM (GGUF)
     
     You can download any GGUF-formatted model from [huggingface](https://huggingface.co/) in the ```AI/models``` folder.
     
     Recommended & tested: Qwen3-14B-Q4_K_M, (see the model on [Hugging Face](https://huggingface.co/Qwen)
     
   * #### Sentence transformer model
   
     Use paraphrase-multilingual-mpnet-base-v2 model.

     Put the file in the ```projecfile/Character/models``` file

     Model: [Sentence-Transformers page.](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2). 



You are now ready to run the project!


### License

This project is distributed under the MIT License. See the ```LICENSE``` file for details.


### Acknowledgments & Key Dependencies

* NVIDIA CUDA Toolkit — GPU computing platform and model. Version 12.9 used here. 

    License: NVIDIA Software License Agreement.

* PyTorch — Deep learning framework for research to production.

    License: BSD-style.

* Hugging Face Transformers — Pretrained models for text/vision/audio.

    License: Apache 2.0.

* Sentence Transformers — State-of-the-art sentence/text/image embeddings.

    License: Apache 2.0.

* Faiss — Efficient similarity search and clustering for dense vectors.

    License: MIT.


