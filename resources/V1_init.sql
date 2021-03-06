/* 낡은 데이터베이스와 유저가 있다면 일단 제거하고서 시작. */
drop database EUNGJING;

drop user 'eungjing'@'localhost';

/* DB 생성 */
Create DATABASE EUNGJING DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/* User 생성 및 DB권한 주기 */
Create User eungjing@'localhost' identified by 'eungjing';

Grant all privileges on EUNGJING.* to eungjing@'localhost' identified by 'eungjing';

use EUNGJING;

/* Table 생성 */
Create Table USERS(
 name varchar(50) PRIMARY KEY,
 password varchar(100) Not Null,
 hint_Q VARCHAR(50) NOT NULL,
 hint_A VARCHAR(50) NOT NULL,
 job VARCHAR(20) NOT NULL,
 smoking BOOL NOT NULL,
 createDate DATETIME DEFAULT CURRENT_TIMESTAMP
);