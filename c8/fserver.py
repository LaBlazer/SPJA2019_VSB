from xmlrpc.server import SimpleXMLRPCServer

class Forecast(object):
    """
    Reprezentuje predpoved. V instancnich promennych jsou reprezentovany hodnoty
    predpovedi.
    """

    def __init__(self, description, wind_force, temperature):
        self._description = description
        self._wind_force = wind_force
        self._temperature = temperature

    def get_list(self):
        return self._description, self._wind_force, self._temperature

class ForecastCalendar(object):
    """
    Reprezentuje predpovedi pro nekolik dni. Data predpovedi jsou ulozena ve
    slovniku. Klicem je datum, hodnotou pak instance tridy Forecast. Vkladani
    predpovedi metodou update_forecast je chraneno heslem, ktere je predano v
    konstruktoru. Startovaci data jsou tektez predana v konstruktoru.
    """
    
    def __init__(self, initial_values, password):
        self._password = password
        self._forecasts = {}

        if isinstance(initial_values, dict):
            for k, v in initial_values.items():
                if isinstance(v, Forecast):
                    self._forecasts[k] = v

    def get_forecast(self, date):
        if date in self._forecasts:
            l = self._forecasts[date].get_list()
            return f"Description: {l[0]}, Wind force: {l[1]}, Temperature: {l[2]}"

        return "No forecast"

    def update_forecast(self, password, date, description, wind_force, temperature):
        if password == self._password:
            self._forecasts[date] = Forecast(description, wind_force, temperature)
            return "OK"

        return "No update"
        
def main():
    initial_state = {
        "20017-11-05": Forecast("super cloudy", 33, 10),
        "20017-11-06": Forecast("super sunny", 1, 40),
        "20017-11-07": Forecast("super rainy", 60, 15),
        "20017-11-08": Forecast("super foggy", 5, 16)
    }

    fcalendar = ForecastCalendar(initial_state, password = "master-of-weather")

    server_address = ('localhost', 10001)
    server = SimpleXMLRPCServer(server_address)
    server.register_instance(fcalendar)
    server.register_introspection_functions()
    print("Starting Weather XML-RPC server, use <Ctrl-C> to stop")
    server.serve_forever()

if __name__ == "__main__":
    main()
