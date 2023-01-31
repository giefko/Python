import random, string, substitution
def main():
    for i in range(1000):
        key = substitution.getRandomKey()
        message = random_string()
        print('Test %s: String: "%s.."' % (i + 1, message[:50]))
        print("Key: " + key)
        encrypted = substitution.translateMessage(message, key, 'E')
        decrypted = substitution.translateMessage(encrypted, key, 'D')

        if decrypted != message:
            print('ERROR: Decrypted: "%s" Key: %s' % (decrypted, key))
            sys.exit()
        print('Substutition test passed!')

def random_string(size = 5000, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
if __name__ == '__main__':
    main()