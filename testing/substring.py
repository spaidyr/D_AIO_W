from time import perf_counter


def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)


def main():
    filenames = [
        './temp/test1.txt',
        './temp/test2.txt',
        './temp/test3.txt',
        './temp/test4.txt',
        './temp/test5.txt',
        './temp/test6.txt',
        './temp/test7.txt',
        './temp/test8.txt',
        './temp/test9.txt',
        './temp/test10.txt',
    ]

    for filename in filenames:
        replace(filename, 'ids', 'id')


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
