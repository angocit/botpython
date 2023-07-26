# coding=utf-8
import pymysql.cursors
import time
import os, sys
import urllib.request
import urllib.parse
import requests
from datetime import datetime
from urllib.request import urlopen
connection = pymysql.connect(host='localhost',
                             user='news',
                             password='d/4[A]_0]5lvWKf6',
                             db='news',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def insert_famous(
                    name,
                    birth,                    
                    place_of_birth,
                    country,
                    profession,
                    horoscope,
                    biography,
                    dating,
                    parent,
                    father,
                    mother,
                    siblings,
                    spouse,
                    children,
                    net_worth,
                    salary,
                    source_of_income,
                    cars,
                    house,
                    height,
                    weight,
                    body_measurements,
                    eye_color,
                    hair_color,
                    shoe_size,
                    image
                    ):
    with connection.cursor() as cursor:
        famous = "select * from famous where name = %s and birth = %s and profession =%s limit 1"
        number_of_rows = cursor.execute(famous, (name,birth,profession))
        if number_of_rows ==0:
            cur2 = connection.cursor()
            sql ="insert into famous(name,birth,place_of_birth,country,profession,horoscope,biography,dating,parent,father,mother,siblings,spouse,children,net_worth,salary,source_of_income,cars,house,height,weight,body_measurements,eye_color,hair_color,shoe_size,image,slug) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            slug = linkthanthien(name)
            cur2.execute(sql, (
                                name,
                                birth,                                
                                place_of_birth,
                                country,
                                profession,
                                horoscope,
                                biography,
                                dating,
                                parent,
                                father,
                                mother,
                                siblings,
                                spouse,
                                children,
                                net_worth,
                                salary,
                                source_of_income,
                                cars,
                                house,
                                height,
                                weight,
                                body_measurements,
                                eye_color,
                                hair_color,
                                shoe_size,
                                image,
                                slug
                                ))
            id = cur2.lastrowid
            # select = connection.cursor()
            # select.execute("select * from theloai where tentheloai = %s limit 1", cat)
            # records = select.fetchall()
            # return records[0]['id']
            print('Them moi '+name+' thanh cong')
            connection.commit()
def update_famous(
                    name,
                    birth,
                    profession,
                    biography,
                    dating,
                    parent                   
                    ):
    with connection.cursor() as cursor:
        famous = "select * from famous where name = %s and birth = %s and profession =%s limit 1"
        number_of_rows = cursor.execute(famous, (name,birth,profession))
        if number_of_rows > 0:
            records = cursor.fetchall()
            idfamous = records[0]['id']
            cur2 = connection.cursor()
            sql ="update famous set biography = %s,dating=%s,parent=%s where id = %s"
            slug = linkthanthien(name)
            cur2.execute(sql, (
                                biography,
                                dating,
                                parent,
                                str(idfamous)
                                ))
            print('Cap nhat '+name+' thanh cong')
            connection.commit()
def id_country(name):
    id = 0
    name=name.strip()
    with connection.cursor() as cursor:
        country = "select * from country where name = %s limit 1"
        number_of_rows = cursor.execute(country, name)
        if number_of_rows ==0:
            cur2 = connection.cursor()
            sql ="insert into country(name,slug) values (%s,%s)"
            slug = linkthanthien(name)
            cur2.execute(sql, (name,slug))
            id = cur2.lastrowid
            # select = connection.cursor()
            # select.execute("select * from theloai where tentheloai = %s limit 1", cat)
            # records = select.fetchall()
            # return records[0]['id']
            connection.commit()

        else:
            records = cursor.fetchall()
            id = records[0]['id']
            connection.commit()
    return id
def id_profession(name):
    id = 0
    name=name.strip()
    with connection.cursor() as cursor:
        profession = "select * from profession where name = %s limit 1"
        number_of_rows = cursor.execute(profession, name)
        if number_of_rows ==0:
            cur2 = connection.cursor()
            sql ="insert into profession(name,slug) values (%s,%s)"
            slug = linkthanthien(name)
            cur2.execute(sql, (name,slug))
            id = cur2.lastrowid
            # select = connection.cursor()
            # select.execute("select * from theloai where tentheloai = %s limit 1", cat)
            # records = select.fetchall()
            # return records[0]['id']
            connection.commit()

        else:
            records = cursor.fetchall()
            id = records[0]['id']
            connection.commit()
    return id
def linkthanthien(str):
    str = str.lower()
    for ch in ['à','á','ả','ạ','ã','â','ấ','ầ','ậ','ẫ','ẩ','ă','ằ','ắ','ẳ','ẵ','ặ','á','à']:
        str = str.replace(ch, 'a')
    for ch in ['è','é','ẻ','ẽ','ẹ','ê','ề','ế','ể','ễ','ệ']:
        str = str.replace(ch, 'e')
    for ch in ['ì','í','ỉ','ĩ','ị']:
        str = str.replace(ch, 'i')
    for ch in ['ò','ó','ỏ','õ','ọ','ơ','ờ','ớ','ở','ỡ','ợ','ô','ồ','ố','ổ','ỗ','ộ']:
        str = str.replace(ch, 'o')
    for ch in ['ù','ú','ủ','ũ','ụ','ư','ừ','ứ','ử','ữ','ự','ú']:
        str = str.replace(ch, 'u')
    for ch in ['ỳ','ý','ỷ','ỹ','ỵ']:
        str = str.replace(ch, 'y')
    for ch in ['!','@','#','$','%','^','&','*','(',')','_','"',"'",'\\','/','{','}','[',']','>','<','?','`','~','+','.',',','❤',':',';','|','⭐']:
        str = str.replace(ch, '')
    str = str.replace('đ','d')
    str = str.replace(' ', '-')
    return str