import subprocess
import time

def pin_attempt(pin):
    start = time.perf_counter()
    result = subprocess.Popen("./pin_checker", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result.stdin.write(f"{pin}\n")
    result.stdin.flush()
    output = result.stdout.readline()
    end = time.perf_counter()
    return end - start

def find_correct_pin():
    guessed_pin = ""

    for i in range(8):
        best_time = 0
        best_digit = ""

        for d in '0123456789':
            current_pin = guessed_pin + d + '0' * (7 - i)
            elapsed_time = pin_attempt(current_pin)

            if elapsed_time > best_time:
                best_time = elapsed_time
                best_digit = d
        guessed_pin += best_digit
        print(f"Guessed so far: {guessed_pin}")
    return guessed_pin

if __name__ == "__main__":
    correct_pin = find_correct_pin()
    print(f"Correct PIN found: {correct_pin}")
