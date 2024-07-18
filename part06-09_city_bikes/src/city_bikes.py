# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename:str):
    with open(filename) as file_main:
        dic = {}
        for line in file_main:
            line = line.strip()
            parts = line.split(";")
            if parts[0] =="Longitude":
                continue
            dic[parts[3]] = (float(parts[0]), float(parts[1]))
    return dic

def distance(stations: dict, station1:str, station2:str):
    stat1 = stations[station1]
    stat2 = stations[station2]

    x_km = (stat1[0] - stat2[0]) * 55.26
    y_km = (stat1[1] - stat2[1]) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations:dict):
    
    cit1 = ""
    cit2 = ""
    distancemax =0

    for i in stations:
        for j in stations:
            calculated = distance(stations, i, j)
            if distancemax < calculated:
                cit1 = i
                cit2 = j
                distancemax = calculated
    
    return (cit1, cit2, distancemax)