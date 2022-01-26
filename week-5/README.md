### ● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
    INSERT INTO member VALUES(NULL,'test','test','test',DEFAULT,DEFAULT);
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-1.png" width="750px" height="100px">

    INSERT INTO member VALUES(NULL,'愛麗絲','Alice','Alice',12,DEFAULT);
    INSERT INTO member VALUES(NULL,'克萊兒','Claire','Claire',24,DEFAULT);
    INSERT INTO member VALUES(NULL,'克莉絲汀','Kristin','Kristin',100,DEFAULT);
    INSERT INTO member VALUES(NULL,'瑞琪兒','Rachel','Rachel',24,DEFAULT);
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-1-1.png" width="780px" height="180px">

### ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
    SELECT * FROM member;
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-2.png" width="780px" height="180px">

### ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
    SELECT * FROM member ORDER BY time;
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-3.png" width="780px" height="180px">

### ● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
    SELECT * FROM member ORDER BY time LIMIT 1,3;
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-4.png" width="780px" height="140px">

### ● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
    SELECT * FROM member where username='test';
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-5.png" width="750px" height="100px">

### ● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
    SELECT * FROM member where username='test' AND password='test';
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-6.png" width="750px" height="100px">

### ● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
    UPDATE member SET name='test2' WHERE username='test';
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/3-7.png" width="785px" height="180px">

### ● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
    SELECT COUNT(DISTINCT username) FROM member;
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/4-1.png" width="280px" height="100px">

### ● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
    SELECT SUM(follower_count) FROM member;
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/4-2.png" width="235px" height="100px">

### ● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
    SELECT AVG(follower_count) FROM member;
<img src="https://github.com/ruth26582/wehelp-assignments/blob/main/week-5/image/4-3.png" width="240px" height="100px">
