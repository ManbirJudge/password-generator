import random
import sys
import argparse


def generate_password(args_):
    if args_.str == 'strong':
        lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_chars = ['!', '@', '#', '$', '%', '&', '^', '*', '+', '-']
        number_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        password_p1 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p2 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p3 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p4 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p5 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)

        password = password_p1 + password_p2 + password_p3 + password_p4 + password_p5

        return password

    elif args_.str == 'normal':
        lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_chars = ['!', '@', '#', '$', '%', '&', '^', '*', '+', '-']
        number_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0 ']

        password_p1 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p2 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p3 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)

        password = password_p1 + password_p2 + password_p3

        return password

    elif args_.str == 'medium':
        lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_chars = ['!', '@', '#', '$', '%', '&', '^', '*', '+', '-']
        number_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0 ']

        password_p1 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p2 = random.choice(lowercase_chars) + random.choice(special_chars) + random.choice(number_chars)
        password_p3 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(special_chars)

        password = password_p1 + password_p2 + password_p3

        return password

    elif args_.str == 'weak' or args_.str == 'easy':
        lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_chars = ['!', '@', '#', '$', '%', '&', '^', '*', '+', '-']
        number_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0 ']

        password_p1 = random.choice(lowercase_chars) + random.choice(uppercase_chars) + random.choice(
            special_chars) + random.choice(number_chars)
        password_p2 = random.choice(lowercase_chars) + random.choice(uppercase_chars)

        password = password_p1 + password_p2

        return password

    else:
        return 'You entered something wrong!!'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--str', type=str, default='strong', help='Specifies strength of your password.\nValid Values '
                                                                  'are: strong, normal, medium and weak ( or easy '
                                                                  ').\nNOTE: Normal is Stronger than Medium. Why? '
                                                                  'IDK.')

    args = parser.parse_args()

    sys.stdout.write(str(generate_password(args)))
