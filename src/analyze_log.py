import csv


def get_item_most_ordered_by_client(client, data):
    filtered_orders_by_client = [
        order[1] for order in data if order[0] == client
    ]
    return max(
        set(filtered_orders_by_client), key=filtered_orders_by_client.count
    )


def get_order_item_count(client, item, data):
    filtered_orders_by_client = [
        order[1] for order in data if order[0] == client
    ]
    return filtered_orders_by_client.count(item)


def get_unordered_items_by_client(client, data):
    available_items = set([order[1] for order in data])
    filtered_items_orderer_by_client = set(
        [order[1] for order in data if order[0] == client]
    )
    for item in filtered_items_orderer_by_client:
        available_items.remove(item)
    return available_items


def get_days_that_client_never_camed(client, data):
    available_days = set([order[2] for order in data])
    filtered_days_that_client_never_camed = set(
        [order[2] for order in data if order[0] == client]
    )
    for days in filtered_days_that_client_never_camed:
        available_days.remove(days)
    return available_days


def analyze_log(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding="utf-8") as csv_file:
            data = list(csv.reader(csv_file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    maria_most_ordered_item = get_item_most_ordered_by_client("maria", data)
    arnaldo_item_ordered = get_order_item_count("arnaldo", "hamburguer", data)
    joao_unordered_items = get_unordered_items_by_client("joao", data)
    days_that_joao_never_camed = get_days_that_client_never_camed("joao", data)

    with open("data/mkt_campaign.txt", mode="w", encoding='utf-8') as file:
        file.write(
          f"{maria_most_ordered_item}\n"
          f"{arnaldo_item_ordered}\n"
          f"{joao_unordered_items}\n"
          f"{days_that_joao_never_camed}\n"
        )
