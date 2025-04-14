def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("❌ File not found!")
    finally:
        try:
            file.close()
        except:
            pass

# Example Usage
read_file("example.txt")
