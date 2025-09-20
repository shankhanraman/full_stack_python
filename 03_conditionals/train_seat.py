# Building a Train seat information system 
# You're building a ticket info system for a railway app.
# Based on seat type , show its features.
# Task:
# . Input : "sleeper", "AC", "luxury", "general"
# . Match using match-case 
# . Unknown -> show:"Invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/luxury/general): ").strip().lower()
match seat_type:
    case "sleeper":
        print("Sleeper: Non-AC, economical, suitable for budget travelers.")
    case "ac":
        print("AC: Air-conditioned, comfortable, mid-range option.")
    case "luxury":
        print("Luxury: Premium amenities, spacious seating, high-end experience.")
    case "general":
        print("General: Basic seating, affordable, no reservations needed.")
    case _:
        print("Invalid seat type")