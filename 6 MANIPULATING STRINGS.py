def printTable(table):

    colWidths = []
    for line in table:
        longest = 0
        for word in line:
            if len(word) > longest:
                longest = len(word)
        colWidths.append(longest)

    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].ljust(colWidths[y]),end=" ")
        print()




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)