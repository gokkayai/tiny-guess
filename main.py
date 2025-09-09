# Bits of Uncertainty: A tiny number guessing game with a discrete math twist

APP_NAME = "Bits of Uncertainty"
DEFAULT_RANGE = (1, 100)
DIFFICULTIES = {"easy": (1, 50), "normal": (1, 100), "hard": (1, 1000)}
TIE_BREAK_RULE = "floor"  # midpoint rule: floor for even ranges
HOT_WARM_THRESHOLDS = {"hot": 3, "warm": 10}  # distance based hints

def main():
    pass  # entry point placeholder