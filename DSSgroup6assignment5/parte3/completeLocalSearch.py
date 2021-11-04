import math
import csv

def completeLocalSearch(file):


    customer_list = []
    min_dist_dict = {}
    min_dist_list = []
    tour_list = []
    t = []
    tt1 = []
    tt2 = []

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0

        # READING ALL DATA FROM CSV FILE
        for row in csv_reader:
            if (line_counter == 0):
                line_counter += 1
                customers_number = int(row[0])

            elif (line_counter == 1):
                line_counter += 1
                capacity = int(row[0])

            elif (line_counter == 2):
                line_counter += 1

            elif (line_counter < customers_number + 3):
                line_counter += 1
                customer = [int(row[0]), float(row[1]), float(row[2]), int(row[3])]
                customer_list.append(customer)
            elif (line_counter == customers_number + 3):
                line_counter += 1
                z_value = float(row[0])
            else:
                line_counter += 1
                t.clear()
                for i in range(0, len(row)):
                    t.append(int(row[i]))
                tour_list.append(t.copy())

    c_matrix = [[0 for x in range(customers_number)] for y in range(customers_number)]

    print("MATRICE DELLE DISTANZE")
    for i in range(customers_number):
        for j in range(customers_number):
            c1x = customer_list[i][1]
            c1y = customer_list[i][2]

            c2x = customer_list[j][1]
            c2y = customer_list[j][2]

            dist = math.sqrt(pow((c1x - c2x), 2) + pow(c1y - c2y, 2))

            c_matrix[i][j] = dist

        print(c_matrix[i])
    print("------------------------")

    z_best = z_value
    while True:
        z_value = z_best
        for tour in tour_list:
            capacita_residua = capacity
            for node in customer_list:
                if ((node[0] in tour) and (node[0] != 0)):
                    capacita_residua -= node[3]

            for current_node in tour:
                tt1.clear()
                tt2.clear()
                delta_z1 = 0
                delta_z2 = 0

                if current_node != 0:
                    index = tour.index(current_node)
                    min_dist_dict.clear()
                    min_dist_list.clear()
                    # CERCHIAMO IL PIU' VICINO NON NEL TOUR DI PARTENZA
                    for node in customer_list:
                        if (not (node[0] in tour)):
                            min_dist_dict[node[0]] = c_matrix[int(current_node)][node[0]]
                    min_dist_list = sorted(min_dist_dict.items(), key=lambda x: x[1])
                    stop = False
                    stopNode = False
                    neighbor = 0
                    for i in range(0, len(min_dist_list)):

                        for node in customer_list:
                            if (node[0] == min_dist_list[i][0]):
                                stopNode = True
                                if (node[3] < capacita_residua):
                                    neighbor = min_dist_list[i][0]
                                    stop = True
                            if (stopNode):
                                break
                        if (stop):
                            break

                    # VICINO PRIMA DEL NODO[0,*,1,2,0]
                    if (neighbor != 0):
                        for cont in range(0, len(tour)):
                            if (cont == index):
                                tt1.append(neighbor)
                                tt1.append(tour[cont])
                            else:
                                tt1.append(tour[cont])
                        prev = tour[index - 1]
                        delta_z1 = delta_z1 + c_matrix[prev][neighbor] + c_matrix[current_node][neighbor] - \
                                   c_matrix[current_node][
                                       prev]
                        for check in tour_list:
                            if (neighbor in check):
                                i = check.index(neighbor)
                                prev = check[i - 1]
                                succ = check[i + 1]
                                delta_z1 = delta_z1 + c_matrix[prev][succ] - c_matrix[prev][neighbor] - c_matrix[succ][
                                    neighbor]

                        # VICINO DOPO IL NODO[0,1,*,2,0]
                        for cont in range(0, len(tour)):
                            if (cont == index):
                                tt2.append(tour[cont])
                                tt2.append(neighbor)
                            else:
                                tt2.append(tour[cont])
                        succ = tour[index + 1]
                        delta_z2 = delta_z2 + c_matrix[current_node][neighbor] + c_matrix[succ][neighbor] - \
                                   c_matrix[current_node][
                                       succ]
                        for check in tour_list:
                            if (neighbor in check):
                                i = check.index(neighbor)
                                prev = check[i - 1]
                                succ = check[i + 1]
                                delta_z2 = delta_z2 + c_matrix[prev][succ] - c_matrix[prev][neighbor] - c_matrix[succ][
                                    neighbor]

                        if (delta_z1 < delta_z2):
                            delta_z = delta_z1
                            tt = tt1
                        else:
                            delta_z = delta_z2
                            tt = tt2

                        if (z_value + delta_z < z_best):
                            x_best = tt.copy()
                            index_tour_da_modificare = tour_list.index(tour)
                            neighbor_da_spostare = neighbor
                            z_best = z_value + delta_z
                        print("")

        if (z_best == z_value):
            break
        else:
            for tour in tour_list:
                if (neighbor_da_spostare in tour):
                    tour.pop(tour.index(neighbor_da_spostare))
                    if (len(tour) == 2):
                        tour_list.pop(tour_list.index(tour))

            tour_list[index_tour_da_modificare] = x_best
    print(z_best)
    print(tour_list)

