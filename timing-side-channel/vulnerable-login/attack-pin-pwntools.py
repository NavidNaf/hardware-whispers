from pwn import *
import string
import time

PIN_LENGTH = 8
TRIALS_PER_GUESS = 7


def test_pin(pin):
    start_time = time.perf_counter_ns()

    p = process("./pin_checker")
    p.sendline(pin)
    p.recvall(timeout=1)
    p.close()

    end_time = time.perf_counter_ns()
    return end_time - start_time

def guess_pin(length):
    guessed_pin = ""

    for pos in range(length):
        best_digit = ""
        best_time = 0.0

        for digit in '0123456789':
            candidate = guessed_pin + digit + ("0" * (length - pos - 1))
            duration = test_pin(candidate)
            print(f"Trying PIN: {candidate} -> Time: {duration:.2f}s")
            if duration > best_time:
                best_time = duration
                best_digit = digit

        guessed_pin += best_digit
        print(f"Recovered so far: {guessed_pin}")

    return guessed_pin

def main():
    pin = guess_pin(PIN_LENGTH)
    print(f"\nGuessed PIN: {pin}")

if __name__ == "__main__":
    main()
