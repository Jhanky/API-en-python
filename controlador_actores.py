from flask import make_response, jsonify
from bd import get_connection


def insert_actor(first_name, last_name, last_update):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO actor(first_name, last_name, last_update) VALUES (%s, %s, %s)',
                       (first_name, last_name, last_update))
    connection.commit()
    connection.close()


def get_actors():
    connection = get_connection()
    actors = ()
    with connection.cursor() as cursor:
        cursor.execute('SELECT actor_id, first_name, last_name, last_update FROM actor LIMIT 5 ')
        actors = cursor.fetchall()
    connection.close()
    return make_response(jsonify(actors), 200)


def get_actor_by_id(id):
    connection = get_connection()
    actor = None
    with connection.cursor() as cursor:
        cursor.execute('SELECT actor_id, first_name, last_name, last_update FROM actor WHERE actor_id = %s', (id,))
        actor = cursor.fetchone()
    connection.close()
    return make_response(jsonify(

        data={
            "actor_id": actor[0],
            "first_name": actor[1],
            "last_name": actor[2],
            "last_update": actor[3]
        }

    ), 200)


def delete_actor_by_id(id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM actor WHERE actor_id = %s', (id,))
    connection.commit()
    connection.close()


def update_actor(name, lastname, id):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('UPDATE actor t SET t.first_name = %s, t.last_name  = %s WHERE t.actor_id = %s', (name, lastname, id))
    connection.commit()
    connection.close()
