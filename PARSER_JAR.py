#definisi CFG
print('Input format   : if <var> <op> <var> { <var> = <angka> }else{ <var> = <angka> }')
print('<var>          := a, b')
print('<op>           := ==, >=, <=, >, <')
print('<angka>        := 1, 2\n')

#menambahkan EOS di kalimat terakhir
print('Masukkan kalimat Anda:')
sentence = input()
print('\n')

tokens =[]
tokens = sentence.split()
tokens.append('EOS')

#definisi simbol
non_terminals = ['S', 'kondisi', 'aksi', 'var', 'op', 'n']
terminals = ['if', '{', '}else{', '}', 'a', 'b', '==', '>=', '<=', '<', '>', '1', '2', '=']

#definisi parse table
parse_table = {}

parse_table[('S', 'if')] = ['if', 'kondisi', '{', 'aksi', '}else{', 'aksi', '}']
parse_table[('S', '{')] = ['ERROR']
parse_table[('S', '}else{')] = ['ERROR']
parse_table[('S', '}')] = ['ERROR']
parse_table[('S', '=')] = ['ERROR']
parse_table[('S', 'a')] = ['ERROR']
parse_table[('S', 'b')] = ['ERROR']
parse_table[('S', '==')] = ['ERROR']
parse_table[('S', '>=')] = ['ERROR']
parse_table[('S', '<=')] = ['ERROR']
parse_table[('S', '<')] = ['ERROR']
parse_table[('S', '>')] = ['ERROR']
parse_table[('S', '1')] = ['ERROR']
parse_table[('S', '2')] = ['ERROR']


parse_table[('kondisi', 'if')] = ['ERROR']
parse_table[('kondisi', '{')] = ['ERROR']
parse_table[('kondisi', '}else{')] = ['ERROR']
parse_table[('kondisi', '}')] = ['ERROR']
parse_table[('kondisi', '=')] = ['ERROR']
parse_table[('kondisi', 'a')] = ['var','op','var']
parse_table[('kondisi', 'b')] = ['var','op','var']
parse_table[('kondisi', '==')] = ['ERROR']
parse_table[('kondisi', '>=')] = ['ERROR']
parse_table[('kondisi', '<=')] = ['ERROR']
parse_table[('kondisi', '<')] = ['ERROR']
parse_table[('kondisi', '>')] = ['ERROR']
parse_table[('kondisi', '1')] = ['ERROR']
parse_table[('kondisi', '2')] = ['ERROR']


parse_table[('aksi', 'if')] = ['ERROR']
parse_table[('aksi', '{')] = ['ERROR']
parse_table[('aksi', '}else{')] = ['ERROR']
parse_table[('aksi', '}')] = ['ERROR']
parse_table[('aksi', '=')] = ['ERROR']
parse_table[('aksi', 'a')] = ['var','=','n']
parse_table[('aksi', 'b')] = ['var','=','n']
parse_table[('aksi', '==')] = ['ERROR']
parse_table[('aksi', '>=')] = ['ERROR']
parse_table[('aksi', '<=')] = ['ERROR']
parse_table[('aksi', '<')] = ['ERROR']
parse_table[('aksi', '>')] = ['ERROR']
parse_table[('aksi', '1')] = ['ERROR']
parse_table[('aksi', '2')] = ['ERROR']

parse_table[('var', 'if')] = ['ERROR']
parse_table[('var', '{')] = ['ERROR']
parse_table[('var', '}else{')] = ['ERROR']
parse_table[('var', '}')] = ['ERROR']
parse_table[('var', '=')] = ['ERROR']
parse_table[('var', 'a')] = ['a']
parse_table[('var', 'b')] = ['b']
parse_table[('var', '==')] = ['ERROR']
parse_table[('var', '>=')] = ['ERROR']
parse_table[('var', '<=')] = ['ERROR']
parse_table[('var', '<')] = ['ERROR']
parse_table[('var', '>')] = ['ERROR']
parse_table[('var', '1')] = ['ERROR']
parse_table[('var', '2')] = ['ERROR']

parse_table[('op', 'if')] = ['ERROR']
parse_table[('op', '{')] = ['ERROR']
parse_table[('op', '}else{')] = ['ERROR']
parse_table[('op', '}')] = ['ERROR']
parse_table[('op', '=')] = ['ERROR']
parse_table[('op', 'a')] = ['ERROR']
parse_table[('op', 'b')] = ['ERROR']
parse_table[('op', '==')] = ['==']
parse_table[('op', '>=')] = ['>=']
parse_table[('op', '<=')] = ['<=']
parse_table[('op', '<')] = ['<']
parse_table[('op', '>')] = ['>']
parse_table[('op', '1')] = ['ERROR']
parse_table[('op', '2')] = ['ERROR']

parse_table[('n', 'if')] = ['ERROR']
parse_table[('n', '{')] = ['ERROR']
parse_table[('n', '}else{')] = ['ERROR']
parse_table[('n', '}')] = ['ERROR']
parse_table[('n', '=')] = ['ERROR']
parse_table[('n', 'a')] = ['ERROR']
parse_table[('n', 'b')] = ['ERROR']
parse_table[('n', '==')] = ['ERROR']
parse_table[('n', '>=')] = ['ERROR']
parse_table[('n', '<=')] = ['ERROR']
parse_table[('n', '<')] = ['ERROR']
parse_table[('n', '>')] = ['ERROR']
parse_table[('n', '1')] = ['1']
parse_table[('n', '2')] = ['2']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idxToken = 0
symbol = tokens[idxToken]

# parsing process
while (len(stack) > 0):
  top = stack[len(stack) - 1]
  # print('top =', top)
  # print('symbol =', symbol)
  if top in terminals:
    # print('top adalah symbol terminal')
    if top == symbol:
      stack.pop()
      idxToken += 1
      symbol = tokens[idxToken]
      if symbol == 'EOS':
        # print('isi stack:', stack)
        stack.pop()
    else:
      break
  elif top in non_terminals:
    # print('top adalah symbol non-terminal')
    if parse_table[(top, symbol)][0] != 'ERROR':
      stack.pop()
      symbolsToBePushed = parse_table[(top, symbol)]
      for i in range(len(symbolsToBePushed) - 1, -1, -1):
        stack.append(symbolsToBePushed[i])
    else:
      break
  else:
    break

# conclusion
if symbol == 'EOS' and len(stack) == 0 :
  list_output = sentence.split()
  for i in list_output:
    if i == "}else{":
        print("}")
        print("else")
        print("{")
        continue
    print(i)
    print("Syntax is Valid")
else:
  print(sentence, 'Invalid Syntax')
