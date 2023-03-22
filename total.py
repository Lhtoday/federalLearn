import csv

class from_csv_to():

    #从指定的路径 读取 csv文件，如果有标签就返回 带标签的数据，并且提取出标签
    #没有标签 只返回数据
    def read_csv_from_path(self, csv_path, has_label):
        data = []
        label = []
        with open(csv_path) as read_csv:
            csv_reader = csv.reader(read_csv)  # 使用csv.reader读取csvfile中的文件
            # header = next(csv_reader)        # 读取第一行每一列的标题
            for row in csv_reader:  # 将csv 文件中的数据保存到data中
                l = len(row)
                data.append(row)
                if has_label:
                    label.append(row[l - 1])

            read_csv.close()

        if has_label:
            return data, label
        else:
            return data

    #给没有标签的数据加上标签
    def add_label_to_train_b(self, data, label):
        l = len(data)
        for i in range(l):
            data[i].append(label[i])

        return  data

    #把数据分成合法的
    def devide_to_legal_to_csv(self, path, data):
        with open(path, "w", newline='') as write_csv:
            csv_writer = csv.writer(write_csv)

            for row in data:
                l = len(row)
                if row[l - 1] == '0':
                    csv_writer.writerow(row)

            write_csv.close()

    #将数据分成非法的
    def devide_to_illegal_to_csv(self, path, data):
        with open(path, "w", newline='') as write_csv:
            csv_writer = csv.writer(write_csv)

            for row in data:
                l = len(row)
                if row[l - 1] == '1':
                    csv_writer.writerow(row)

            write_csv.close()

if __name__ == '__main__':
    oper = from_csv_to()

    origin_train_a_with_label, label = oper.read_csv_from_path("D:\\Federal-Learning\\dataset\\train_a_label.csv", True)
    oper.devide_to_legal_to_csv("D:\\Federal-Learning\\dataset\\deal\\train_a_legal.csv", origin_train_a_with_label)
    oper.devide_to_illegal_to_csv("D:\\Federal-Learning\\dataset\\deal\\train_a_illegal.csv", origin_train_a_with_label)

    origin_train_b_without_label = oper.read_csv_from_path("D:\\Federal-Learning\\dataset\\train_b.csv", False)
    origin_train_b_with_label = oper.add_label_to_train_b(origin_train_b_without_label, label)
    oper.devide_to_legal_to_csv("D:\\Federal-Learning\\dataset\\deal\\train_b_legal.csv", origin_train_b_with_label)
    oper.devide_to_illegal_to_csv("D:\\Federal-Learning\\dataset\\deal\\train_b_illegal.csv", origin_train_b_with_label)
