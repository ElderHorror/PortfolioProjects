

class PasswordGenerator:
    def __init__(self):
        self.nr_letters = random.randint(8, 10)
        self.nr_symbols = random.randint(2, 4)
        self.nr_numbers = random.randint(2, 4)
        self.password_list = []
        self.generate_password()

    def generate_password(self):
        for i in range(0, self.nr_letters):
            letter = random.choice(LETTERS)
            self.password_list.append(letter)
        for i in range(0, self.nr_symbols):
            symbols = random.choice(SYMBOLS)
            self.password_list.append(symbols)
        for i in range(0, self.nr_numbers):
            numbers = random.choice(NUMBERS)
            self.password_list.append(numbers)
        random.shuffle(self.password_list)

    def final(self):
        generated_pass = ""
        for _ in self.password_list:
            generated_pass.append(_)
        return generated_pass
