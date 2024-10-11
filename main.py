class FamilyMember:
    def __init__(self, name, earning_status = True, earnings = 0):
        self.name = name
        self.earning_status = earning_status
        self.earnings = earnings

    def __str__(self):
        return (
            f"Name: {self.name}, Earning Status: {'Earning' if self.earning_status else 'Not Earning'}, Earnings: {self.earnings}")


class Expense:
    def __init__(self, value, category, description, date):
        self.value = value
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"Value: {self.value}, Category: {self.category}, Description: {self.description}, Date: {self.date}"


class FamilyExpenseTracker:
    def __init__(self):
        self.family_members = []
        self.expenses = []

    def add_family_member(self, name, earning_status= True, earnings = 0):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        member = FamilyMember(name, earning_status, earnings)
        self.family_members.append(member)

    def delete_family_member(self, member):
        self.family_members.remove(member)

    def update_family_member(self, member, name, earning_status, earnings):
        if member :
            member.earning_status = earning_status
            member.earnings = earnings

    def calculate_total_earnings(self):
        total_earnings = 0
        for member in self.family_members:
            if member.earning_status:
                total_earnings += member.earnings
        return total_earnings

    def add_expense(self, value, category, description, date):
        if value == 0:
            raise ValueError("Value cannot be zero")
        if not category.strip():
            raise ValueError("Category cannot be empty")

        expense = Expense(value, category, description, date)
        self.expenses.append(expense)

    def delete_expense(self, expense):
        self.expenses.remove(expense)

    def merge_similar_category(self, value, category, description, date):
        if value == 0:
            raise ValueError("Value cannot be zero")
        if not category.strip():
            raise ValueError("Category cannot be empty")

        existing_expense = None

        for expense in self.expenses:
            if expense.category == category:
                existing_expense = expense
                break

        if existing_expense:
            existing_expense.value += value
            if description:
                existing_expense.description += description
        else:
            self.add_expense(value, category, description, date)

    def calculate_total_expenses(self):
        total_expenses = sum(expense.value for expense in self.expenses)
        return total_expenses


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expense_tracker = FamilyExpenseTracker()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
