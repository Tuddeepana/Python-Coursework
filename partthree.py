# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#student id - 20222416
#Date - 2023.4.20


print("PART 1:")

credit_range = [0, 20, 40, 60, 80, 100, 120]
f_v_count = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progress_data = []
pass_c = defer_c = fail_c = 0
flag = True


def get_credit_input(message):
    while True:
        try:
            credit = int(input(message))
            if credit not in credit_range:
                print('Out of range')
            else:
                return credit
        except ValueError:
            print('Integer required')


def call(flag):
    global pass_c, defer_c, fail_c, pro, p_m, d_p, exclu, total, f_v_count, progress_count, trailer_count, retriever_count, exclude_count, progress_data

    while True:
        if flag:
            pass_c = get_credit_input('Please enter your credits at pass\t: ')
            defer_c = get_credit_input('Please enter your credits at defer\t: ')
            fail_c = get_credit_input('Please enter your credits at fail\t: ')

        total = pass_c + defer_c + fail_c
        # check count
        if total != 120:
            print('Total incorrect')
            continue

        else:

            if pass_c == 120 and defer_c == 0 and fail_c == 0:
                pro = '\nProgress'
                print(pro, end='')
                progress_count += 1
                break


            elif pass_c == 100 and (defer_c == 20 or defer_c == 0):
                p_m = '\nProgress (module trailer)'
                print(p_m, end='')
                trailer_count += 1
                break

            elif (pass_c == 40 and defer_c == 0) and (pass_c == 20 and defer_c == 0) and (
                    pass_c == 20 and defer_c == 0) and (
                    pass_c == 0 and (defer_c == 40 or defer_c == 20 or defer_c == 0)):
                exclu = '\nExclude'
                print(exclu, end='')
                exclude_count += 1
                break

            else:
                d_p = '\nDo not Progress – module retriever'
                print(d_p, end='')
                retriever_count += 1
                break

    if flag:
        print()
        progress_data += [[pass_c, defer_c, fail_c]]


call(True)

while True:
    print("\nWould you like to enter another set of data?\n")
    re_enter = str(input("Enter 'y' for yes or 'q' to quit and view results\t: "))

    if re_enter == 'y':
        call(True)
    elif re_enter == 'q':
        print('\nHistrogram\n')

        categories = {
            'Progress': progress_count,
            'Trailer': trailer_count,
            'Retriever': retriever_count,
            'Exclude': exclude_count
        }

        for category, count in categories.items():
            print(f"{category}: {'*' * count}")
        total = sum(categories.values())
        print(f"\noutcomes in total.  {total}\n")

        break
    else:
        continue

print("..................................................")

print('\nPart 2\n')

for progress in progress_data:
    pass_c = progress[0]
    defer_c = progress[1]
    fail_c = progress[2]
    call(False)
    print(" -", progress[0], ",", progress[1], ",", progress[2])

# Print the category names and counts
print('...................................................')

print('\nPart 3\n')

with open('progress.txt', 'w') as file:
    for result in progress_data:
        line = str(result[0]) + " , " + str(result[1]) + " , " + str(result[2])
        file.write(line)
        file.write('\n')

with open('progress.txt', 'r') as file:
    for line in file:
        line = line.strip()
        result = eval(line)
        pass_c, defer_c, fail_c = result
        call(False)
        print(" -", pass_c, ",", defer_c, ",", fail_c)

