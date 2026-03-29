import subprocess

newText = "World hello"

result = subprocess.run(
    ["cat"],
    input=newText,
    capture_output=True,
    text=True
)

print(result.stdout)