import sys


###############
# author: Frankie Girling
#
# project #1
#
# description: Count inversions in an ascending and descending array and confirm whether ascending or descending sort
# gives the least amount of inversions
###############


def ChooseOrdering(ascending, descending, fp_out=sys.stdout):
    '''
    @pre: non empty array of integers that holds the countsof inversions for ascending each array 
          non empty array of the same length that holds the count of inversions for descending each array
          file object to write to

    @post:  returns nothing, writes the output to a file.

    function decides which sorting arrangement would be more efficient and prints the output to file
    '''
    # DO NOT MODIFY - WILL DEDUCT POINTS
    if abs(sum(ascending) - sum(descending)) < 0.00001:
        outcome = "TIE"
    else:
        outcome = "ASCENDING" if sum(ascending) < sum(descending) else "DESCENDING"

    # directing output to file  
    print("Total Number of portfolio's assessed: ", len(ascending), file=fp_out)
    print(" " * 12, "{:^12s}  vs {:^12s}".format("Ascending", "Descending"), file=fp_out)
    for pairs in range(len(ascending)):
        print("Portfolio #{:02d} {:^12d} vs {:^12d}" \
              .format(pairs + 1, ascending[pairs], descending[pairs]), file=fp_out)
    print("\n\nTotal Inversion Count", file=fp_out)
    print("Ascending: ", sum(ascending), " vs. Descending: ", sum(descending), file=fp_out)

    print("\n\nBest Form of Ordering: ", outcome, file=fp_out)


def OrderCurriences(fp, fp_out=sys.stdout):
    '''
    @pre: set of arrays with sorted or unsorted integers
          file object to write to

    @post: returns nothing, calls ChooseOrdering function

    This function converts the input string into a list of integers to properly sort in ascending and descending order
    '''

    acc_list = []
    dec_list = []

    for item in fp:

        item = item.replace('\n', '')
        lst = item.split(",")
        lst2 = []

        for str1 in lst:

            str2 = int(str1)
            lst2.append(str2)

        acc_list.append(merge_count_inversion(lst2)[1])
        dec_list.append(merge_count_inversion_dec(lst2)[1])

    ChooseOrdering(acc_list, dec_list, fp_out)


def merge_count_inversion(lst):
    """
    @pre: a list of integers

    @post: a list sorted in ascending order, and the number of inversions in the list

    This function sorts a list of integers in ascending order using merge sort, and counts the number of inversions
    """

    if len(lst) <= 1:

        return lst, 0

    middle = int(len(lst) / 2)

    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)

    return result, (a + b + c)


def merge_count_split_inversion(left, right):
    """
    @pre: two lists of numbers

    @post: a single list sorted in ascending order containing both original lists of numbers

    This function sorts two lists of numbers into one, and counts the number of inversions
    """

    result = []
    count = 0
    i = 0
    j = 0

    left_len = len(left)

    while i < left_len and j < len(right):

        if left[i] <= right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            count += left_len - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, count


def merge_count_inversion_dec(lst):
    """
    @pre: a list of integers

    @post: a list sorted in descending order, and the number of inversions in the list

    This function sorts a list of integers in descending order using merge sort, and counts the number of inversions
    """

    if len(lst) <= 1:

        return lst, 0

    middle = int(len(lst) / 2)

    left, a = merge_count_inversion_dec(lst[:middle])
    right, b = merge_count_inversion_dec(lst[middle:])
    result, c = merge_count_split_inversion_dec(left, right)

    return result, (a + b + c)


def merge_count_split_inversion_dec(left, right):
    """
    @pre: two lists of numbers

    @post: a single list sorted in descending order containing both original lists of numbers

    This function sorts two lists of numbers into one, and counts the number of inversions
    """

    result = []
    count = 0
    i = 0
    j = 0

    left_len = len(left)

    while i < left_len and j < len(right):

        if left[i] >= right[j]:

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            count += left_len - i
            j += 1

    result += left[i:]
    result += right[j:]

    return result, count


def main():
    fp = open(input("Insert Filename (with extension) for input: ").strip())

    fp_out = open(input("Insert Filename (with extension) for output: ").strip(), 'w')

    OrderCurriences(fp, fp_out)
    fp_out.close()
    fp.close()


main()
