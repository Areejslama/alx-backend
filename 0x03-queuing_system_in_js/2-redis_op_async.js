import redis from 'redis';
import { promisify } from 'util';

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

async function displaySchoolValue(schoolName) {
    const getAsync = promisify(client.get).bind(client);
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.log('Error fetching value:', error);
    }
}

(async () => {
    await setNewSchool('Holberton', 'School');
    await displaySchoolValue('Holberton');

    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
