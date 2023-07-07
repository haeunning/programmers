-- 코드를 입력하세요
# 22년 10월 게시물 제목, 게시글 ID, 댓글 ID, 댓글내용, 댓글 작성일

select TITLE, a.BOARD_ID, REPLY_ID, b.WRITER_ID, b.CONTENTS, date_format(b.created_date,'%Y-%m-%d') as CREATED_DATE
from used_goods_board a join used_goods_reply b on a.board_id=b.board_id
where a.created_date like '2022-10%'
order by CREATED_DATE, title