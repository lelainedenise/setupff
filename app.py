from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_metrics(revenue, units_sold, selling_price, cost_of_goods_sold, operating_expenses, interest, taxes):

    average_revenue = revenue / units_sold
    operating_cost = cost_of_goods_sold + operating_expenses
    gross_profit = revenue - cost_of_goods_sold
    gross_profit_margin_rate = (gross_profit / revenue) * 100
    operating_profit_margin_rate = ((gross_profit - operating_expenses) / revenue) * 100
    net_profit_margin_rate = (((gross_profit - operating_expenses) - (interest + taxes)) / revenue) * 100
    return_of_investment = (((gross_profit - operating_expenses) - (interest + taxes)) / (cost_of_goods_sold + units_sold)) * 100

    color_green = lambda x: 'green' if x > 0 else 'black'
    color_red = lambda x: 'red' if x < 0 else 'black'

    return {
        'average_revenue': format(average_revenue, '.2f'),
        'operating_cost': format(operating_cost, '.2f'),
        'gross_profit': format(gross_profit, '.2f'),
        'gross_profit_margin_rate': format(gross_profit_margin_rate, '.2f'),
        'operating_profit_margin_rate': format(operating_profit_margin_rate, '.2f'),
        'net_profit_margin_rate': format(net_profit_margin_rate, '.2f'),
        'return_of_investment': format(return_of_investment, '2f'),
        }


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        revenue = float(request.form['revenue'])
        units_sold = float(request.form['units_sold'])
        selling_price = float(request.form['selling_price'])
        cost_of_goods_sold = float(request.form['cost_of_goods_sold'])
        operating_expenses = float(request.form['operating_expenses'])
        interest = float(request.form['interest'])
        taxes = float(request.form['taxes'])

        metrics = calculate_metrics(revenue, units_sold, selling_price, cost_of_goods_sold, operating_expenses, interest, taxes)

        return render_template('result.html', metrics=metrics)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
