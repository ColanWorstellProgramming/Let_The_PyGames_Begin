#!/usr/bin/python3

# Non - Collision
Passable = [   #Grass
    "G1",  # Plain Grass
    "G2",  # Top Left
    "G3",  # Top Middle
    "G4",  # Top Right
    "G5",  # Left Middle
    "G6",  # Right Middle
    "G7",  # Bottom Left
    "G8",  # Bottom Middle
    "G9",  # Bottom Right
    "G0",  # Grown Grass

    #Grass Corners
    "C1",  # Top Left Corner Curve
    "C2",  # Top Strait (Right Bottom Corner Curve)
    "C3",  # Top Strait (Left Bottom Corner Curve)
    "C4",  # Top Right Corner Curve
    "C5",  # Left Strait (Right Bottom Corner Curve)
    "C6",  # In Land (Right Bottom Corner Curve)
    "C7",  # In Land (Left Bottom Corner Curve)
    "C8",  # Right Strait (Right Bottom Corner Curve)
    "C9",  # Left Strait (Right Top Corner Curve)
    "C0",  # In Land (Right Top Corner Curve)
    "c1",  # In Land (Left Top Corner Curve)
    "c2",  # Right Strait (Right Top Corner Curve)
    "c3",  # Bottom Left Corner Curve
    "c4",  # Bottom Strait (Right Top Corner Curve)
    "c5",  # Bottom Strait (Left Top Corner Curve)
    "c6",  # Bottom Right Corner Curve

    #Dirt Path
    "P1",
    "P2", 
    "P3", 
    "P4", 
    "P5", 
    "P6", 
    "P7", 
    "P8", 
    "P9",
    "p1",
    "p2",
    "p3",
    "p4",

    #Pathing
    "L1",  
    "L2",  
    "L3",  
    "L4",  
    "L5", 
    "L6", 
    "L7",
    "L8", 
    "L9",
    "L0",
]
impassable = [
    # Collision
    #Fences
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9", 
    "F0",
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "f6",

    #Thick Tree
    "T1",
    "T2",
    "T3",
    "T4",

    #Thin Tree
    "T5" ,
    "T6",

    #Apple Tree
    "T7",
    "T8",
    "T9",
    "T0",

    #Bushes
    "B1",
    "B2",
    #Stumps
    "B3",
    "B4",    
    #Flowers
    "B5",
    "B6",
    "B7",
    "B8",
    "B9",

    #Rocks
    "y1", 
    "y2",   
    #Shrooms
    "S1",
    "S2",

    #Fruit
    "S3", 
    "S4",  
    #House
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "H7",
    "H8",

    #Doors
    "D1",
    #Collision On For "D2 Only"
    "D2",
    "D3",
    "D4",

    #Roof
    "R1", 
    "R3", 
    "R4",
    "R5", 
    "R6",
    "R7",
    "R8",
    "R9",
    "R0",
    "r1",
    "r2",
    "r3",   
    "r4",  
    "r5",

    #Water
    "W1",
    "W2",
    "W3",
    "W4"
]
print(Passable)
print(impassable)
