# 🌸 Bloom Filter

This repository contains an implementation of a Bloom Filter in Python. A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. It is highly space-efficient but allows for a small probability of false positives.

## 📄 Files

- `constants/config.py`: Contains configuration constants such as `MAX_ELEMENTS`, `ERROR_PROBABILITY`, and `MAX_ELEMENT_LENGTH`.
- `bloom_filter.py`: Contains the `BloomFilter` class which implements the Bloom Filter logic.
- `main.py`: The main script that reads input from a file, performs operations on the Bloom Filter, and prints the results.

## 🛠️ Requirements

- Python 3.x
- `bitarray` library
- `mmh3` library
- `numpy` library

## 📥 Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/YuriiCodes/bloom-filter.git
    cd bloom-filter
    ```

2. Install the required libraries:
    ```sh
    pip install bitarray mmh3 numpy
    ```

## 🚀 Usage

1. Prepare an input file named `input.txt` with the following format:
    ```
    + item1
    ? item2
    #
    ```
    - `+ item1`: Add `item1` to the Bloom Filter.
    - `? item2`: Check if `item2` is in the Bloom Filter.
    - `#`: Break the operation.

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the main script:
    ```sh
    python main.py
    ```

4. The script will output the results of the check operations.

## ⚙️ Configuration

You can adjust the configuration parameters in `constants/config.py`:
- `MAX_ELEMENTS`: Maximum number of elements expected to be stored in the Bloom Filter.
- `ERROR_PROBABILITY`: Desired false positive probability.
- `MAX_ELEMENT_LENGTH`: Maximum length of an element to be added to the Bloom Filter.

