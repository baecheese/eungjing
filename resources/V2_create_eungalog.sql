CREATE TABLE `eungalog` (
	`id` bigint PRIMARY KEY AUTO_INCREMENT
	, user_name varchar(50)
	, weather varchar(3) NOT null
	, size varchar(10) not null
	, feature varchar(15) not null
	, satisfaction varchar(8) not null
	, eunga_drip text
	, FOREIGN KEY (user_name)
		REFERENCES users (name)
);