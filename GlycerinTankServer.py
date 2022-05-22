from BaseComponentServer import BaseComponentServer
from Enums.Ports import ServersPorts
import sys


class GlycerinTankServer(BaseComponentServer):
    def __init__(self, host, port) -> None:
        super().__init__(host, port)
        self.remaining_glycerin = 0

    def signal_handler(self, sig, frame):
        sys.exit(0)

    def get_state(self):
        return {"occupied_capacity": self.remaining_glycerin}

    def process_substance(self, glycerin_payload: dict) -> None:
        glycerin_amount = glycerin_payload["glycerin_amount"]
        self.remaining_glycerin += glycerin_amount

        self.log_info(f"Received {self.glycerin_amount}l of glycerin")

        return self.get_state()


if __name__ == "__main__":
    GlycerinTankServer('localhost', ServersPorts.glycerin_tank).run()
