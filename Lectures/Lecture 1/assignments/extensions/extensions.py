prompt = input("File name: ").lower().strip()

 
if prompt.endswith(".gif"):
    print("image/gif")
elif prompt.endswith(".jpeg") or prompt.endswith(".jpg"):
    print("image/jpeg")
elif prompt.endswith(".png"):
    print("application/png)")
elif prompt.endswith(".zip"):
    print("application/zip)")
elif prompt.endswith(".pdf"):
    print("application/pdf)")
elif prompt.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")