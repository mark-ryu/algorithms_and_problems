
def main():
    '''gets the fibonacci sequence whose values do not exceed four million, find 
    the sum of the even-valued terms.'''
    m = 0
    n = 1
    even_list = list()
    while n < 4000000:
        z = m + n
        m = n
        n = z
        if n % 2 == 0:
            even_list.append(n)
    print (sum(even_list))
    return sum(even_list)
        

if __name__ == '__main__':
    main()
