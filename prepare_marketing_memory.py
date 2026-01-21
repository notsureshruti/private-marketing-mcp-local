import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_all_md_files():
    content = []
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content.append(f"\n--- FILE: {path} ---\n")
                    content.append(f.read())
    return "\n".join(content)

context = read_all_md_files()

print("\n================ MARKETING OS MEMORY ================\n")
print("You are my private Marketing OS.")
print("Base every answer ONLY on the context below.")
print("If information is missing, ask questions instead of guessing.")
print("\nCONTEXT:\n")
print(context)
print("\n================ END MEMORY ================\n")
print("👉 Copy everything ABOVE this line.")
print("👉 Then run:  ollama run llama3")
print("👉 Paste once and start chatting.")
