import csv
import math

c = 0.00002
epsilon = 0.1*math.e

def hub(file):
    node_list = []
    mass_centre_x_0 = 0
    mass_centre_y_0 = 0
    f_iterazione = []
    d = []
    d_sum = 0
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')                            

        #READING ALL DATA FROM CSV FILE
        for row in csv_reader:
            node = [row[0], float(row[1]), float(row[2]), int(row[3])] #[water well, abscissa, ordinate, flow rate] 
            d.append(int(row[3]))
            node_list.append(node)

    #calculate the center of mass(x0,y0)
    for node in node_list:
        d_sum += node[3]
        mass_centre_x_0 += node[1]*node[3]
        mass_centre_y_0 += node[2]*node[3]
    
    mass_centre_x_0 = mass_centre_x_0/d_sum
    mass_centre_y_0 = mass_centre_y_0/d_sum

    #Weiszfeld heuristic at #0 iteration
    f_iterazione.append(f(mass_centre_x_0, mass_centre_y_0, node_list))
    
    print("Iterazione 0")
    print("x_0="+str(mass_centre_x_0)+", y_0="+str(mass_centre_y_0))
    print("z_0="+str(f_iterazione[0]))

    mass_centre_x = new_x(mass_centre_x_0, mass_centre_y_0, node_list)
    mass_centre_y = new_y(mass_centre_x_0, mass_centre_y_0, node_list)

    #Weiszfeld heuristic at #1 iteration
    f_iterazione.append(f(mass_centre_x, mass_centre_y, node_list))

    print("Iterazione 1")
    print("x_1="+str(mass_centre_x)+", y_1="+str(mass_centre_y))
    print("z_1="+str(f_iterazione[1]))

    h=1
    
    #We finally check if the cost reduction is less than the threshold
    while (f_iterazione[h-1] - f_iterazione[h] > epsilon):
        h += 1
        x = mass_centre_x
        y = mass_centre_y
        mass_centre_x = new_x(x, y, node_list)
        mass_centre_y = new_y(x, y, node_list)
        f_iterazione.append(f(mass_centre_x, mass_centre_y, node_list))
        print("Iterazione "+str(h))
        print("x_"+str(h)+"="+str(mass_centre_x)+", y_"+str(h)+"="+str(mass_centre_y))
        print("z_"+str(h)+"="+str(f_iterazione[h]))
        

    print("L'hub si posiziona in x="+ str(mass_centre_x)+", y="+str(mass_centre_y)+" con z="+str(f_iterazione[h]))

#this defines the weiszfeld heuristic
def f(x, y, node_list):
    f=0
    for node in node_list:
        f += c*node[3]*(math.sqrt(pow((node[1]-x), 2) + pow((node[2]-y), 2)))

    return f

#this calculate the new x that will be used in the next iterations 
def new_x(x, y, node_list):
    num_x = 0
    den = 0
    for node in node_list:
        num_x += (node[3]*node[1]/(math.sqrt(pow((node[1]-x), 2) + pow((node[2]-y), 2))))
        den += (node[3]/(math.sqrt(pow((node[1]-x), 2) + pow((node[2]-y), 2))))

    return num_x/den

#this calculate the new x that will be used in the next iterations
def new_y(x, y, node_list):
    num_y = 0
    den = 0
    for node in node_list:
        num_y += (node[3]*node[2]/(math.sqrt(pow((node[1]-x), 2) + pow((node[2]-y), 2))))
        den += (node[3]/(math.sqrt(pow((node[1]-x), 2) + pow((node[2]-y), 2))))

    return num_y/den

    
    
