hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
end_time=float((((hour*60)+ mins)+dura)/60)
print(float(end_time))