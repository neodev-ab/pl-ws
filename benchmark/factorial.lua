function factorial(n)
	result = 1
	for i = 1, n do
		result = result * i
	end
	return result
end

for i = 0, 12 do
	print(factorial(i))
end
