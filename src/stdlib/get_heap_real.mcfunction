execute store result score $search1 namespace run scoreboard players operation $search2 namespace = $index namespace
scoreboard players operation $search1 namespace /= $1024 namespace
execute unless score $search1 namespace = $lasta namespace run data modify storage namespace:main heap[].selected set value 0
execute unless score $search1 namespace = $lasta namespace run function namespace:tree/heap_select
scoreboard players operation $lasta namespace = $search1 namespace
scoreboard players operation $search2 namespace %= $1024 namespace
function namespace:tree/heap_get