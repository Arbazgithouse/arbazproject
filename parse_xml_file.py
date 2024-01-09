import os
import xml.etree.ElementTree as ET

class XMlParser:

    # This method parse xml files from specified folder
    # returns dictionary of classname as key and time as value
    @staticmethod
    def parse_xml_file(folder_path):
        class_time_dict = {}
        # Iterate through XML files in the specified folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.xml'):
                tree = ET.parse(os.path.join(folder_path, filename))
                root = tree.getroot()
                for attr in root:
                    classname = attr.get('classname')
                    time = float(attr.get('time'))
                    if classname not in class_time_dict:
                        class_time_dict[classname] = time
                    else:
                        class_time_dict[classname] += time

        return class_time_dict
    # ------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def dump_csv(group_list, csv_file_name):
        headers = "ClassName,Time,GroupNo\n"
        group_no = 1
        with open(csv_file_name, "w") as csv_file:
            csv_file.write(headers)
            for group in group_list:
                for class_name, time in group:
                    csv_file.write(class_name + "," + str(time) + "," + str(group_no) + "\n")

                group_no += 1
        return

    # ------------------------------------------------------------------------------------------------------------------

    # distributes classes in 5 groups with respect to times
    @staticmethod
    def distribute_classnames(class_time_dict):
        sorted_classes = sorted(class_time_dict.items(), key=lambda x: x[1], reverse=True)
        groups = [[] for _ in range(5)]
        group_times = [0] * 5

        for class_name, time in sorted_classes:
            min_group_index = group_times.index(min(group_times))
            groups[min_group_index].append((class_name, time))
            group_times[min_group_index] += time

        return groups

# ======================================================================================================================


if __name__ == '__main__':
    dir_path = "./data"
    class_time_dict = XMlParser.parse_xml_file(dir_path)

    group_list = XMlParser.distribute_classnames(class_time_dict)

    csv_file_path = r"./class_time_csv.csv"
    XMlParser.dump_csv(group_list, csv_file_path)
    