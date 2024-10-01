import re
steps = input('input steps number:')
steps = int(steps)+1
a = input('input original(oofem.out.m_.gp) middle number:')
b = input('input exported(oofem.out.m_.gp) middle number:')
def match(row):
    row = row.strip().split()
    numbers = [i for i in row]
    last_two_numbers = numbers[-2:]
    return last_two_numbers

def extract_data(row):
    row = row.strip().split()
    numbers = [i for i in row]
    element_number = numbers[0]
    zcoord = numbers[8]
    stress = numbers[10]
    strain = numbers[17]
    material = numbers[-1]


    en = str(element_number)
    z = str(zcoord)
    st = str(stress)
    stra = str(strain)
    mat = str(material)
    row0 = en + ' ' + z + ' ' + st + ' ' + stra + ' ' + mat
    return row0

for i in range(1,steps,1):
    contour = str(i)
    filename0= 'oofem.out.m' + a + '.' + contour + '.gp'
    filename1 = 'oofem.out.m' + b + '.' + contour + '.gp'
    filename2 = 'output' + contour + '.dat'
    with open(filename0,'r') as f:
        data = [line for line in f]

        data2 = []
        with open(filename1,'w') as w:

            for row in data:

                last_two_numbers = match(row)

                if last_two_numbers == ['1', '1.000000e+00']:
                    break
                else:
                    w.write(row)

                if last_two_numbers == ['1', '2.000000e+00']:
                    row8 = extract_data(row)+'\n'
                    data2.append(row8)
        with open(filename2,'w') as w2:
            w2.write('#element_number #zCoord #stress #strain #material number\n')
            for i in data2:
                w2.write(i)








