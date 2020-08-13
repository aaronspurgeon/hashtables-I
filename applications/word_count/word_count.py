def word_count(s):
    # Your code here
    hash_table = {}
    ignore = '":;,.-+=/\\|[]{}()*^&'
    lower = s.lower()

    for i in lower:
        if i in ignore:
            lower = lower.replace(i, '')
    words = lower.split()
    for j in words:
        if j not in hash_table:
            hash_table[j] = 1
        else:
            hash_table[j] += 1
    return hash_table


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
