user_info={
    'name':'abd',
    'age':20,
    'fav_movie':['tarzan','avengers'],
    'schools':['aradhna','exotica']
}

# add data:
user_info['name']=['bha']
print(user_info)


# pop data:
popped_item=user_info.pop('fav_movie')
print(f"popped_item is{popped_item}")
print(user_info)

#update data:
more_info={'state':'gujarat'}
user_info.update(more_info)
print(user_info)