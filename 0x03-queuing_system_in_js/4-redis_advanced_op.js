import redis from 'redis';


const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});
client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${ERROR_MESSAGE}`);
});

const setNewSchool = function(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

const displaySchoolValue = function(schoolName) {
	client.get(schoolName, (err, value) => {
		console.log(value);
  });
}

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'NewYork', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools','Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, reply) => {
	if (err) {
		console.log(err);
	} else {
		console.log('success', reply);
	}
});
