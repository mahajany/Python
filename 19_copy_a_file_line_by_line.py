#!/usr/bin/python3
try:
    f_in=open("data_file_list.txt", "r")
    f_out=open("data_file_list_out.txt", "w")

    while True:
        line=f_in.readline()
        if not line:
            break
        if not line.strip():
            continue
        yr,character,creator=line.split(',')
        yr=int(yr)+100000000
        f_out.write(str(yr)+"-->"+character+"\n" )

except Exception as err:
    print("Error Occurred!")
    print(err)
finally :
    f_in.close()
    f_out.close()
