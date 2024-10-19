# 🌸 Bloom Filter

This repository contains an implementation of a Bloom Filter in Python. A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. It is highly space-efficient but allows for a small probability of false positives.

## 📄 Files

- `constants/config.py`: Contains configuration constants such as `MAX_ELEMENTS`, `ERROR_PROBABILITY`, and `MAX_ELEMENT_LENGTH`.
- `bloom_filter.py`: Contains the `BloomFilter` class which implements the Bloom Filter logic with 7 hash functions.
- `main.py`: The main script that reads input from a file, performs operations on the Bloom Filter, and prints the results.

## 🛠️ Requirements

- Python 3.x
- `bitarray` library
- `numpy` library

## 📥 Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/YuriiCodes/bloom-filter.git
    cd bloom-filter
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
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

2. Run the main script:
    ```sh
    python main.py
    ```

3. The script will output the results of the check operations.

## 🧮 Hash Functions

The implementation uses 7 random hash functions based on the formula:
```math
\[ h_{ab}(k) = ((a \cdot k + b) \mod p) \mod m \]
```
where:
- \( a \) and \( b \) are random integers chosen from the set \( Z^*_p \).
- \( p \) is a prime number greater than the maximum expected element length.
- \( m \) is the size of the Bloom Filter's bit array.
- \( k \) is the integer hash value of the input string.

These hash functions provide better distribution and minimize the probability of collisions, ensuring the desired false positive rate.

## ⚙️ Configuration

You can adjust the configuration parameters in `constants/config.py`:
- `MAX_ELEMENTS`: Maximum number of elements expected to be stored in the Bloom Filter.
- `ERROR_PROBABILITY`: Desired false positive probability.
- `MAX_ELEMENT_LENGTH`: Maximum length of an element to be added to the Bloom Filter.

## 📝 Example

An example `input.txt` file:
```
+ apple
+ banana
? apple
? cherry
+ grape
? banana
? grape
? orange
#
```

### Expected Output
```
Y
N
Y
Y
N
```