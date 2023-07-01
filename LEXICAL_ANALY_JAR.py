#definisi CFG
print('Input format   : if <var> <op> <var> { <var> = <angka> }else{ <var> = <angka> }')
print('<var>          := a, b')
print('<op>           := ==, >=, <=, >, <')
print('<angka>        := 1, 2\n')

#jenis kata
#alphabet (variable)
var = ['a', 'b']
#bilangan bulat (angka)
n = ['1', '2']
#perbandingan (operator)
op = ['==', '>=', '<=', '>', '<']
#kata lainnya
statement = ['if', '{', '}else{', '}', '=']

def get_kata(teks, x):
    k = len(teks)
    kata = ""

    # abaikan spasi dan pindah baris
    while teks[x] == ' ' or teks[x] == '\r' or teks[x] == '\n':
        x += 1

    # ambil 1 kata
    while x < k and teks[x] != ' ' and teks[x] != '\r' and teks[x] != '\n':
        if teks[x] == '>':
            if kata != '':
                return kata
            else:
                x += 1
                if teks[x] == '=':
                    x += 1
                    return ">="
                else:
                    return ">"
        elif teks[x] == '<':
            if kata != '':
                return kata
            else:
                x += 1
                if teks[x] == '=':
                    x += 1
                    return "<="
                else:
                    return "<"
        elif teks[x] == '=':
            if kata != '':
                return kata
            else:
                x += 1
                return "="
        kata += teks[x]
        x += 1

    return kata

# count kata
def kata_kata(kalimat):
    i = 0
    chrlength = len(kalimat)
    hasil = ""

    while i < chrlength:
        kata = get_kata(kalimat, i)

        if kata not in var and kata not in n and kata not in op and kata not in statement:
            return "kata input invalid"

        i = i + len(kata)
        while i < chrlength and (kalimat[i] == ' ' or kalimat[i] == '\r' or kalimat[i] == '\n'):
            i = i + 1

    return kalimat

# input user
print('Masukkan kalimat : ')
kalimat = input()
loop = kata_kata(kalimat)
list_output = loop.split()
for i in list_output:
    if i == "}else{":
        print("}")
        print("else")
        print("{")
        continue
    print(i)

