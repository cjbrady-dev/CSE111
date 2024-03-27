def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    fruit_list.reverse()
    print(fruit_list)

    fruit_list.append("orange")
    print(fruit_list)

    fruit_list.insert(2,"cherry")
    print(fruit_list)

    fruit_list.remove(1)
    print(fruit_list)

    fruit_list.pop(-1)
    print(fruit_list)

    fruit_list.sort()
    print(fruit_list)

    fruit_list.clear()
    print(fruit_list)
    
if __name__ == "__main__":
    main()