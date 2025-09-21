


### Installation

Follow these steps to set up the project environment locally. This guide covers installing necessary system-level dependencies, setting up a Python virtual environment, and downloading the required models.

1.  **Prerequisites**
    Before you begin, ensure you have the following software installed on your system.
    *Python 3.11: This code is based on Python 3.11
      * You can download it from the [Python Downloads](https://www.python.org/downloads/)
    * NVIDIA CUDA Toolkit 12.9: Required for GPU acceleration.
      * You can download it from the [NVIDIA CUDA Toolkit Archive.](https://developer.nvidia.com/cuda-12-9-0-download-archive)

3.  Clone the repository.
    ```sh
    git clone [https://github.com/namjuu3913/Delta_me13_py.git](https://github.com/namjuu3913/Delta_me13_py.git)
    ```

4.  Navigate to the project directory.
    ```sh
    cd Delta_me13_py
    ```

5.  **Download the large model files** using Git LFS.
    ```sh
    git lfs pull
    ```

6.  Install the required Python packages.
    ```sh
    pip install -r requirements.txt
    ```
