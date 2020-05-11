class Node:
    def __init__(self,data = None): # Будем хранить данные предыдущего угла и указатель слудующего
        self.data = data # Не имеет никакого значения до назначения
        self.next = None # Не имеет никакого значения до момента пока у узла появится дочерний узел

class Linked_list:
    def __init__(self):
        self.head = Node() # Головной узел не будет содержать никаких данных, но будет указывать на первый элемент в списке

    def append(self,data): # Метод добавления узлов
        new_node = Node(data) # Создаем новый узел
        cur = self.head # Текущим элементом будет самый первый т. е. головной
        while cur.next != None: # Пока следующий узел не равно None
            cur = cur.next # Текущее меняется на следующее
        cur.next = new_node # Следующий элемент текущего узла новый узел


    def length(self): # Метод который возвращает длину списка
        cur = self.head # Текущий элемент
        len_my_list = 0 # Начальная длина списка
        while cur.next != None: # Пока следующий узел не равно None
            len_my_list += 1 # Длина списка будет увеличиваться
            cur = cur.next # Следующий узел становится текущим
        return len_my_list

    def display(self): # Метод для отображения списка
        elems = [] # Создаем список
        cur_node = self.head  # Текущим узлом будет головной
        while cur_node.next != None: # Цикл будет выполняться до тех пор пока следующий узел текущего не будет равно None
            cur_node = cur_node.next # Текущим узлом назначается следующий узел текущего
            elems.append(cur_node.data) # Добавляем данные в список
        print(elems) #

    def check(self, data): # Проверка ,сущетсвует ли элемент в списке
        cur_node = self.head # Текущий узел стал головным
        while (cur_node):
            if data == cur_node.data: # Если элемент существует в цикле то вернуть true
                return True
            else:
                cur_node = cur_node.next # Иначе начальным узлом станет следующий

my_list = Linked_list()
my_list.append(1)
my_list.append(5)
my_list.display()
my_list_len = my_list.length()
print(my_list_len)
print(my_list.check(5))
