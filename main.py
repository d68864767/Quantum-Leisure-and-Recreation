# main.py

from quantum_leisure import QuantumLeisure

def main():
    # Create an instance of QuantumLeisure
    ql = QuantumLeisure()

    # Get a leisure idea
    leisure_idea = ql.get_leisure_idea()

    # Print the leisure idea
    print(leisure_idea)

if __name__ == "__main__":
    main()
