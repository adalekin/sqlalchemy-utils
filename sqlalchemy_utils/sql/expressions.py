from typing import List

from sqlalchemy.orm import Query
from sqlalchemy.sql.expression import ClauseElement


def or_(query: Query, *clauses: List[ClauseElement]):
    q = None

    for c in clauses:
        if q is None:
            q = query.filter(c)
        else:
            q = q.union(query.filter(c))

    return q
