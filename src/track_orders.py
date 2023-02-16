from src.analyze_log import (
    get_item_most_ordered_by_client,
    get_unordered_items_by_client,
    get_days_that_client_never_camed
)

class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return get_item_most_ordered_by_client(customer, self.data)

    def get_never_ordered_per_customer(self, customer):
        return get_unordered_items_by_client(customer, self.data)

    def get_days_never_visited_per_customer(self, customer):
        return get_days_that_client_never_camed(customer, self.data)

    def get_busiest_day(self):
        list_days = [order[2] for order in self.data]
        return max(
            set(list_days), key=list_days.count
        )

    def get_least_busy_day(self):
        list_days = [order[2] for order in self.data]
        return min(
            set(list_days), key=list_days.count
        )
