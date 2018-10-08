--select * from get_web_data_platformstatistics ORDER BY get_time desc limit 1
--SELECT * FROM get_web_data_platformstatistics WHERE  get_time > datetime('2018-09-10 00:00:00') and vid_id =2  limit 1
-- SELECT * from get_web_data_videodetail where video_id = 25 ORDER BY play DESC ;

SELECT
  a.video_id,
  b.title,
  datetime(b.created, 'unixepoch', 'localtime')         AS create_time,
  min(a.get_time) as min_time,
  min(cast(a.play AS INT)) as min_num,
  (case when min('2018-10-01 00:00:00') > datetime(b.created, 'unixepoch', 'localtime')  then min(cast(a.play AS INT)) else 0 end) AS min_num1,
  Max(cast(a.play AS INT)) as max_num,
  (Max(cast(a.play AS INT)) -  ( (case when min('2018-10-01 00:00:00') > datetime(b.created, 'unixepoch', 'localtime')  then min(cast(a.play AS INT)) else 0 end)) ) AS addNum
FROM get_web_data_videodetail a, get_web_data_videolist b
WHERE a.video_id = b.id
 -- and a.get_time > datetime('2018-10-01 00:00:00')
  and create_time  > datetime('2018-10-01 00:00:00')
GROUP BY video_id
ORDER BY addNum DESC
LIMIT 10;