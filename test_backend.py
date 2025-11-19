from backend import calc_aqi_level
from config import AQI_INTERVALS

def test_so2_level_calculation():
    """
    Tests the case we found in the debugger.
    SO2 concentration of "77" should be Level 2 ("Good").
    """
    concentration = "77"
    intervals = AQI_INTERVALS["so2"]

    # We expect Level 2 (Good)
    expected_level = 2
    calculated_level = calc_aqi_level(concentration, intervals)
    assert calculated_level == expected_level

def test_co_level_calculation():

    concentration = "684.85"  # CO concentration
    
    intervals = AQI_INTERVALS["co"]  # CO AQI intervals
    expected_level = 1  # Expected level from config.py
    calculated_level = calc_aqi_level(concentration, intervals)  # Calculate AQI level

    assert calculated_level == expected_level  # Check if it matches

