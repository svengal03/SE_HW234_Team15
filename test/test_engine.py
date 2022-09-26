from test import test_sample

def main():
    result = 0
    result += 1 if test_sample.test_the() else 0
    result += 1 if test_sample.test_num() else 0
    result += 1 if test_sample.test_sym() else 0
    result += 1 if test_sample.test_bignum() else 0
    result += 1 if test_sample.test_data() else 0
    result += 1 if test_sample.test_stats() else 0
    result += 1 if test_sample.test_csv() else 0
    print(result, " tests failed")
    print(7 - result, " tests passed")
    return result

if __name__ == '__main__':
    main()
