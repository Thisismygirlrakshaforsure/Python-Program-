# Function to calculate the area of a rectangular room 1
def calculate_area(length, width):
    return length * width

# Collect the number of room 2
num_rooms = int(input("Enter the number of rooms: "))

# Initialize total area room
total_area = 0

# Collect dimensions for each room 3
for i in range(num_rooms):
    print(f"\nRoom {i + 1}")
    length = float(input("Enter length (in meters): "))
    width = float(input("Enter width (in meters): "))
    area = calculate_area(length, width)
    print(f"Area of Room {i + 1}: {area:.2f} square meters")
    total_area += area

# Display total area
print(f"\nTotal Floor Area: {total_area:.2f} square meters")

#CopiedbyChatGPT...Hence4hastagsusedherewithdifferentoperations<3forpython
