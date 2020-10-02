from django.db import connection


def exec_query(sql, params, t=0):
    # t = 0 / 1
    # 0 = expecting row affected
    # 1 = expecting return data
    with connection.cursor() as c:
        c.execute(sql, params)
        if t == 0:
            row = c.rowcount

        elif t == 1:
            row = _dictfetchall(c)

        c.close

    return row


def _dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
