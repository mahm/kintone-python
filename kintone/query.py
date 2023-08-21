class Query:
    @staticmethod
    def now():
        return "NOW()"

    @staticmethod
    def last_month():
        return "LAST_MONTH()"

    @staticmethod
    def today():
        return "TODAY()"

    @staticmethod
    def this_month():
        return "THIS_MONTH()"

    @staticmethod
    def this_year():
        return "THIS_YEAR()"

    @staticmethod
    def login_user():
        return "LOGINUSER()"

    def __init__(self):
        self.query = []

    def build(self):
        return str(self)

    def field(self, code):
        condition = self.Field(self, code)
        self.query.append(condition)
        return condition

    def precede(self, inner_query):
        self.query.append(f"({inner_query.build()})")
        return self

    def and_(self):
        self.query.append("and")
        return self

    def or_(self):
        self.query.append("or")
        return self

    def order_by(self, field, direction='asc'):
        self.query.append(f'order by {field} {direction}')
        return self

    def limit(self, value):
        self.query.append(f'limit {value}')
        return self

    def offset(self, value):
        self.query.append(f'offset {value}')
        return self

    def __str__(self):
        return " ".join(map(str, self.query))

    def _function_string(self, function):
        return function

    class Field:
        def __init__(self, parent, code):
            self.parent = parent
            self.code = code
            self.condition = None
            self.other = None

        def equal(self, other):
            return self._save('=', other)

        def not_equal(self, other):
            return self._save('!=', other)

        def greater_than(self, other):
            return self._save('>', other)

        def less_than(self, other):
            return self._save('<', other)

        def greater_than_or_equal(self, other):
            return self._save('>=', other)

        def less_than_or_equal(self, other):
            return self._save('<=', other)

        def like(self, other):
            return self._save('like', other)

        def not_like(self, other):
            return self._save('not like', other)

        def in_(self, other):
            if isinstance(other, (list, tuple)):
                other = ", ".join(f'"{item}"' for item in other)  # ここでダブルクォーテーションを追加
                other = f"({other})"
            return self._save('in', other)

        def not_in(self, other):
            if isinstance(other, (list, tuple)):
                other = ", ".join(f'"{item}"' for item in other)  # ここでダブルクォーテーションを追加
                other = f"({other})"
            return self._save('not in', other)

        def _save(self, condition, other):
            if isinstance(other, (int, float)):
                self.condition = condition
                self.other = str(other)
                return self.parent
            self.condition = condition
            self.other = f'"{other}"' if not (other.endswith("()") or other.startswith('(')) else other
            return self.parent

        def __str__(self):
            return f'{self.code} {self.condition} {self.other}'
