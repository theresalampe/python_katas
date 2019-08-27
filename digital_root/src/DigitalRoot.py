class DigitalRoot:

    def digital_root_1(n):
        n = str(n)
        while len(n) > 1:
            result = 0
            for i in range(0, len(n)):
                result += int(n[i])
            n = str(result)
        return result

    def digital_root(n):
        return n % 9 or n and 9
