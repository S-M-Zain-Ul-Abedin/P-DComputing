import threading
import multiprocessing
import time

# ---------- DFA CLASS ----------
class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def validate_string(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            next_state = self.transition_function.get((current_state, symbol))
            if next_state is None:
                return False
            current_state = next_state
        return current_state in self.accept_states


# ---------- EXAMPLE DFA ----------
# DFA that accepts binary strings ending with '0'
states = {"q0", "q1"}
alphabet = {"0", "1"}
transition_function = {
    ("q0", "0"): "q0",
    ("q0", "1"): "q1",
    ("q1", "0"): "q0",
    ("q1", "1"): "q1",
}
start_state = "q0"
accept_states = {"q0"}

dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# ---------- TEST STRINGS ----------
test_strings = ["010", "1100", "1111", "000", "1010", "1110", "0001", "0010"] * 1000  # increase workload


# ---------- TASK FUNCTION ----------
def run_dfa_tests():
    for string in test_strings:
        dfa.validate_string(string)


# ---------- MULTIPROCESSING FUNCTION ----------
def process_task():
    run_dfa_tests()


if __name__ == "__main__":
    # ---------- MULTITHREADING TEST ----------
    thread_counts = [5, 10, 15]
    for count in thread_counts:
        threads = []
        start_time = time.time()
        for _ in range(count):
            t = threading.Thread(target=run_dfa_tests)
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        end_time = time.time()
        print(f"🧵 Threads: {count} | Time taken: {end_time - start_time:.4f} seconds")

    # ---------- MULTIPROCESSING TEST ----------
    process_counts = [5, 10, 15]
    for count in process_counts:
        processes = []
        start_time = time.time()
        for _ in range(count):
            p = multiprocessing.Process(target=process_task)
            processes.append(p)
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        end_time = time.time()
        print(f"⚙️ Processes: {count} | Time taken: {end_time - start_time:.4f} seconds")
