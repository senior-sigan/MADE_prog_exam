from typing import List, Dict, Any, Tuple

event_seq = ['ordered', 'arrived', 'started', 'finished']

"""
1. ordered событие заказа такси. Описывается словами 
1.1. order_id — (идентификатор заказа, строка), 
1.2. user_id — (идентификатор пользователя, строка), 
1.3. ordered_at — (время заказа в Unix time, целое число), 
1.4. x (ожидаемое время подачи машины в минутах, целое число), 
1.5. y (ожидаемая длительность поездки в минутах, целое число)
2. arrived — машина подана пользователю. Описывается словами
2.1. order_id — (идентификатор заказа, строка), 
2.2. arrived_at — (время подачи машины, в Unix time, целое число)
3. started — пользователь сел в машине и началась поездка. Описывается словами order_id и started_at аналогично событию arrived.
4. finished — поездка завершилась. Описывается словами order_id и finished_at аналогично событию started.
"""


def calc_order_delay(order: Dict, waiting_time: int) -> Tuple[int, str]:
    ev = order['ordered']
    user_id = ev['user_id']
    ordered_at = ev['ordered_at']

    trip_time = (ev['x'] + waiting_time + ev['y'])*60
    expected_finish_time = ordered_at + trip_time

    actual_finish_time = order['finished']['finished_at']

    delay = actual_finish_time - expected_finish_time

    if delay <= 0:
        return 0, user_id

    arrived_at = order['arrived']['arrived_at']
    started_at = order['started']['started_at']
    taxi_wait_m = started_at - arrived_at

    if taxi_wait_m <= waiting_time*60:
        return delay, user_id

    return 0, user_id


def load_events(n_events: int):
    for _ in range(n_events):
        yield parse_event(input().split(" "))


def load_orders(n_events: int):
    orders = {}
    for event in load_events(n_events):
        order_id = event['order_id']
        event_type = event['type']
        if orders.get(order_id) is None:
            orders[order_id] = {event_type: event}
        orders[order_id][event_type] = event

        if len(orders[order_id]) == 4:
            yield orders[order_id]


def users_delays(orders, waiting_time):
    for order in orders:
        delay, user_id = calc_order_delay(order, waiting_time)
        if delay > 0:
            yield delay, user_id


def top_waiters(n_events: int, limit: int, waiting_time: int) -> List[str]:
    orders = load_orders(n_events)

    users = {}
    for delay, user_id in users_delays(orders, waiting_time):
        users.setdefault(user_id, 0)
        users[user_id] += delay

    users = [(user_id, users[user_id]) for user_id in users]
    users = sorted(users, key=lambda el: el[0], reverse=False)  # lexical sort
    users = sorted(users, key=lambda el: el[1], reverse=True)  # delay sort

    return [user[0] for user in users[:limit]]


def parse_event(event: List[str]) -> Dict[str, Any]:
    if event[0] == "ordered":
        return {
            "type": event[0],
            "order_id": event[1],
            "user_id": event[2],
            "ordered_at": int(event[3]),
            "x": int(event[4]),
            "y": int(event[5])
        }
    if event[0] == "arrived":
        return {
            "type": event[0],
            "order_id": event[1],
            "arrived_at": int(event[2])
        }
    if event[0] == "started":
        return {
            "type": event[0],
            "order_id": event[1],
            "started_at": int(event[2])
        }
    if event[0] == "finished":
        return {
            "type": event[0],
            "order_id": event[1],
            "finished_at": int(event[2])
        }

    raise f"UNKNOWN EVENT TYPE {event[0]}"


def main():
    x = int(input())
    for _ in range(x):
        e, n, k = map(lambda el: int(el), input().split(" "))
        users = top_waiters(n_events=e, limit=n, waiting_time=k)
        if len(users) == 0:
            print("-")
        else:
            print(" ".join(users))


if __name__ == "__main__":
    main()
