execute if score $index namespace matches 0 run say AHHAAHHAHAHAHAHAH errorororoor attempting to dereference NULL!!!!
# static memory
execute if score $index namespace matches ..536870911 run function namespace:get_heap_real
# allocated memory
execute if score $index namespace matches 536870912..1073741823 run function namespace:get_alloc
# global variables' addresses
execute if score $index namespace matches 1073741824..1610612735 run function namespace:tree/var_get
# local variables' addresses
execute if score $index namespace matches 1610612736.. run function namespace:get_local