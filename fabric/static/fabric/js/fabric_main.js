console.log('blah')


// displaying order in talbe
function In() {
	document.getElementById('order-out').style.display = 'block';
	document.getElementById('order-in').style.display = 'none';

	document.getElementById('order-out-table').style.display = 'none';
	document.getElementById('order-in-table').style.display = 'block';

	document.getElementById('order-out-title').style.display = 'none';
	document.getElementById('order-in-title').style.display = 'block';
}


// displaying order out
function Out() {
	document.getElementById('order-in').style.display = 'block';
	document.getElementById('order-out').style.display = 'none';

	document.getElementById('order-out-table').style.display = 'block';
	document.getElementById('order-in-table').style.display = 'none';

	document.getElementById('order-out-title').style.display = 'block';
	document.getElementById('order-in-title').style.display = 'none';
}