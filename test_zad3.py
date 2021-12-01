import math
import unittest


invoice1 = {
  "customer": "BigCo",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 55
    },
    {
      "playID": "as-like",
      "audience": 35
    },
    {
      "playID": "othello",
      "audience": 40
    }
  ]
}

plays1 = {
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "as-like": {"name": "As You Like It", "type": "comedy"},
  "othello": {"name": "Othello", "type": "tragedy"}
}



def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'
    def format_as_dollars(amount):
        return f"${amount:0,.2f}"
    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result

class statementTester(unittest.TestCase):
    def testString(self):
        self.assertIsInstance(statement(invoice1, plays1), str)
    def testNones(self):
        self.assertRaises(Exception, statement, None, None)
    def testInts(self):
        self.assertRaises(Exception, statement, 123, 421)
    def testGoodInput(self):
        self.assertEqual(statement({"customer": "fico", "performances": [{"playID": "Bad Play", "audience": 300}]}, {"Bad Play": {"name": "Bad Play", "type": "tragedy"}}),"Statement for fico\n Bad Play: $3,100.00 (300 seats)\nAmount owed is $3,100.00\nYou earned 270 credits\n")
    def testBadInput(self):
        self.assertRaises(Exception, statement, {"customeeer": "fico", "performances": [{"playID": "Bad Play", "audience": 300}]}, {"Bad Play": {"name": "Bad Play", "type": "tragedy"}})
    def testGoodInputBigCo(self):
        self.assertEqual(statement(invoice1, plays1), "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n")