select animal_type, count(distinct animal_id) as count from animal_ins
group by animal_type
order by animal_type