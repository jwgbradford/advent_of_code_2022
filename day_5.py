def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    boxes, orders = file_data.split("\n\n")
    boxes_list = [data for data in boxes.split("\n")]
    orders_list = [data for data in orders.split("\n")]
    return boxes_list, orders_list

def list_to_matrix(data_list):
    columns = data_list[-1].split(" ")
    column_count = 0
    for entry in columns:
        if entry:
            column_count += 1
    box_stack = [[]for _ in range(column_count)]
    for boxes in data_list:
        for column, box in enumerate(boxes):
            if box and (column - 1)%4 == 0:
                box_stack[(column - 1) // 4].append(box)
    # get rid of empty entries
    empties = []
    for i, column in enumerate(box_stack):
        for item in column:
            if item == ' ':
                empties.append(i)
    for empty in empties:
        box_stack[empty].pop(0)
    return box_stack

def shuffle_boxes(stack, orders):
    # redo to maintain order
    for order in orders:
        order_elements = order.split(" ")
        '''
        item = stack[int(order_elements[3]) - 1][:int(order_elements[1])]
        item.reverse()
        for box in item:
            stack[int(order_elements[3]) - 1].pop(0)
            stack[int(order_elements[5]) - 1].insert(0, box)
        '''
        for _ in range(int(order_elements[1])):
            for item in stack[int(order_elements[3]) - 1]:
                if item:
                    stack[int(order_elements[3]) - 1].pop(0)
                    stack[int(order_elements[5]) - 1].insert(0, item)
                    break
    return stack

def top_boxes(stack):
    top_list = ''
    for column in stack:
        top_list = top_list + column[0]
    print(top_list)

boxes_list, orders_list = get_data('day_5.txt')
box_stack = list_to_matrix(boxes_list)
shuffled_stack = shuffle_boxes(box_stack, orders_list)
top_boxes(shuffled_stack)