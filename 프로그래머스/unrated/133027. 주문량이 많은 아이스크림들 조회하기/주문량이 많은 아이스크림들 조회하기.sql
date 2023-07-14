select a.flavor from first_half a
join (select flavor, sum(total_order) as total from july group by flavor 
      having sum(total_order)) b
on a.flavor = b.flavor
order by total+a.total_order desc limit 3
