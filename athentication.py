import binascii
from datetime import datetime
import hashlib
import os

from psycopg2._psycopg import AsIs

from data_base_connection import cur, conn


def sign_up(first_name: str, last_name: str, national_num: int, email, password: str) -> dict:
    from cloud_management import UserTable
    hashed_password = hash_password(password)
    insertion_sql = 'INSERT INTO "%s" (name, f_name, email, hashd_password,national_num)VALUES (%s,%s,%s,%s, %s);'
    cur.execute(insertion_sql, (AsIs(UserTable), first_name, last_name, email, hashed_password, national_num))
    conn.commit()
    return sign_in(email=email, password=password)


def sign_in(email: str, password: str, is_admin=False) -> dict:
    from cloud_management import CustomerInfo, UserTable, AdminTable
    select_query = 'select * from public."%s"' + " where %s=%s"
    if is_admin:
        cur.execute(select_query, (AsIs(AdminTable), AsIs('email'), email))
    else:
        cur.execute(select_query, (AsIs(UserTable), AsIs('email'), email))
    rows = cur.fetchall()
    if len(rows) != 0:
        if not is_admin:
            boolean = verify_password(rows[0][4], password)
        else:
            boolean = verify_password(rows[0][2], password)
        if boolean:
            select_query = 'select * from public."%s"' + " where %s=%s"
            if not is_admin:
                cur.execute(select_query, (AsIs(CustomerInfo), AsIs('email'), email))
                rows = cur.fetchall()
                for row in rows:
                    return {
                        "customer_id": row[0],
                        "first_name": row[1],
                        "last_name": row[2],
                        "wallet_amount": row[3],
                        "email": row[4]
                    }
            else:
                return {
                    "id": rows[0][0],
                    "email": rows[0][1],
                    "is_super":rows[0][3]
                }


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

# sign_up('vida', 'gharavian', 123456, 'mgharavian@gmail.com', '123456')
