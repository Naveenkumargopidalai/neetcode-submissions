class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for op in operations:
            if op == '+':
                score = record[-1] + record[-2]
                record.append(score)
                total += score
            elif op == 'D':
                score = 2 * record[-1]
                record.append(score)
                total += score
            elif op == 'C':
                removed = record.pop()
                total -= removed
            else:
                score = int(op)
                record.append(score)
                total += score

        return total