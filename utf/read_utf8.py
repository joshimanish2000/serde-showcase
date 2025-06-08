def read_utf8(fileName: str) -> None:
    with open(fileName, "r", encoding="utf-16") as f:
        content = f.read()
        print(content)
    
read_utf8("la_utf16.txt")