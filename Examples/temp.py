import random
import time


Temperature_sample = [random.uniform(34,40)for i in range (10)]
time.sleep(0.5)
humidity_sample = [random.uniform(350,500)for i in range (10)]
time.sleep(0.5)
pressure_sample = [random.uniform(750,800)for i in range (10)]
time.sleep(0.5)
light_levels_sample = [random.uniform(30,40)for i in range (10)]
time.sleep(0.5)


print("Temperature_sample: ", Temperature_sample)
print("Humidity_sample: ", humidity_sample)
print("Pressure_sample", pressure_sample)
print("Light_Levels_sample: ", light_levels_sample)
average_temperature = sum(Temperature_sample)/len(Temperature_sample)
average_humidity = sum(humidity_sample)/len(humidity_sample)
average_pressure = sum(pressure_sample)/len(pressure_sample)
average_light_levels = sum(light_levels_sample)/len(light_levels_sample)
print("Average Temperature: ", average_temperature)
print("Average Humidity: ", average_humidity)
print("Average Pressure: ", average_pressure)
print("Average Light Levels: ", average_light_levels)