def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))