num_file = 0
while True:
    file = open(str(num_file) + '.txt', 'w')
    for _control in range(1, 2**((4096*2)*1000000)):
        file.write('hdhushdhsuhshau')
    num_file += 1
    file.close()
