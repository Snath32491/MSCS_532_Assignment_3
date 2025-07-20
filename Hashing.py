import random

class HashTableChaining:
    def __init__(self, size=11, prime=109345121):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.p = prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash(self, key):
        k = hash(key)
        return ((self.a * k + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        result = ["\n--- Hash Table ---"]
        for i, chain in enumerate(self.table):
            chain_str = " -> ".join(f"({k}, {v})" for k, v in chain) if chain else "None"
            result.append(f"[{i}]: {chain_str}")
        return "\n".join(result)


def menu():
    ht = HashTableChaining(size=7)

    while True:
        print("\nOptions:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Print Hash Table")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            key = input("Enter key: ").strip()
            value = input("Enter value: ").strip()
            ht.insert(key, value)
            print("Inserted successfully.")
        elif choice == "2":
            key = input("Enter key to search: ").strip()
            result = ht.search(key)
            if result is not None:
                print(f"Found: {result}")
            else:
                print("Key not found.")
        elif choice == "3":
            key = input("Enter key to delete: ").strip()
            if ht.delete(key):
                print("Deleted successfully.")
            else:
                print("Key not found.")
        elif choice == "4":
            print(ht)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    menu()
4