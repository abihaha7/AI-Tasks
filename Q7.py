def logger():
    count = 0
    def log_message(msg):
        nonlocal count
        count += 1
        print(f"[{count}] {msg}")
    return log_message

# Example Usage
log = logger()
log("First log")
log("Second log")
