# 🐍 Python Multiprocessing: Advanced Demonstrations

This README explores Python’s `multiprocessing` module with practical examples. It demonstrates creating, naming, synchronizing, managing, and terminating multiple processes using a shared CPU-bound function `do_something()` from `do_something.py`.

---

## ⚙️ 1. `process_monitoring.py`

**Goal:** Monitor a single process from start to termination using `.start()`, `.terminate()`, and `.join()`.

**Code Snippet:**

```python
process = multiprocessing.Process(target=run_task)
monitor_process(process)
```

**Output Example:**

```
[🔍] Before start: <Process ...> False
[⚙️] Running: <Process ...> True
[🛑] Terminated: <Process ...> False
[🔚] Joined: <Process ...> False
[📦] Exit code: -15
```

**Insight:** Safe lifecycle management of processes is demonstrated; processes can be monitored, terminated, and joined safely.

---

## ⚙️ 2. `sequential_processes.py`

**Goal:** Launch multiple processes **sequentially**, each waiting for the previous to finish.

**Code Snippet:**

```python
for i in range(6):
    proc = multiprocessing.Process(target=run_task, args=(i,))
    proc.start()
    proc.join()
```

**Output Example:**

```
[⚙️] Process 0 started
[✅] Process 0 finished with 0 results
...
[⚙️] Process 5 started
[✅] Process 5 finished with 5000 results
```

**Insight:** Sequential launching ensures predictable execution order, but **parallelism is not utilized**.

---

## ⚙️ 3. `concurrent_processes.py`

**Goal:** Launch multiple processes **concurrently**, then join them after all have started.

**Code Snippet:**

```python
processes = [multiprocessing.Process(target=run_task, args=(i,)) for i in range(6)]
for p in processes: p.start()
for p in processes: p.join()
```

**Output Example:**

```
[⚙️] Process 0 started
[⚙️] Process 1 started
...
[✅] Process 5 finished with 5000 results
```

**Insight:** Processes run in parallel, efficiently utilizing CPU cores.

---

## ⚙️ 4. `daemon_vs_non_daemon.py`

**Goal:** Compare **daemon** and **non-daemon** process behavior.

**Code Snippet:**

```python
bg_proc.daemon = True
fg_proc.daemon = False
```

**Output Example:**

```
[🚀] Starting background_process
[🚀] Starting NO_background_process
[✅] Exiting NO_background_process
```

**Insight:**

* **Daemon processes** terminate when the main program exits.
* **Non-daemon processes** run independently and finish their tasks.

---

## ⚙️ 5. `process_barrier.py`

**Goal:** Synchronize processes using `Barrier` and `Lock`.

**Code Snippet:**

```python
sync = Barrier(2)
lock = Lock()
Process(target=run_with_barrier, args=(sync, lock))
```

**Output Example:**

```
p1 - with_barrier ---> 2025-11-08 12:34:56
p1 - with_barrier results: [0.0, 1.0]
```

**Insight:**

* **Barrier** ensures a set of processes waits for each other.
* **Lock** prevents concurrent printing or shared data access issues.

---

## ⚙️ 6. `process_pool.py`

**Goal:** Use `Pool` to distribute tasks across multiple processes.

**Code Snippet:**

```python
with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(compute_square, inputs)
```

**Output Example:**

```
Pool: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Insight:** `Pool` efficiently manages worker processes for CPU-bound operations.

---

## ⚙️ 7. `parallel_worker_demo.py`

**Goal:** Run multiple workers with shared `do_something()` tasks using `multiprocessing.Manager().list()`.

**Code Snippet:**

```python
out_list1 = multiprocessing.Manager().list()
out_list2 = multiprocessing.Manager().list()
p1 = multiprocessing.Process(target=do_something, args=(size, out_list1))
p2 = multiprocessing.Process(target=do_something, args=(size, out_list2))
p1.start(); p2.start(); p1.join(); p2.join()
```

**Output Example:**

```
Worker-1 output length: 1000
Worker-2 output length: 1000
```

**Insight:** Shared manager lists allow safe inter-process communication.

---

### 📊 Summary Table

| Script                    | Purpose                                 | ✅ | Key Insight                                 |
| ------------------------- | --------------------------------------- | - | ------------------------------------------- |
| `process_monitoring.py`   | Monitor & terminate a process           | ✅ | Safe process lifecycle management           |
| `sequential_processes.py` | Sequential process execution            | ✅ | Predictable, single-core execution          |
| `concurrent_processes.py` | Parallel process execution              | ✅ | Efficient CPU utilization                   |
| `daemon_vs_non_daemon.py` | Compare daemon vs non-daemon processes  | ✅ | Daemons exit with main; non-daemons persist |
| `process_barrier.py`      | Synchronize processes with Barrier/Lock | ✅ | Ordered execution & shared resource safety  |
| `process_pool.py`         | Parallelism using Pool                  | ✅ | Automatic workload distribution             |
| `parallel_worker_demo.py` | Multiple workers sharing data           | ✅ | Manager.list enables inter-process sharing  |

---

### 🧠 Final Takeaways

* Multiprocessing enables **true parallelism** for CPU-bound tasks.
* **Sequential vs concurrent** launching affects performance and predictability.
* **Daemon processes** are tied to the main program lifecycle; non-daemons run independently.
* **Barrier and Lock** help synchronize processes and protect shared resources.
* **Pool** simplifies workload distribution across multiple processes.
* **Manager lists** allow safe data sharing between processes.
