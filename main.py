import basic

print("MAIN")

while True:
    text = input ('java Code >')
    result, error = basic.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)
