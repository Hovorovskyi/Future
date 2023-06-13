INSERT INTO user_table
VALUES
(123, 'Alice', 'alice@gmail.com'),
(456, 'Bob', 'bob@inbox.com'),
(789, 'Eve', 'eve@gmail.com'),
(654, 'Dave', 'dave@gmail.com'),
(987, 'Fred', 'fred@mail.ua'),
(321, 'Dima', 'dima@gmail.com'),
(1, 'Vlad', 'vlad@gmail.com'),
(2, 'Dima', 'dmitriy@gmail.com'),
(3, 'Vladislav', 'vladislav@inbox.com'),
(4, 'Sasha', 'oleksandr@mail.ua')

SELECT * FROM user_table

INSERT INTO post
VALUES
(1, 'Hello, world!', 123, '2021-01-01'),
(2, 'Hello, friends!', 456, '2021-01-02'),
(3, 'Welcome!', 123, '2021-01-03'),
(4, 'Have a good day!', 789, '2021-01-04'),
(5, 'Slava Ukraine!', 2, '2023-05-22'),
(6, 'Heroyam Slava!', 1, '2023-05-22'),
(7, 'Give Ukraine F-16!', 4, '2023-05-02')

INSERT INTO like_table
VALUES
(1, 456, 1),
(2, 123, 2),
(3, 789, 3),
(4, 456, 4),
(5, 3, 5),
(6, 2, 6),
(7, 1, 7)

INSERT INTO follower
VALUES
(1, 123, 654),
(2, 456, 654),
(3, 123, 987),
(4, 789, 654),
(5, 987, 789),
(6, 987, 456),
(7, 1, 2),
(8, 2, 1),
(9, 4, 1),
(10, 2, 4)


INSERT INTO comment_table
VALUES
(1, 123, 'Good!', 4),
(2, 789, 'Have fun!', 1),
(3, 789, 'Strong', 2),
(4, 456, 'Yeeaaar!', 3),
(5, 4, 'Heroyam Slava!', 5),
(6, 2, 'Give F-16!', 7),
(7, 1, 'Pray to Ukraine!', 7)

SELECT * FROM user_table

SELECT post.post_id AS post, COUNT(like_table.like_id) AS likes
FROM post
INNER JOIN like_table ON post.post_id = like_table.post_id
GROUP BY post.post_id

SELECT post.post_id AS post, COUNT(like_table.like_id) AS likes
FROM post
INNER JOIN like_table ON post.post_id = like_table.post_id
WHERE like_table.like_id > 100
GROUP BY post.post_id

SELECT comment_text
FROM comment_table
WHERE user_id = 123

SELECT user_table.user_name, COUNT(follower_id) AS followers
FROM follower
INNER JOIN user_table ON user_table.user_id = follower.user_id
GROUP BY user_table.user_name

SELECT post_text
FROM post
INNER JOIN like_table ON post.post_id = like_table.post_id
WHERE user_id = 123

SELECT user_table.user_name, COUNT(comment_text) AS commets
FROM user_table
JOIN comment_table ON comment_table.user_id = user_table.user_id
GROUP BY user_table.user_name

SELECT user_name
FROM user_table
JOIN like_table ON like_table.user_id = user_table.user_id
WHERE post_id = 1

SELECT post.post_text AS post
FROM post
JOIN comment_table ON post.post_id = comment_table.post_id
GROUP BY post.post_text
HAVING COUNT(comment_table.comment_id) >= 5
