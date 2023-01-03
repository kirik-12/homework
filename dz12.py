
#task1
"""
'''Реализация класса "Карточная игра", который будет 
содержать методы для создания колоды карт, раздачи
 карт игрокам, сравнения карт и т.д'''

class card_game:
    def __init__(self, amount  = 54 , kind_of_game = 'poker') -> None:
        self.amount = amount
        self.kind_of_game = kind_of_game
    

    def set_card_deck(self, **cards_and_players):
        # self.amount = len(cards)
        self.cards_and_players = cards_and_players
        # self.game = players


    def info_about_player_and_cards(self):
        return f'This game have: {self.cards_and_players}'


    def start_game(self, other):
        if other.kind_of_game == self.kind_of_game:
            return f'Let`s play in {self.kind_of_game}'
        return f'You don`t wanna play this game: {self.kind_of_game}'
    
a = card_game()
a.set_card_deck(player1 = [1,2,3,4] , player2 = [2,3,6,8])

# print(a.info_about_player_and_cards())
"""

#task2
"""
'''
Реализация класса "Магазин", который будет содержать информацию 
о товарах, их ценах, количестве на складе и т.д. и методы для работы 
с этой информацией, такие как добавление/удаление товаров, проведение 
продаж, поиск товаров по цене и т.д.
'''

class shop():
    def __init__(self, *products_list):
        self.products_list = products_list


    def set_amount_of_product_func(self,**price_and_products_dict):
        self.amount_of_products_dict = price_and_products_dict


    def set_price_of_products_func(self, **price_of_products_dict):
        self.price_of_products_dict = price_of_products_dict 


    # тут мы добавляем и убавляем количество продуктов
    def app_and_dim_product(self, product, amount=1):
        amount_dict = dict(self.amount_of_products_dict)
        if product in amount_dict:
            amount_dict[product] += amount
        else:
            amount_dict[product] = 0
            amount_dict[product] += amount

        if amount_dict[product] < 0: amount_dict[product] = 0

        self.amount_of_products_dict = amount_dict
    
    # изменяем цену товара
    def change_price_product(self, product, new_price):
        price_dict = dict(self.price_of_products_dict)
        if new_price < 0: new_price = 0
        if product in price_dict:
            price_dict[product] = new_price
        else:
            return f'This product:{product} is not found in database'

        self.price_of_products_dict = price_dict
        

    # выводим всю информацию о продуктах
    def info_about_products(self):
        products = self.products_list
        price = self.price_of_products_dict
        amount = self.amount_of_products_dict
        
        price_key = [ str(i[0]).upper() for i in sorted(price.items)]
        price_values = [ str(i[1]).upper() for i in sorted(price.items)]

        amount_key = [ str(i[0]).upper() for i in sorted(amount.items)]
        amount_values = [ str(i[1]).upper() for i in sorted(amount.items)]

        products_key = [str(i).upper() for i in products]

        c = set(price_key, amount_key, products_key)

        print('all products: ', c)
        print('price products: ', price_key, price_values)
        print('amount products: ', amount_key, amount_values)


    def find_info_product(self, product):
        price = self.price_of_products_dict
        amount = self.amount_of_products_dict
        if product in self.products_list:
            print(product, price[product], amount[product])
        else:
            print('Product not found')


    #удаляем продукт из базы данных
    def del_product(self, product):
        self.products_list = list(self.products_list).remove(product) 
        self.amount_of_products_dict = (self.amount_of_products_dict).pop(product, None)
        self.price_of_products_dict = (self.price_of_products_dict).pop(product, None) 
"""

#task3
"""
'''Реализовать алгоритм Дейкстры для нахождения кратчайшего пути в графе'''

def main():
    G = read_graph()
    start, finish = input('Enter start and finish: ').split()
    shortest_distances = dijkstra(G, start)
    shortest_path = get_path(G, shortest_distances, finish)
    print(f'Shortest path: ', *shortest_path)


def get_path(G, shortest_distances, finish):
    path = [finish]
    distance = shortest_distances[finish]
    while distance != 0:
        for neigh, weight in G[finish].items():
            if distance == shortest_distances[neigh] + int(weight):
                path.append(neigh)
                distance = shortest_distances[neigh]
                finish = neigh
    return path[::-1]


def dijkstra(G, start):
    from collections import deque
    deque = deque()
    short_dist = {start: 0}
    deque.append(start)
    while deque:
        curr = deque.popleft()
        for neigh in G[curr]:
            if neigh not in short_dist or short_dist[curr] + int(G[curr][neigh]) < short_dist[neigh]:
                short_dist[neigh] = short_dist[curr] + int(G[curr][neigh])
                deque.append(neigh)
    return short_dist


def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight


def read_graph():
    G = {}
    with open('graph_1.txt', 'r') as txt:
        for lineString in txt:
            a, b, weight = lineString.split()
            add_edge(G, a, b, weight)
            add_edge(G, b, a, weight)
    return G


if __name__ == '__main__':
    main()
"""
