import random
number = random.randrange(0,100)

guessCheck = "wrong"
print("Welcome to number guessing")

while guessCheck == "wrong":
    response = int(input("Mohon input angka between 0 dan 100 : "))
    try:
        val=int(response)
    except ValueError:
        print("Ini bukan integer, tolong ulanga kembali!")
        continue

    val = int(response)
    if val < number:
        print("Ini lebih rendah dari angka sebenarnya. Silahkan coba lagi.")
    elif val > number:
        print("Ini lebih tinggi dari angka sebenarnya. Silahkan coba lagi.")
    else:
        print("Ini nomor yang benar")
        guessCheck = "Benar"

print("Terimakasih telah bermain!!")