function factorial(n) {
	let result = 1;
	for (let i = 1; i <= n; ++i)
		result *= i;
	return result;
}

for (let i = 0; i <= 12; i++) {
	console.log(factorial(i))
}
