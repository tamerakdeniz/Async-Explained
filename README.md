# 🔄 Async-Explained

A simple demonstration project showing the difference between synchronous and asynchronous Python programming.

## 🎯 Purpose

This project provides two examples:
- A synchronous execution example in [main.py](main.py)
- An asynchronous execution example in [async-main.py](async-main.py)

The code demonstrates how async/await patterns can improve performance by running tasks concurrently.

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/tamerakdeniz/Async-Explained.git
cd Async-Explained
```

2. Make sure you have Python 3.13+ installed:
```bash
python --version
```

## 💻 Usage

### Running the Synchronous Example
```bash
python main.py
```
This will execute two functions sequentially, taking approximately 10 seconds total.

### Running the Asynchronous Example
```bash
python async-main.py
```
This will execute two functions concurrently, taking approximately 5 seconds total.

## 📊 Comparison

- **Synchronous (main.py)**: Functions run one after another
  - Total execution time: ~10 seconds
  - Blocks until each function completes

- **Asynchronous (async-main.py)**: Functions run concurrently
  - Total execution time: ~5 seconds
  - Non-blocking execution using asyncio
