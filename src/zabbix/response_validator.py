from loguru import logger

class ResponseValidator:
    @staticmethod
    def validate(response) -> tuple[float, float, float] | None:
        data = response.json()
        generation = data.get("generationPower")
        consumption = data.get("usePower")
        grid = data.get("wirePower")

        if consumption is None or consumption == 0:
            logger.error("Invalid response data")
            logger.error(f"Status: {response.status_code}")
            logger.error(f"Data: {data}")
            return None

        return generation, consumption, grid