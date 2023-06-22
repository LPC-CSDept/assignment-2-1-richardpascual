def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_male = int(input('How many male students: '))
    num_female = int(input('How many female students: '))

    total = num_male + num_female
    m_perc = float((num_male / total)*100)
    f_perc = float((num_female / total)*100)

    print(f'The total number of students:\t\t{total:d}')
    print(f'The number of males and females:\t{num_male:d}\t{num_female:d}')
    print(f'The percentage of males and females:\t{m_perc:.2f}\t{f_perc:.2f}')   

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
