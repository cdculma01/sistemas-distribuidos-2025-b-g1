# palindrome.py
def is_palindrome(text):
    """Verifica si una palabra es un palíndromo."""
    return text.lower() == text.lower()[::-1]

if __name__ == "__main__":
    word = input("Ingresa una palabra para verificar: ")
    if is_palindrome(word):
        print(f"'{word}' es un palíndromo.")
    else:
        print(f"'{word}' no es un palíndromo.")