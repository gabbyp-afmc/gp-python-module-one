#

class Trip:
    def __init__(self, destination, start_date, end_date, flights_cost, 
                 hotel_cost_per_day, other_cost_per_day):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.flights_cost = flights_cost
        self.hotel_cost_per_day = hotel_cost_per_day
        self.other_cost_per_day = other_cost_per_day

        if end_date < start_date:
            raise ValueError(f"end_date '{end_date}' must be after the start_date '{start_date}'")

        currencies = {
            "flights_cost": flights_cost,
            "hotel_cost_per_day": hotel_cost_per_day,
            "other_cost_per_day": other_cost_per_day,
        }

        for column, currencies in currencies.items():
            if currencies < 0:
                raise ValueError(f"Column '{column}' has negative value '{currencies}'")

    def __str__(self):
        return f"{self.destination}: {self.duration_days} days, ${self.total_cost:,}"

    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days

    @property
    def total_cost(self):
        per_day = self.hotel_cost_per_day + self.other_cost_per_day
        return (self.flights_cost + per_day * self.duration_days)