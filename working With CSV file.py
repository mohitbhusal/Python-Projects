#CSV stands for comma seperated value
import csv
with open('Csv making.csv','rt') as file: #here with command better because using
                                          # it doesnt require to close the opened file we can
                                          # just indent the output inside the with and it works well
    csv_rows = csv.reader(file)
    a=" "
    for rows in csv_rows:
        m=len(rows)
        if rows[m-m]=="":
            print(*rows[m-2],sep="")

        else:
            print(a*4,*rows,sep='   ')






