import requests


def get_rate(original_currency, new_currency):
    url = "https://open.er-api.com/v6/latest/" + original_currency
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or new_currency not in data['rates']:
        print("Error fetching exchange rates")
        return None

    return data['rates'][new_currency]


def currency_converter():
    original_currency = input("From currency: ").upper()
    new_currency = input("To currency: ").upper()
    amount = float(input("Amount in " + original_currency + ": "))

    rate = get_rate(original_currency, new_currency)
    if rate != None:
        converted_amount = amount * rate
        print(str(amount) + " " + original_currency + " = " + str(converted_amount) + " " + new_currency)


def main():
    currency_converter()


if __name__ == "__main__":
    main()
