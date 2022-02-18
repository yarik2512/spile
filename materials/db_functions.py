from mysql.connector import connect, Error
import json

con = connect(
    host='37.140.192.174',
    database='u1490660_default',
    user='u1490660_default',
    password='Ds3Nb2d5wYj6UW28'
)
cur = con.cursor()


def new_task(user, obj):
    author = user
    typ = obj['type']
    question = obj['question']
    content = json.dumps(obj)
    global con, cur
    cur.execute(
        f"INSERT INTO tasks (id, author, type, question, content) "
        f"VALUES (NULL, '{author}', '{typ}', '{question}','{content}')"
    )
    con.commit()


def export_tasks_by_user(user):
    global con, cur
    cur.execute(
        f"SELECT * FROM tasks WHERE author='{user}'"
    )
    data = cur.fetchall()
    return data


def export_tests_by_user(id):
    global con, cur
    cur.execute(
        f"SELECT * FROM tests WHERE author='{id}'"
    )
    data = cur.fetchall()
    return data


def materials_get_by_author(id_author):
    global con, cur
    cur.execute(
        f"SELECT * FROM materials WHERE id_author='{id_author}'"
    )
    data = cur.fetchall()
    return data


def materials_get_by_discipline(discipline):
    global con, cur
    cur.execute(
        f"SELECT * FROM materials WHERE subject='{discipline}'"
    )
    data = cur.fetchall()
    return data


def materials_get_by_discipline_and_level(level, discipline):
    global con, cur
    cur.execute(
        f"SELECT * FROM materials WHERE subject='{discipline}' AND level='{level}'"
    )
    data = cur.fetchall()
    return data


def materials_update_status(status):
    global con, cur
    cur.execute(
        f"UPDATE materials SET status='{status}'"
    )


def materials_add(data):
    global con, cur
    cur.execute(
        f"INSERT INTO materials (id, id_author, title, level, subject, path, status) VALUES "
        f"(NULL, '{data['author']}', '{data['name']}', '{data['level']}', '{data['discipline']}', '{data['link']}', 0)"
    )
    con.commit()
