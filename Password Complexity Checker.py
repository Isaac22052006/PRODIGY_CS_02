import string
import math

def check_password_strength(password):
    # Criteria weights (adjust these according to your preference)
    length_weight = 2
    lowercase_weight = 1
    uppercase_weight = 1
    digit_weight = 1
    special_char_weight = 2
    consecutive_weight = -3
    sequence_weight = -3

    # Initialize criteria counts
    length = len(password)
    lowercase_count = sum(1 for char in password if char.islower())
    uppercase_count = sum(1 for char in password if char.isupper())
    digit_count = sum(1 for char in password if char.isdigit())
    special_char_count = sum(1 for char in password if char in string.punctuation)

    # Check for consecutive characters
    consecutive_count = 0
    for i in range(len(password) - 1):
        if ord(password[i + 1]) == ord(password[i]) + 1:
            consecutive_count += 1

    # Check for common sequences (e.g., "abc", "123")
    sequence_count = 0
    for seq in ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789"]:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password:
                sequence_count += 1

    # Calculate strength score
    strength_score = (length * length_weight +
                      lowercase_count * lowercase_weight +
                      uppercase_count * uppercase_weight +
                      digit_count * digit_weight +
                      special_char_count * special_char_weight +
                      consecutive_count * consecutive_weight +
                      sequence_count * sequence_weight)

    # Calculate password entropy (in bits)
    charset = (string.ascii_lowercase if lowercase_count > 0 else "") + \
              (string.ascii_uppercase if uppercase_count > 0 else "") + \
              (string.digits if digit_count > 0 else "") + \
              (string.punctuation if special_char_count > 0 else "")
    charset_size = len(charset)
    entropy = length * math.log2(charset_size) if length > 0 and charset_size > 0 else 0

    # Determine strength level based on score
    if strength_score >= 100:
        strength_level = "Very Strong"
    elif strength_score >= 80:
        strength_level = "Strong"
    elif strength_score >= 60:
        strength_level = "Moderate"
    elif strength_score >= 40:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    # Provide feedback
    feedback = {
        "strength_score": strength_score,
        "strength_level": strength_level,
        "length": length,
        "lowercase_count": lowercase_count,
        "uppercase_count": uppercase_count,
        "digit_count": digit_count,
        "special_char_count": special_char_count,
        "consecutive_count": consecutive_count,
        "sequence_count": sequence_count,
        "entropy": entropy
    }

    return feedback

def main():
    print("Welcome to the Advanced Password Strength Evaluator!")
    while True:
        password = input("Enter your password to evaluate its strength (or 'quit' to exit): ").strip()

        if password.lower() == 'quit':
            break

        if len(password) == 0:
            print("Password cannot be empty. Please enter a password.")
            continue

        feedback = check_password_strength(password)

        print("\nPassword Strength Evaluation:")
        print(f"Strength Score: {feedback['strength_score']}")
        print(f"Strength Level : {feedback['strength_level']}")
        print(f"Length: {feedback['length']}")
        print(f"Lowercase Letters: {feedback['lowercase_count']}")
        print(f"Uppercase Letters: {feedback['uppercase_count']}")
        print(f"Digits: {feedback['digit_count']}")
        print(f"Special Characters: {feedback['special_char_count']}")
        print(f"Consecutive Characters: {feedback['consecutive_count']}")
        print(f"Common Sequences: {feedback['sequence_count']}")
        print(f"Entropy (bits): {feedback['entropy']:.2f}\n")

if __name__ == "__main__":
    main()
