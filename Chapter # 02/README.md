## 🧵 Python Multithreading Examples

This project demonstrates **Python multithreading synchronization mechanisms** using simple and readable examples.
Each example uses the same shared task (`do_something.py`) but synchronizes access differently — with **Lock**, **RLock**, **Condition**, and **Semaphore**.

---

### 📂 Project Structure

```
multithreading_examples/
│
├── condition_example.py     # Uses threading.Condition
├── lock_example.py          # Uses threading.Lock
├── rlock_example.py         # Uses threading.RLock
├── semaphore_example.py     # Uses threading.Semaphore
├── do_something.py          # Common function used by all examples
└── README.md
```

---

### ⚙️ How It Works

The shared function `do_something(size, out_list)` performs a small computation and appends results to a shared list.
Each threading example controls access to this list differently:

| File                   | Synchronization Tool       | Description                                                       |
| ---------------------- | -------------------------- | ----------------------------------------------------------------- |
| `lock_example.py`      | **Lock**                   | Basic mutual exclusion; one thread writes at a time.              |
| `rlock_example.py`     | **RLock (Reentrant Lock)** | Allows the same thread to acquire the lock multiple times safely. |
| `condition_example.py` | **Condition**              | Enables threads to wait and notify based on shared state changes. |
| `semaphore_example.py` | **Semaphore**              | Limits how many threads can access a resource concurrently.       |

---

### 🧩 `do_something.py`

```python
import math

def do_something(size, out_list):
    """Performs a simple computation and appends results to the shared list."""
    results = [math.sqrt(i) ** 2 for i in range(size)]
    out_list.extend(results)
```

---

### ▶️ Running the Examples

Each example can be run individually:

```bash
python lock_example.py
python rlock_example.py
python condition_example.py
python semaphore_example.py
```

---

### 🧠 Concepts Demonstrated

* **Thread creation and management** using `threading.Thread`
* **Synchronization** using:

  * `Lock` for simple mutual exclusion
  * `RLock` for reentrant locking
  * `Condition` for signaling between threads
  * `Semaphore` for limiting concurrent access
* **Thread-safe data access** with shared resources (`out_list`)
* **Clean thread joining** to ensure graceful termination

---

### 📊 Sample Output (Semaphore Example)

```
[⏳] Thread 0 waiting for permit...
[🚀] Thread 0 started.
[⏳] Thread 1 waiting for permit...
[🚀] Thread 1 started.
[⏳] Thread 2 waiting for permit...
[✅] Thread 0 finished.
[🚀] Thread 2 started.
[✅] Thread 1 finished.
[✅] Thread 2 finished.

Final Output List: [0.0, 1.0, 2.0, ..., 6.0, 0.0, 1.0, ..., 6.0]
Length of list (Semaphore): 21
```

---

### 🏁 Summary

| Mechanism     | Use Case            | Key Feature                      |
| ------------- | ------------------- | -------------------------------- |
| **Lock**      | Protect shared data | Only one thread at a time        |
| **RLock**     | Recursive locking   | Same thread can re-acquire lock  |
| **Condition** | Thread coordination | Wait/notify mechanism            |
| **Semaphore** | Limit concurrency   | Control number of active threads |

---

### 👨‍💻 Author

Created as a learning project to demonstrate **Python’s threading synchronization primitives** in a simple and visual way.
