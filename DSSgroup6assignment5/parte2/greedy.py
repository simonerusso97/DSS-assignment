import math
import csv

def greedy(file):
    customer_list = []
    succ = {}
    min_dist_dict = {}
    min_dist_list = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        

        #READING ALL DATA FROM CSV FILE
        for row in csv_reader:
            if(line_counter==0):
                line_counter += 1
                customers_number=int(row[0])

            elif(line_counter==1):
                line_counter +=1
                capacity=int(row[0])

            elif (line_counter==2):
                line_counter +=1
                
            elif (line_counter < customers_number+3):
                line_counter +=1
                customer = [int (row[0]), float (row[1]), float (row[2]), int (row[3]) ]
                customer_list.append(customer)

    
    c_matrix = [[0 for x in range(customers_number)] for y in range(customers_number)]

    i = 0
    print("MATRICE DELLE DISTANZE")
    for i in range(customers_number):
        for j in range(customers_number):
                
            c1x = customer_list[i][1]
            c1y = customer_list[i][2]

            c2x = customer_list[j][1]
            c2y = customer_list[j][2]
                
            dist = math.sqrt(pow((c1x - c2x),2) + pow(c1y - c2y, 2))

            c_matrix[i][j] = dist
    
        print(c_matrix[i])
    print("------------------------")
        

    
    last_customer = customer_list[0]
    temp = customer_list.copy()
    capacity_left = capacity
    succ_list = []
    while len(temp) > 1 :
        check = True
        min_dist_dict.clear()
        print ("INIZIO ITERAZIONE")
        print()
        print("TEMP LIST")
        print(temp)
        print()

        temp.remove(last_customer)

        print("TEMP LIST DOPO REMOVE")
        print(temp)
        print()
        
        for current in temp:

            print("CURRENT NEL FOR")
            print(current)

            min_dist_dict[current[0]] = c_matrix[last_customer[0]][current[0]]

        min_dist_list = sorted(min_dist_dict.items(), key=lambda x: x[1])

        print("MIN DIST")
        print(min_dist_list)
        print()

        for i in min_dist_list:
            c = customer_list[i[0]]
            print("CUSTOMER MIN DIST")
            print(c)
            print()

            if(capacity_left >= c[3]):
                capacity_left = capacity_left - c[3]
                succ[last_customer[0]] = c[0]
                last_customer= customer_list[succ[last_customer[0]]]
                print("CAPACITA RESIDUA")
                print(capacity_left)
                print()
                print("SUCC IN IF CAPACITA")
                print(succ)
                print()
                print("LAST_CUST IN IF CAPACITA")
                print(last_customer)
                print()
                check = False
                break
            

        if check:
            #CHIUDO IL CICLO
            succ[last_customer[0]]=customer_list[0][0]
            last_customer = customer_list[0]
            temp.append(last_customer)
            succ_list.append(succ.copy())
            print("SUCC LIST")
            print(succ_list)
            capacity_left = capacity
            succ.clear()
            
        
             
        print("---------------------------------")

    succ[last_customer[0]]=customer_list[0][0]
    succ_list.append(succ.copy())
    print("SUCC FINALE")
    print(succ)
    print("SUCC LIST FINALE")
    print(succ_list)
