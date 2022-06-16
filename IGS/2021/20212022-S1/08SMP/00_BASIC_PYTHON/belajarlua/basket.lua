
basket = {"apple", "orange", "melon"}

for num,item in pairs(basket) do
	if item == "apple" then
		print(num, "cut",item)
	elseif item == "orange" then
		print(num, "peel", item)
	elseif item == "melon" then
		print(num, "smash", item)
	end
end