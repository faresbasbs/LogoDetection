def db_add(link):
    import pymysql
            
    db = pymysql.connect(host='rm-l4v1rvq113r3ckr1x.mysql.me-central-1.rds.aliyuncs.com', port=3306, user='logo_db_acc', passwd='q1w2E#R$', database='new_db')

    cursor = db.cursor()

    line = 'INSERT INTO requests (ImgUrl) VALUES (%s);'

    val = (str(link))

    cursor.execute(line,val)

    db.commit()

    db.close()
