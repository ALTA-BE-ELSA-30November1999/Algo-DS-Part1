def CekPrima(bilangan): 
    prima = True 
    if bilangan <= 1 :
        prima = False
    for i in range(2, bilangan): 
        if (bilangan % i == 0): 
            prima = False 
            break 
    return prima
max = 100
def get_prime(max) :
    List = []
    for i in range(max+1):
        if CekPrima(i):
            List.append(i)
    return List
# print("List prima = ", get_prime(max))

def generate_primes_grid(width, height, start):
    if start >5 :
        List_result = []
        for i in range (height) :
            for j in range (width) :
                start -= 1
                # temp_width =  (i * width)
                # idx_result =  (j * temp_width) + temp_width 
                num = start + i * width + j 
                num = start
                num -= 1
                bil_prima = get_prime(max)
                List_result.append(bil_prima[num])
            Urut = sorted(List_result)
        Hasil = ' '.join(map(str, Urut))
        return Hasil
    else :
        List_result = []
        for i in range (height) :
            for j in range (width) :
                start += 1
                # temp_width =  (i * width)
                # idx_result =  (j * temp_width) + temp_width 
                num = start + i * width + j 
                num = start
                num -= 1
                bil_prima = get_prime(max)
                List_result.append(bil_prima[num])
        Hasil = ' '.join(map(str, List_result))
        return Hasil

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """