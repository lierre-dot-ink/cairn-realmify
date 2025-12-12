from dataclasses import dataclass


@dataclass
class Territory:
    landmarks: dict = None


def generate_territory(config):
    t = Territory()
    t.landmarks = config
    return t
