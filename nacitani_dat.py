import json

with open('test_path.json') as i :
    test_path_parsed = json.load(i)

with open('map_data_0.json') as j:
    map_data_O_parsed = json.load(j)


def x_coordinates():
    """
         sort x coordinates of obstacle
    """
    coordinates_unselected_0 = map_data_O_parsed["object"]
    x_coordinates_selected = []
    for i in range(len(coordinates_unselected_0)):
        for objects_0 in coordinates_unselected_0:
            coordinates_selected_0 = objects_0["coordinates"]
            x_coordinate_0 = []
            for x_numbers_0 in coordinates_selected_0:
                x_coordinate = x_numbers_0[0]
                x_coordinate_0.append(x_coordinate)
        x_coordinates_selected.append(x_coordinate_0)
    return(x_coordinates_selected)
print(x_coordinates())


def y_coordinates():
    """
    sort y coordinates of obstacle
    """
    coordinates_unselected_00 = map_data_O_parsed["object"]
    y_coordinates_selected = []
    for j in range(len(coordinates_unselected_00)):
        for objects_00 in coordinates_unselected_00:
            coordinates_selected_00 = objects_00["coordinates"]
            y_coordinate_00 = []
            for y_numbers_0 in coordinates_selected_00:
                y_coordinate = y_numbers_0[-1]
                y_coordinate_00.append(y_coordinate)
        y_coordinates_selected.append(y_coordinate_00)
    return (y_coordinates_selected)
print(y_coordinates())


def start():
    """
     sort start coordinates
    """
    start_paths_unsorted = test_path_parsed["path"]
    start_coordinates = []
    for starts in start_paths_unsorted:
        start_path = starts["start"]
        start_coordinates.append(start_path)
    return(start_coordinates)
print(start())


def end():
    """
    sort end coordinates
    """
    end_paths_unsorted = test_path_parsed["path"]
    end_coordinates = []
    for ends in end_paths_unsorted:
        end_path = ends["end"]
        end_coordinates.append(end_path)
    return (end_coordinates)
print(end())


