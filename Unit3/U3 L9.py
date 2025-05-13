import math

def hx(TdegC: float, dewPtC: float) -> float:
    """
     * Calculates the humidex, given
     * TdegC, the temp in degrees C
     * dewPtC, the dewpoint in degrees C
     *
     * Returns:
     * hTemp: humidex in degrees C
    """
    hTemp = 0.0

    p = 5417.753 * ((1 / 273.15) - (1 / (273.15 + dewPtC)))
    hTemp = TdegC + 5.0 / 9.0 * (6.11 * math.exp(p) - 10)

    return hTemp

def humidex(hTemp):
  hTemp = hx(T, D)
  
  if hTemp < 30:
    return "Normal"
  elif 30 <= hTemp < 39:
    return "Causes some discomfort"
  elif 40 <= hTemp < 44:
    return "Causes great discomfort"
  elif 45 <= hTemp < 49:
    return "Considered dangerous"
  else:
    return "Heat stroke is very likely"

T = 28.0
D = 26.0
h = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f Warning: %s" % (h, T, D, humidex(h)))

T = 30.0
D = 20.0
h = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f Warning: %s" % (h, T, D, humidex(h)))

T = 26.0
D = 28.0
h = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f Warning: %s" % (h, T, D, humidex(h)))
